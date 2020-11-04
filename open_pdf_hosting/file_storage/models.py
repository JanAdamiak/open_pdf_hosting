from django.db import models
from django.utils import timezone
from open_pdf_hosting.account.models import CustomGroups


class FileStorage(models.Model):
    file_name = models.CharField(max_length=80)
    group = models.ForeignKey(CustomGroups, on_delete=models.CASCADE)
    date_created = models.DateField()
    path = models.CharField(max_length=80)


    def __str__(self):
        return self.file_name

    def save(self, *args, **kwargs):
        self.date_created = timezone.now()
        return super().save(*args, **kwargs)