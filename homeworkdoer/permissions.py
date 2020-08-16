from django.contrib.auth.models import Permission,Group,User
from django.contrib.contenttypes.models import ContentType
from assignments.models import Assignment
from payments.models import Membership,UserMembership,Subscription
from writers.models import WritersJoin,Document

#################
# set content types 
user_content_type=ContentType.objects.get_for_model(User)
assignment_content_type=ContentType.objects.get_for_model(Assignment)
membership_content_type=ContentType.objects.get_for_model(Membership)
user_membership_content_type=ContentType.objects.get_for_model(UserMembership)
subscription_content_type=ContentType.objects.get_for_model(Subscription)
writers_content_type=ContentType.objects.get_for_model(WritersJoin)
document_content_type=ContentType.objects.get_for_model(Document)
##################
# create permissions

#################
can_view_uploaded_files=Permission.objects.create(
    codename='can_view_uploaded_files',
    name='can view uploaded files',
    content_type=user_content_type
)
can_approve_orders_completed=Permission.objects.create(
    codename='can_approve_orders_completed',
    name='can approve orders completed',
    content_type=user_content_type
)
can_return_order_revision=Permission.objects.create(
    codename='can_return_orders_revision',
    name='can return orders revision',
    content_type=user_content_type
)

can_edit_deadlines=Permission.objects.create(
    codename='can_edit_deadlines',
    name='can edit deadlines',
    content_type=user_content_type
)

can_mark_completed=Permission.objects.create(
    codename='can_mark_completed',
    name='can mark completed',
    content_type=writers_content_type
)

can_request_for_payment=Permission.objects.create(
    codename='can_request_for_payment',
    name='can request for payment',
    content_type=writers_content_type
)

can_view_orders=Permission.objects.create(
    codename='can_view_orders',
    name='can view orders',
    content_type=writers_content_type
)

can_view_payment_details=Permission.objects.create(
    codename='can_view_payment_details',
    name='can view payment details',
    content_type=user_content_type
)


can_assign_orders=Permission.objects.create(
    codename='can_assign_orders',
    name='can assign orders',
    content_type=user_content_type
)

can_issue_quote=Permission.objects.create(
    codename='can_issue_quotes',
    name='can issue quotes',
    content_type=user_content_type
)


# set groups into permissions

##############
# create groups
client_group,created = Group.objects.get_or_create(name='clients_group')
writers_group,created = Group.objects.get_or_create(name='writers_group')
support_group,created = Group.objects.get_or_create(name='support_group')

#################
# assign permissions to groups

client_group.permissions.add(
    can_approve_orders_completed,
    can_return_order_revision
)
writers_group.permissions.add(
    can_request_for_payment,
    can_mark_completed,can_view_orders,
    can_view_payment_details
)
support_group.permissions.add(
    can_assign_orders,can_issue_quote,
    can_return_order_revision,can_approve_orders_completed,
    can_edit_deadlines
)