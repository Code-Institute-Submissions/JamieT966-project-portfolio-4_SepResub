from django.db import models


class ContactForm(models.Model):
    """
    Model for contact form containing four fields.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField(max_length=600)

    def __str__(self):
        """
        Message to appear in contact section of admin.
        """
        return self.message
