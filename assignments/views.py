from paypalcheckoutsdk.orders import OrdersCreateRequest
from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypalcheckoutsdk.core import SandboxEnvironment, PayPalHttpClient,LiveEnvironment
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse_lazy,reverse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geoip2 import GeoIP2
from django.db.models import Q,F,Avg,Sum,Count
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

# from django.http import HttpRe
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.views.generic import UpdateView
from bootstrap_modal_forms.generic import (BSModalCreateView,
                                           BSModalUpdateView,
                                           BSModalReadView,
                                           BSModalDeleteView)
from .forms import AssignmentDocumentForm,AssignmentEditForm,UploadAssignmentForm,AssignWriterForm
from .models import Assignment
from payments.models import Order,OrderItem
from chat.forms import ComposeForm
from paypal.standard.forms import PayPalPaymentsForm
from chat.models import ChatMessage,Thread
from authentication.models import User,Notification
from django.urls import reverse,reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from authentication.models import User
from datetime import datetime
import stripe

# Create your views here.
def AssignmentCategoryView(request):
    return render(request,'search.html')


def AssignmentSearchView(request):
    return render(request,'job-search.html')


def AssignmentDetailView(request):
    return render(request,'job-single.html')

def get_ip(request):
    if request.META.get('REMOTE_ADDR',None) == '127.0.0.1' or request.META.get('REMOTE_ADDR').startswith('10.'):
        ip='197.232.22.183'
    else:
        ip=request.META.get('REMOTE_ADDR',None)
    return ip

def assignment_upload(request):
	if request.method == 'POST' and request.user.is_authenticated:
		active_support=User.objects.filter(Q(is_superuser=True) & Q(is_active=True)).first()
		form=AssignmentDocumentForm(request.POST, request.FILES)
		if form.is_valid():
			ip=get_ip(request)
			geographical_location=GeoIP2()
			data=geographical_location.city(ip)
			country=data["country_name"]
			form.instance.ip_address=ip
			form.instance.location=country
			form.instance.creator=request.user
			form.instance.support=active_support
			form.save()
			messages.success(request,'Assignment has been successfully uploaded.Thank you')
			return redirect('assignments:assignment_list')
	else:
		form=AssignmentDocumentForm()
	return render(request,'upload.html',{'form':form})


def delete_assignment(request,pk):
    if request.method=='POST':
        assignment=Assignment.objects.get(pk=pk)
        assignment.delete()
    return redirect('assignments:assignment_list')



def assignment_list(request): 
    context ={} 
    context['individual_assignments'] = Assignment.objects.filter(creator=request.user)
    context['all_assignments']=Assignment.objects.all()
    return render(request, "assignment_list.html", context) 
  

@csrf_exempt
def capture(request,order_id,assignment_id):
    assignment=get_object_or_404(Assignment,id=assignment_id)
    if request.method =="POST":
        capture_order = OrdersCaptureRequest(order_id)
        Order.objects.create(
            token=order_id,
            total=assignment.price,
            emailAddress=assignment.creator.email,
            assignment=assignment,
            paid=True,
            client=assignment.creator,
            writer=assignment.writer,
            support=assignment.support
        )
        environment = LiveEnvironment(client_id=settings.PAYPAL_CLIENT_ID, client_secret=settings.PAYPAL_SECRET_ID)
        client = PayPalHttpClient(environment)

        response = client.execute(capture_order)
        data = response.result.__dict__['_dict']

        return JsonResponse(data)
    else:
        return JsonResponse({'details': "invalid request"})


@csrf_exempt
def processing_payment(request,assignment_id):
    assignment=get_object_or_404(Assignment,id=assignment_id)
    if request.method == 'POST':
        environment = LiveEnvironment(client_id=settings.PAYPAL_CLIENT_ID, client_secret=settings.PAYPAL_SECRET_ID)
        client = PayPalHttpClient(environment)
        create_order = OrdersCreateRequest()
        create_order.request_body (
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "USD",
                            "value": assignment.price,
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": assignment.price
                                }
                                },
                            },                               


                    }
                ]
            }
        )

        response = client.execute(create_order)
        data = response.result.__dict__['_dict']
        return JsonResponse(data)






class AssignWriter(UpdateView):
    model=Assignment
    template_name='chat/template.html'
    form_class=AssignWriterForm
    success_message='You have successfully assigned a writer'
    success_url=None


    def get_context_data(self,*args,**kwargs):
        context=super(AssignWriter,self).get_context_data(**kwargs)
        context['assign_writer'] = True
        context['writers']=User.objects.filter(Q(is_staff=True) & Q(is_superuser=False))
        return context

    def form_valid(self,form):
        form=self.get_form()
        assignment=Assignment.objects.get(id=self.kwargs.get('pk'))
        if self.request.POST.get('writers'):
            form.instance.writer=User.objects.get(username=self.request.POST.get('writers'))
        return super(AssignWriter,self).form_valid(form)

    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            assignment_id=self.kwargs.get('pk')
            assignment=get_object_or_404(Assignment,id=assignment_id)
            return reverse_lazy('chat:threads',kwargs={'username':assignment.creator.username,'pk':assignment_id})
        else:
            return None




