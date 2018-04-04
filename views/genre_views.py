from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Genre
from ..forms import GenreForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class GenreListView(ListView):
    model = Genre
    template_name = "arosenius-admin-django/genre_list.html"
    paginate_by = 20
    context_object_name = "genre_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(GenreListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GenreListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GenreListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(GenreListView, self).get_queryset()

    def get_allow_empty(self):
        return super(GenreListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(GenreListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(GenreListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(GenreListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(GenreListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(GenreListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(GenreListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GenreListView, self).get_template_names()


class GenreDetailView(DetailView):
    model = Genre
    template_name = "arosenius-admin-django/genre_detail.html"
    context_object_name = "genre"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(GenreDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GenreDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GenreDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GenreDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(GenreDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(GenreDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GenreDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GenreDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GenreDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GenreDetailView, self).get_template_names()


class GenreCreateView(CreateView):
    model = Genre
    form_class = GenreForm
    # fields = ['name']
    template_name = "arosenius-admin-django/genre_create.html"
    success_url = reverse_lazy("genre_list")

    def __init__(self, **kwargs):
        return super(GenreCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(GenreCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GenreCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GenreCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(GenreCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GenreCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GenreCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GenreCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(GenreCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GenreCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GenreCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(GenreCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GenreCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("genre_detail", args=(self.object.pk,))


class GenreUpdateView(UpdateView):
    model = Genre
    form_class = GenreForm
    # fields = ['name']
    template_name = "arosenius-admin-django/genre_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "genre"

    def __init__(self, **kwargs):
        return super(GenreUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GenreUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(GenreUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(GenreUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GenreUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(GenreUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(GenreUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(GenreUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(GenreUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(GenreUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(GenreUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(GenreUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(GenreUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(GenreUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GenreUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GenreUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GenreUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("genre_detail", args=(self.object.pk,))


class GenreDeleteView(DeleteView):
    model = Genre
    template_name = "arosenius-admin-django/genre_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "genre"

    def __init__(self, **kwargs):
        return super(GenreDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(GenreDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(GenreDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(GenreDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(GenreDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(GenreDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(GenreDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(GenreDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(GenreDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(GenreDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(GenreDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("genre_list")
