import stripe
import json
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import FormMixin

from django.views.generic import DetailView, ListView,CreateView
from django.views.generic import TemplateView

from assignments.models import Assignment
from authentication.models import User,Notification
# from payments.models import UserMembership,Membership
from .forms import ComposeForm,ReviewForm
from .models import Thread, ChatMessage,Review
from django.db.models import Q

stripe.api_key=settings.STRIPE_SECRET_KEY # new


class IndexView(TemplateView):
    template_name = "search.html"


class ClientView(TemplateView):
    template_name = "chat/clients.html"
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)


class WriterView(LoginRequiredMixin, ListView):
    template_name = "chat/writers.html"
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)




class InboxView(LoginRequiredMixin, ListView):
    template_name = 'chat/inbox.html'
    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)


class ThreadView(SuccessMessageMixin, LoginRequiredMixin, FormMixin, DetailView):
    template_name = 'chat/thread.html'
    form_class = ComposeForm
    success_url = None



    def get_queryset(self):
        return Thread.objects.by_user(self.request.user)

    def get_object(self):
        other_username  = self.kwargs.get("username")
        assignment_id=self.kwargs.get('pk')
        assignment=Assignment.objects.get(id=assignment_id)
        obj, created    = Thread.objects.get_or_new(self.request.user,other_username)
        if self.request.GET.get('read'):
            ChatMessage.objects.create(user=self.request.user, thread=obj, assignment=assignment,viewed=True)
        if obj == None:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super(ThreadView,self).get_context_data(**kwargs)
        assignment_id=self.kwargs.get('pk')
        context['form'] = self.get_form()
        assignment=get_object_or_404(Assignment,id=assignment_id)
        context['assignment'] = assignment
        context['individual_assignments'] = Assignment.objects.filter(Q(creator=assignment.creator) or Q(writer=assignment.writer))
        
        context['client_id'] = settings.PAYPAL_CLIENT_ID
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        assignment=Assignment.objects.get(id=self.kwargs.get('pk'))
        if self.request.POST.get('viewed'):
            assignment.viewed=self.request.POST.get('viewed')
            assignment.save()
        # print(self.request.POST.get('viewed'))
        
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        thread = self.get_object()
        user = self.request.user
        assignment=Assignment.objects.get(id=self.kwargs.get('pk'))
        message = form.cleaned_data.get("message")
        ChatMessage.objects.create(user=user, thread=thread, message=message,assignment=assignment)
        messages.add_message(self.request, messages.SUCCESS, 'You are successfully chatting.')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):         
       return '{}'.format(reverse('chat:threads', kwargs={'username': self.kwargs.get('username'),'pk':self.kwargs.get('pk')}))



def index(request):
    return render(request, 'chat/base.html', {})


@login_required
def room(request,room_name={'room_name':'support'}):
    # add the dictionary during initialization
    assignment_list = Assignment.objects.all()
    if request.user.is_authenticated:
        notifications=Notification.objects.filter(user=request.user,viewed=False)
    if request.method == 'POST':
        quote=request.POST.get('quote')
        get_membership=Membership.objects.all().first()
        Membership.objects.create(slug=get_membership.slug,
            membership_type=get_membership.membership_type,price=quote,
            stripe_plan_id=get_membership.stripe_plan_id
        )



    return render(request,'chat/clients.html',{
        'room_name_json':mark_safe(json.dumps(room_name)),
        'username':mark_safe(json.dumps(request.user.username)),
       
    })



def orders(request):
    context={}
    context['assignments'] = Assignment.objects.all().order_by('-uploaded_at')
    if request.user.is_superuser:
        unassigned_orders=Assignment.objects.filter(status='PRIV').order_by('-uploaded_at')
        public_orders=Assignment.objects.filter(status='BID').order_by('-uploaded_at')
        pending_orders=Assignment.objects.filter(status='PEN').order_by('-uploaded_at')
        completed_orders=Assignment.objects.filter(status='COMP').order_by('-uploaded_at')
        returned_orders=Assignment.objects.filter(status='REV').order_by('-uploaded_at')
        approved_orders=Assignment.objects.filter(status='APP').order_by('-uploaded_at')
        context['unaccepted_orders']=[*unassigned_orders,*public_orders]
        context['pending_orders']=[*pending_orders,*returned_orders]
        context['completed_orders']=[*completed_orders,*approved_orders]
        return render(request,'chat/writers_orders.html',context)
    elif request.user.is_staff:
        unassigned_orders=Assignment.objects.filter(Q(status='PRIV') & Q(writer=request.user)).order_by('-uploaded_at')
        public_orders=Assignment.objects.filter(Q(status='BID') & Q(writer=request.user)).order_by('-uploaded_at')
        pending_orders=Assignment.objects.filter(Q(status='PEN') & Q(writer=request.user)).order_by('-uploaded_at')
        completed_orders=Assignment.objects.filter(Q(status='COMP') & Q(writer=request.user)).order_by('-uploaded_at')
        returned_orders=Assignment.objects.filter(Q(status='REV') & Q(writer=request.user)).order_by('-uploaded_at')
        approved_orders=Assignment.objects.filter(Q(status='APP') & Q(writer=request.user)).order_by('-uploaded_at')
        context['unaccepted_orders']=public_orders
        context['pending_orders']=[*pending_orders,*returned_orders]
        context['completed_orders']=[*completed_orders,*approved_orders]
        return render(request,'chat/writers_orders.html',context)



def reviews(request):
    reviews=Review.objects.all()
    if request.method == 'POST':
        form=ReviewForm(request.POST or None)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully added a review.')
            context={
                'form':form,
                'reviews':reviews
            }
            return render(request,'chat/reviews.html',context)
    else:

        form=ReviewForm()
        context={
            'form':form,
            'reviews':reviews
        }
        return render(request,'chat/reviews.html',context)


def search_assignment(request,pk,username):
    context={}
    # import pdb;pdb.set_trace()
    assignment = Assignment.objects.get(pk=pk)
    context['assignment'] = assignment
    context['data_key'] = settings.STRIPE_PUBLISHABLE_KEY
    host=request.get_host()

    other_username = assignment.support.username

    objects,created = Thread.objects.get_or_new(request.user, other_username)
    if objects is not None:
        obj=objects
    if request.method == 'POST':
        chat_form = ComposeForm(request.POST)


        if chat_form.is_valid():
            message=chat_form.cleaned_data['message']
            thread= obj
            instance=ChatMessage(user=request.user, thread=thread, message=message)
            instance.save() # you named this named_form, not form.
        else:
            context["chat_form"] = chat_form
    else:

        dataset = Assignment.objects.all().first()
        
        
        if request.user.is_authenticated:
            context['notifications']=Notification.objects.filter(user=request.user,viewed=False)
    context['messageset'] = objects
    context['client_id'] = settings.PAYPAL_CLIENT_ID
    # import pdb;pdb.set_trace()
    return render(request, 'assignment_detail.html',context)