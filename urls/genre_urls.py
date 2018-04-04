from django.conf.urls import url
from ..views import (GenreListView, GenreCreateView, GenreDetailView,
                     GenreUpdateView, GenreDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(GenreCreateView.as_view()),
        name="genre_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(GenreUpdateView.as_view()),
        name="genre_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(GenreDeleteView.as_view()),
        name="genre_delete"),

    url(r'^(?P<pk>\d+)/$',
        GenreDetailView.as_view(),
        name="genre_detail"),

    url(r'^$',
        GenreListView.as_view(),
        name="genre_list"),
]
