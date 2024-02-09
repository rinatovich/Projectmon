from django.db import models

# Create your models here.
from core.models.components import LegalEntity


class Organization(LegalEntity):

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"

    def __str__(self):
        return f"{self.name} (Организация)"