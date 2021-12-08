from django.urls import path

from . import views

app_namespace = 'form_email'

urlpatterns = [
    path('', views.ServiceRequestView.as_view(), name='service_request_view'),
]
