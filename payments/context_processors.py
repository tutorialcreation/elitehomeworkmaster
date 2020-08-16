from payments.models import Order

def get_membership_quote(request):
    membership_quote=Order.objects.all().first()
    return dict(membership_quote=membership_quote)
