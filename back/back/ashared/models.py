from django.db import models
from django_tenants.models import DomainMixin

from tenant_users.tenants.models import TenantBase


class Client(TenantBase):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Domain(DomainMixin):
    """This class is required for django_tenants."""


