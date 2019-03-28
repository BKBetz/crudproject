from django.db import models
import datetime

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birth_date = models.DateField(("Date"), default=datetime.date.today)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name_plural = 'Users'
