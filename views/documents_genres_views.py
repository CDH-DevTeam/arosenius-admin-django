from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DocumentsGenres
from ..forms import DocumentsGenresForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentsGenresListView(ListView):
    model = DocumentsGenres
    template_name = "arosenius-admin-django/documents_genres_list.html"
    paginate_by = 20
    context_object_name = "documents_genres_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentsGenresListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsGenresListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsGenresListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentsGenresListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentsGenresListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentsGenresListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentsGenresListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentsGenresListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentsGenresListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentsGenresListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsGenresListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsGenresListView, self).get_template_names()


class DocumentsGenresDetailView(DetailView):
    model = DocumentsGenres
    template_name = "arosenius-admin-django/documents_genres_detail.html"
    context_object_name = "documents_genres"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentsGenresDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsGenresDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsGenresDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsGenresDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsGenresDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsGenresDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsGenresDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsGenresDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsGenresDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsGenresDetailView, self).get_template_names()


class DocumentsGenresCreateView(CreateView):
    model = DocumentsGenres
    form_class = DocumentsGenresForm
    # fields = ['document', 'genre']
    template_name = "arosenius-admin-django/documents_genres_create.html"
    success_url = reverse_lazy("documents_genres_list")

    def __init__(self, **kwargs):
        return super(DocumentsGenresCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentsGenresCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsGenresCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsGenresCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentsGenresCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsGenresCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsGenresCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsGenresCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsGenresCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsGenresCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsGenresCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsGenresCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsGenresCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_genres_detail", args=(self.object.pk,))


class DocumentsGenresUpdateView(UpdateView):
    model = DocumentsGenres
    form_class = DocumentsGenresForm
    # fields = ['document', 'genre']
    template_name = "arosenius-admin-django/documents_genres_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_genres"

    def __init__(self, **kwargs):
        return super(DocumentsGenresUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsGenresUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsGenresUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsGenresUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsGenresUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsGenresUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsGenresUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentsGenresUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsGenresUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsGenresUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsGenresUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsGenresUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsGenresUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsGenresUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsGenresUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsGenresUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsGenresUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_genres_detail", args=(self.object.pk,))


class DocumentsGenresDeleteView(DeleteView):
    model = DocumentsGenres
    template_name = "arosenius-admin-django/documents_genres_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_genres"

    def __init__(self, **kwargs):
        return super(DocumentsGenresDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsGenresDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentsGenresDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentsGenresDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsGenresDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsGenresDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsGenresDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsGenresDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsGenresDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsGenresDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsGenresDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_genres_list")
