from django.urls import path

from open_pdf_hosting_project.apps.account.views import UserLoginView

urlpatterns = [
    path('account', UserLoginView.as_view(), name='account')
]