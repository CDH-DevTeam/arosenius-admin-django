from django.conf.urls import url
from ..views import (DocumentsPersonsListView, DocumentsPersonsCreateView, DocumentsPersonsDetailView,
                     DocumentsPersonsUpdateView, DocumentsPersonsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentsPersonsCreateView.as_view()),
        name="documents_persons_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentsPersonsUpdateView.as_view()),
        name="documents_persons_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentsPersonsDeleteView.as_view()),
        name="documents_persons_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentsPersonsDetailView.as_view(),
        name="documents_persons_detail"),

    url(r'^$',
        DocumentsPersonsListView.as_view(),
        name="documents_persons_list"),
]
