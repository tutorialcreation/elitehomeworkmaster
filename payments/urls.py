from django.urls import path
from .views import  (
    PaymentIndexView,
    charge,
    # MembershipSelectView,
    # PaymentView,
    # updateTransactions,
    IssueQuote,
    change_quote
)

# from . import views

app_name='payments'

urlpatterns = [
    # path('', MembershipSelectView.as_view(), name='select'),
    # path('payment_script/', PaymentView, name='payment'),
    path('charge/', charge, name='charge'), # new
    # path('update-transactions/<subscription_id>/',updateTransactions,name='update-transactions'),
    path('issue_quote/<int:pk>/',IssueQuote.as_view(),name='issue_quote'),
    path('change_quote/<int:pk>/',change_quote,name='change_quote'),
]
