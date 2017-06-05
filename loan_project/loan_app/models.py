from __future__ import unicode_literals

from django.db import models

'''
The Loan information is a simple high level view of the company requesting the Loan (ie its
sector and a synopsis of what it does) and how much they are looking to borrow.
'''


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Loan(models.Model):
    owner = models.ForeignKey('auth.User', related_name='loans', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    company = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    synopsis = models.TextField(blank=True, default='')
    amount = models.IntegerField(blank=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)