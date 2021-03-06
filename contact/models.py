from django.db import models

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(max_length=255)

    def __str__(self):
        return self.first_name
    