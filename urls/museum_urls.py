from django.conf.urls import url
from ..views import (MuseumListView, MuseumCreateView, MuseumDetailView,
                     MuseumUpdateView, MuseumDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(MuseumCreateView.as_view()),
        name="museum_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(MuseumUpdateView.as_view()),
        name="museum_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(MuseumDeleteView.as_view()),
        name="museum_delete"),

    url(r'^(?P<pk>\d+)/$',
        MuseumDetailView.as_view(),
        name="museum_detail"),

    url(r'^$',
        MuseumListView.as_view(),
        name="museum_list"),
]
