from django.conf.urls import url
from ..views import (DocumentsTagsListView, DocumentsTagsCreateView, DocumentsTagsDetailView,
                     DocumentsTagsUpdateView, DocumentsTagsDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentsTagsCreateView.as_view()),
        name="documents_tags_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentsTagsUpdateView.as_view()),
        name="documents_tags_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentsTagsDeleteView.as_view()),
        name="documents_tags_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentsTagsDetailView.as_view(),
        name="documents_tags_detail"),

    url(r'^$',
        DocumentsTagsListView.as_view(),
        name="documents_tags_list"),
]