def upload_assignment(request,pk):
    obj = get_object_or_404(Assignment, pk=pk)
    form = UploadAssignmentForm(request.POST or None,
                        request.FILES or None, instance=obj)
    # getting the done assignment by the writer
    # then posting it back the user
    if request.method == 'POST':
        if form.is_valid():
           form.save()
           return redirect('chat:orders')
           
    
    return render(request, 'chat/template.html', {'form': form})



@login_required
def assignment_mark_return(request, pk):
    """
    marking assignments as returned.
    """
    assignment = get_object_or_404(Assignment, id=pk)
            
    if request.user or request.user.is_superuser and request.method == 'POST':
        if assignment.status == 'COMP' or assignment.status == 'APP':
            assignment.return_reason=request.POST.get('message')
            assignment.status = 'REV'
            assignment.save()
            messages.success(request, "The assignment has been successfully returned for revision!")
            if request.user == assignment.support:
                return redirect(reverse('chat:threads',kwargs={'username':assignment.creator.username,'pk':pk}))
            else:
                return redirect(reverse('chat:threads',kwargs={'username':assignment.support.username,'pk':pk}))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied


@login_required
@require_http_methods(["GET"])
def assignment_mark_completed(request,pk):
    """
    Marking the assignment as completed
    """
    assignment = get_object_or_404(Assignment, id=pk)
    if request.user or request.user.is_staff:
        if assignment.status == 'PEN' or assignment.status == 'REV':
            assignment.status = 'COMP'
            assignment.completed_date=datetime.today()
            assignment.save()
            messages.success(request, "The assignment has been marked as completed successfully!")
            if request.user == assignment.writer:
                return redirect(reverse('chat:orders'))
            else:
                return redirect(reverse('chat:search',kwargs={'username':assignment.support,'pk':pk}))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied


@login_required
@require_http_methods(['GET'])
def assignment_mark_disputed(request,pk):
    assignment=get_object_or_404(Assignment,id=pk)
    if request.user or request.user.is_superuser:
        if assignment.status=='PEN':
            assignment.status='DIS'
            assignment.save()
            messages.success(request,f"the assignment {assignment.description} has been successfully marked as disputed. Thank you")
            if request.user==assignment.support:
                    return redirect(reverse('chat:threads',kwargs={'username':assignment.creator.username,'pk':pk}))
            else:   
                    return redirect(reverse('chat:threads',kwargs={'username':assignment.support.username,'pk':pk}))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied



@login_required
@require_http_methods(['GET'])
def assignment_mark_paid(request,pk):
    assignment=get_object_or_404(Assignment,id=pk)
    if request.user or request.user.is_superuser:
            if assignment.order_set.paid==False:
                assignment.order_set.paid=True
                assignment.status='MP'
                assignment.save()
                messages.success(request,'The assignment has been successfully marked as paid. Thank you')
                return redirect(reverse('chat:threads',kwargs={'username':assignment.creator.username,'pk':pk}))
            else:
                raise PermissionDenied
    else:
        raise PermissionDenied




@login_required
@require_http_methods(["GET"])
def assignment_mark_approved(request,pk):
    """
    Only task creator and assigned users can mark task as Completed.
    """
    assignment = get_object_or_404(Assignment, id=pk)
    if request.user:
        if assignment.status == 'COMP':
            assignment.status = 'APP'
            assignment.save()
            messages.success(request, "The assignment has been marked as approved successfully!")
            assignment_support=assignment.support
            if request.user == assignment.support:
                return redirect(reverse('chat:threads',kwargs={'username':assignment.creator,'pk':pk}))
            else:
                return redirect(reverse('chat:search',kwargs={'username':assignment.support,'pk':pk}))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied


@login_required
@require_http_methods(["GET"])
def assignment_bid(request,pk):
    """
    Only task creator and assigned users can mark task as Completed.
    """
    assignment = get_object_or_404(Assignment, id=pk)
    if request.user:
        if assignment.status == 'BID':
            assignment.status = 'PEN'
            assignment.save()
            messages.success(request, "The assignment has been successfully marked as pending. Thank you")
            return redirect(reverse('chat:orders'))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied


@login_required
@require_http_methods(["GET"])
def assignment_make_public(request,pk):
    """
    Only task creator and assigned users can mark task as Completed.
    """
    assignment = get_object_or_404(Assignment, id=pk)
    if request.user:
        if assignment.status == 'PRIV':
            assignment.status = 'BID'
            assignment.save()
            messages.success(request, "The assignment has been made public successfully. Thank you!")
            return redirect(reverse('chat:orders'))
        else:
            raise PermissionDenied
    else:
        raise PermissionDenied








