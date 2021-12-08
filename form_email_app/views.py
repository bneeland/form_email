from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.mail import send_mail

from . import models

class ServiceRequestView(CreateView):
    model = models.ServiceRequest
    fields = [
        'name',
        'email',
        'date',
        'time',
    ]
    template_name = 'form_email_app/service_request_view.html'
    success_url = reverse_lazy('form_email_app:service_request_view')

    def form_valid(self, form):
        data = form.cleaned_data
        name = data['name']
        email = data['email']
        date = data['date']
        time = data['time']

        # send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=None)
        send_mail(
            subject='Service request',
            message=f'New service request:\n\nName: {name}\nDate: {date}\nTime: {time}',
            from_email=email,
            recipient_list=['brian.neeland@gmail.com'],
            fail_silently=False,
        )

        self.object = form.save()
        return super().form_valid(form)
