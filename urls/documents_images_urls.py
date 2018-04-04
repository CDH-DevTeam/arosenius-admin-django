from django.conf.urls import url
from ..views import (DocumentsImagesListView, DocumentsImagesCreateView, DocumentsImagesDetailView,
                     DocumentsImagesUpdateView, DocumentsImagesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DocumentsImagesCreateView.as_view()),
        name="documents_images_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DocumentsImagesUpdateView.as_view()),
        name="documents_images_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DocumentsImagesDeleteView.as_view()),
        name="documents_images_delete"),

    url(r'^(?P<pk>\d+)/$',
        DocumentsImagesDetailView.as_view(),
        name="documents_images_detail"),

    url(r'^$',
        DocumentsImagesListView.as_view(),
        name="documents_images_list"),
]
