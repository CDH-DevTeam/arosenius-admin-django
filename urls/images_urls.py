from django.conf.urls import url
from ..views import (ImagesListView, ImagesCreateView, ImagesDetailView,
                     ImagesUpdateView, ImagesDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ImagesCreateView.as_view()),
        name="images_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ImagesUpdateView.as_view()),
        name="images_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ImagesDeleteView.as_view()),
        name="images_delete"),

    url(r'^(?P<pk>\d+)/$',
        ImagesDetailView.as_view(),
        name="images_detail"),

    url(r'^$',
        ImagesListView.as_view(),
        name="images_list"),
]
