from django.conf.urls import url
from ..views import (DocumentsPlacesListView, DocumentsPlacesCreateView, DocumentsPlacesDetailView,
                     DocumentsPlacesUpdateView, DocumentsPlacesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentsPlacesCreateView.as_view()),
        name="documents_places_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentsPlacesUpdateView.as_view()),
        name="documents_places_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentsPlacesDeleteView.as_view()),
        name="documents_places_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentsPlacesDetailView.as_view(),
        name="documents_places_detail"),

    url(r'^$',
        DocumentsPlacesListView.as_view(),
        name="documents_places_list"),
]
