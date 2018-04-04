from django.conf.urls import include, url

urlpatterns = [

    url(r'^documents/', include('arosenius-admin-django.urls.document_urls')),  # NOQA
    url(r'^images/', include('arosenius-admin-django.urls.image_urls')),
    url(r'^places/', include('arosenius-admin-django.urls.place_urls')),
    url(r'^documents_placess/', include('arosenius-admin-django.urls.documents_places_urls')),
    url(r'^documents_imagess/', include('arosenius-admin-django.urls.documents_images_urls')),
    url(r'^documents_genress/', include('arosenius-admin-django.urls.documents_genres_urls')),
    url(r'^imagess/', include('arosenius-admin-django.urls.images_urls')),
    url(r'^tags/', include('arosenius-admin-django.urls.tag_urls')),
    url(r'^documents_personss/', include('arosenius-admin-django.urls.documents_persons_urls')),
    url(r'^documents_tagss/', include('arosenius-admin-django.urls.documents_tags_urls')),
    url(r'^genres/', include('arosenius-admin-django.urls.genre_urls')),
    url(r'^museums/', include('arosenius-admin-django.urls.museum_urls')),
    url(r'^persons/', include('arosenius-admin-django.urls.person_urls')),
]
