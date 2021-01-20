from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin

from open_pdf_hosting_project.apps.account.models import CustomGroups
from open_pdf_hosting_project.apps.file_storage.models import FileStorage


class ListAllFiles(PermissionRequiredMixin, ListView):
    queryset = FileStorage
    ordering = '-date_created'
