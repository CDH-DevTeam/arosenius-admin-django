from django.conf.urls import url
from ..views import (ImageListView, ImageCreateView, ImageDetailView,
                     ImageUpdateView, ImageDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(ImageCreateView.as_view()),
        name="image_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(ImageUpdateView.as_view()),
        name="image_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(ImageDeleteView.as_view()),
        name="image_delete"),

    url(r'^(?P<pk>\d+)/$',
        ImageDetailView.as_view(),
        name="image_detail"),

    url(r'^$',
        ImageListView.as_view(),
        name="image_list"),
]
