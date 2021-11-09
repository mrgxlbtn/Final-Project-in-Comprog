from django.db import models


class Complaint(models.Model):
    name = models.CharField('Name', max_length=50)
    email = models.EmailField('E-mail', max_length=100)
    address = models.CharField('Address', max_length=150)
    subject = models.CharField('Subject of the Complaint', max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.subject