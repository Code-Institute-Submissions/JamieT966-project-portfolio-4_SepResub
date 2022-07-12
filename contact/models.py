from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=600)

    def __str__(self):
        return self.message