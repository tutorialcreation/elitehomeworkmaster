
from django.conf import settings
from django.views.generic.base import TemplateView
from django.views.generic import CreateView,ListView,UpdateView
from django.shortcuts import render,redirect # new
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.contrib.auth import login
from django.utils.decorators import method_decorator
# from .forms import ClientSignupForm,WriterSignupForm,AdministrationSignupForm
# from .models import User,Client,Writer,Adminstration
from .decorators import writer_required,client_required,admin_required
from paypal.standard.forms import PayPalPaymentsForm
# from .models import Membership,UserMembership,Subscription
from assignments.models import Assignment
from .forms import QuoteForm

import stripe # new
stripe.api_key = settings.STRIPE_SECRET_KEY # new


# Create your views here.
def PaymentIndexView(request):
    return render(request,'pricing-plan.html')



class HomePageView(TemplateView):
    template_name = 'assignment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request): # new
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return redirect("index")



# def get_invoie(request):
#     if request.method == 'POST':
#         invoice=stripe.Invoice.create(
#             customer=
#         )

# def get_user_membership(request):
#     user_membership_qs=UserMembership.objects.filter(user=request.user)
#     if user_membership_qs.exists():
#         return user_membership_qs.first()
#     return None

# def get_user_subscription(request):
#     user_subscription_qs=Subscription.objects.filter(
#         user_membership=get_user_membership(request)
#     )
#     if user_subscription_qs.exists():
#         user_subscription=user_subscription_qs.first()
#         return user_subscription
#     return None

# def get_selected_membership(request):
#     membership_type=request.session['selected_membership_type']
#     selected_membership_qs=Membership.objects.filter(
#         membership_type=membership_type
#     )
#     if selected_membership_qs.exists():
#         return selected_membership_qs.first()
#     return None



# class MembershipSelectView(ListView):
#     model=Membership

#     def get_context_data(self,*args,**kwargs):
#         context=super().get_context_data(**kwargs)
#         current_membership=get_user_membership(self.request)
#         context['current_membership']=str(current_membership.membership)
#         return context

#     def post(self,request,**kwargs):
#         selected_membership=request.POST.get('membership_type')
#         user_membership=get_user_membership(request)
#         user_subscription=get_user_subscription(request)

#         selected_membership_qs=Membership.objects.filter(
#             membership_type=selected_membership
#         )

#         if selected_membership_qs.exists():
#             selected_membership=selected_membership_qs.first()
        
#         '''
#         ============
#         VALIDATION
#         ============
#         '''
#         if user_membership.membership==selected_membership:
#                if user_subscription != None:
#                    messages.info(request,"You \
#                        already have this membership")
#                    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 

#         request.session['selected_membership_type']=selected_membership.membership_type

#         return HttpResponseRedirect(reverse('payments:payment')) 



# def PaymentView(request):
#     user_membership=get_user_membership(request)
#     selected_membership=get_selected_membership(request)

#     publishKey=settings.STRIPE_PUBLISHABLE_KEY

#     if request.method=='POST':
#         try:
#             token=request.POST.get('stripeToken')
#             # import pdb; pdb.set_trace()
#             cus = stripe.Customer.retrieve(user_membership.stripe_customer_id)
#             cus.source = token
#             cus.save()
#             subscription=stripe.Subscription.create(
#                 customer=user_membership.stripe_customer_id,
#                 items=[
#                     {
#                         "price": selected_membership.stripe_plan_id,
#                     },
#                 ],
#                 # source=token
#             )
#             return redirect(reverse('payments:update-transactions',
#             kwargs={
#                'subscription_id': subscription.id 
#             }))
#         except stripe.error.CardError as e:
#             messages.info(request,"Your card has been declined")


#     context={
#         'publishKey': publishKey,
#         'selected_membership':selected_membership
#     }

#     return render(request,'payments/membership_payments.html',context)



# def updateTransactions(request,subscription_id):
#     user_membership=get_user_membership(request)
#     selected_membership=get_selected_membership(request)

#     user_membership.membership=selected_membership
#     user_membership.save()

#     sub,created=Subscription.objects.get_or_create(user_membership=user_membership)
#     sub.stripe_subscription_id=subscription_id
#     sub.active=True
#     sub.save()

#     try:
#         del request.session['selected_membership_type']
#     except:
#         pass
    

#     messages.info(request,"successfully created {} membership".format(selected_membership))
#     return redirect('/payments')




class IssueQuote(UpdateView):
    model=Assignment
    template_name='chat/template.html'
    form_class=QuoteForm
    success_url=None



    def form_valid(self, form):
        form=self.get_form()
        assignment=Assignment.objects.get(id=self.kwargs.get('pk'))
        # import pdb;pdb.set_trace()
        if self.request.POST.get('price') is not None and assignment.price is not None:
            form.instance.price_delta=abs(int(self.request.POST.get('price'))-int(assignment.price))
        return super(IssueQuote, self).form_valid(form)

    def get_success_url(self, **kwargs):         
        if  kwargs != None:
            assignment_creator=self.request.GET.get('assignment_creator')
            return reverse_lazy('chat:threads', kwargs = {'username':assignment_creator,'pk':self.kwargs.get('pk')})
        else:
            return reverse_lazy('detail', args = (self.object.id,))




def change_quote(request,pk):
    assignment=Assignment.objects.get(id=pk)
    assignment.price=assignment.price_delta
    assignment.save()
    messages.success(request,'You have successfully changed the quote. Thank you.')
    return redirect(reverse('chat:threads', kwargs = {'username':assignment.creator.username,'pk':pk}))

