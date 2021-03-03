from django.urls import path
from .views import (lead_list, lead_detail, lead_create,lead_update,lead_delete,
                    LeadListView, DetailListView,CreateLeadView,UpdateLeadView,DeleteLeadView)

app_name = "leads"

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    path('<int:pk>/', DetailListView.as_view(), name='lead-detail'),
    path('<int:pk>/update', UpdateLeadView.as_view(),name='lead-update'),
    path('<int:pk>/delete', DeleteLeadView.as_view(),name='lead-delete'),
    path('create/', CreateLeadView.as_view(),name='lead-create'),
]