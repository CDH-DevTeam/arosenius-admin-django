from django.conf.urls import url
from ..views import (DocumentsGenresListView, DocumentsGenresCreateView, DocumentsGenresDetailView,
                     DocumentsGenresUpdateView, DocumentsGenresDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentsGenresCreateView.as_view()),
        name="documents_genres_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentsGenresUpdateView.as_view()),
        name="documents_genres_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentsGenresDeleteView.as_view()),
        name="documents_genres_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentsGenresDetailView.as_view(),
        name="documents_genres_detail"),

    url(r'^$',
        DocumentsGenresListView.as_view(),
        name="documents_genres_list"),
]
