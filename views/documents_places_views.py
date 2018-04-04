from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DocumentsPlaces
from ..forms import DocumentsPlacesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentsPlacesListView(ListView):
    model = DocumentsPlaces
    template_name = "arosenius-admin-django/documents_places_list.html"
    paginate_by = 20
    context_object_name = "documents_places_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentsPlacesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPlacesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPlacesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentsPlacesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentsPlacesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentsPlacesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentsPlacesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentsPlacesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentsPlacesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentsPlacesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPlacesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPlacesListView, self).get_template_names()


class DocumentsPlacesDetailView(DetailView):
    model = DocumentsPlaces
    template_name = "arosenius-admin-django/documents_places_detail.html"
    context_object_name = "documents_places"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentsPlacesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPlacesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPlacesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPlacesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPlacesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPlacesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPlacesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPlacesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPlacesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPlacesDetailView, self).get_template_names()


class DocumentsPlacesCreateView(CreateView):
    model = DocumentsPlaces
    form_class = DocumentsPlacesForm
    # fields = ['document', 'place']
    template_name = "arosenius-admin-django/documents_places_create.html"
    success_url = reverse_lazy("documents_places_list")

    def __init__(self, **kwargs):
        return super(DocumentsPlacesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentsPlacesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPlacesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsPlacesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentsPlacesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsPlacesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsPlacesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsPlacesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsPlacesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsPlacesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPlacesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPlacesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPlacesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_places_detail", args=(self.object.pk,))


class DocumentsPlacesUpdateView(UpdateView):
    model = DocumentsPlaces
    form_class = DocumentsPlacesForm
    # fields = ['document', 'place']
    template_name = "arosenius-admin-django/documents_places_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_places"

    def __init__(self, **kwargs):
        return super(DocumentsPlacesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPlacesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPlacesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsPlacesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPlacesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPlacesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPlacesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentsPlacesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsPlacesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsPlacesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsPlacesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsPlacesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsPlacesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPlacesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPlacesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPlacesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPlacesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_places_detail", args=(self.object.pk,))


class DocumentsPlacesDeleteView(DeleteView):
    model = DocumentsPlaces
    template_name = "arosenius-admin-django/documents_places_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_places"

    def __init__(self, **kwargs):
        return super(DocumentsPlacesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPlacesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentsPlacesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentsPlacesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPlacesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPlacesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPlacesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPlacesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPlacesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPlacesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPlacesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_places_list")
