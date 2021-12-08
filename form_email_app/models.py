from django.db import models

class ServiceRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True) # This will record the date and time that the form was submitted
