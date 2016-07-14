from __future__ import unicode_literals

from django.db import models


class Visit(models.Model):
    ip_address = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True, blank=True)
