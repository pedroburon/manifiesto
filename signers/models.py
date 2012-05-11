from django.db import models


class Signer(models.Model):
    country = models.IntegerField()
    message = models.TextField()
    user = models.OneToOneField('auth.User')
    subscribed = models.BooleanField(default=False)
