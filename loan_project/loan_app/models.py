from __future__ import unicode_literals

from django.db import models

'''
The Loan information is a simple high level view of the company requesting the Loan (ie its
sector and a synopsis of what it does) and how much they are looking to borrow.
'''


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