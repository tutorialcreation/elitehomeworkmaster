from django.urls import path,re_path
from .views import (
    AssignmentCategoryView,
    AssignmentSearchView,
    AssignmentDetailView,
    assignment_upload,
    delete_assignment,
    assignment_list,
    AssignWriter,
    assignment_mark_return,
    assignment_mark_completed,
    assignment_mark_approved,
    assignment_bid,
    assignment_make_public,
    upload_assignment,
    processing_payment,
    assignment_mark_disputed,
    assignment_mark_paid,
    capture
    
)

app_name='assignments'

urlpatterns = [
    path('list/',assignment_list,name='assignment_list'),
    path('detail/',AssignmentDetailView,name='detail'),
    path('upload/',assignment_upload,name='upload'),
    path('delete/<int:pk>/',delete_assignment,name='delete_assignment'),
    path('list/',assignment_list,name='assignment_list'),
    path('assign_writer/<int:pk>/',AssignWriter.as_view(),name='assign_writer'),
    path('upload_assignment/<int:pk>/',upload_assignment,name='upload_assignment'),
    path('return_assignment/<int:pk>/',assignment_mark_return,name='return'),
    path('mark_completed/<int:pk>/',assignment_mark_completed,name='completed'),
    path('mark_approved/<int:pk>/',assignment_mark_approved,name='approved'),
    path('mark_disputed/<int:pk>/',assignment_mark_disputed,name='disputed'),
    path('mark_paid/<int:pk>/',assignment_mark_paid,name='mark_paid'),
    path('assignment_bid/<int:pk>/',assignment_bid,name='bid'),
    path('assignment_make_public/<int:pk>/',assignment_make_public,name='make_public'),
    path('capture/<str:order_id>/<int:assignment_id>/',capture,name='capture'),
    path('processing/payment/<int:assignment_id>/',processing_payment,name='processing_payment'),
]
