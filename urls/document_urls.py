from django.conf.urls import url
from ..views import (DocumentListView, DocumentCreateView, DocumentDetailView,
                     DocumentUpdateView, DocumentDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentCreateView.as_view()),
        name="document_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentUpdateView.as_view()),
        name="document_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentDeleteView.as_view()),
        name="document_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentDetailView.as_view(),
        name="document_detail"),

    url(r'^$',
        DocumentListView.as_view(),
        name="document_list"),
]
