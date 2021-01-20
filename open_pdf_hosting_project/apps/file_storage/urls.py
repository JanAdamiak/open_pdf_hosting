from django.urls import path

from open_pdf_hosting_project.apps.file_storage.views import ListAllFiles

urlpatterns = [
    path('', ListAllFiles.as_view(), name='testing')
]