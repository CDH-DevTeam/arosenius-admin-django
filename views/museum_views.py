from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Museum
from ..forms import MuseumForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class MuseumListView(ListView):
    model = Museum
    template_name = "arosenius-admin-django/museum_list.html"
    paginate_by = 20
    context_object_name = "museum_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(MuseumListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MuseumListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MuseumListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(MuseumListView, self).get_queryset()

    def get_allow_empty(self):
        return super(MuseumListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(MuseumListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(MuseumListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(MuseumListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(MuseumListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(MuseumListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(MuseumListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MuseumListView, self).get_template_names()


class MuseumDetailView(DetailView):
    model = Museum
    template_name = "arosenius-admin-django/museum_detail.html"
    context_object_name = "museum"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(MuseumDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MuseumDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MuseumDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MuseumDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(MuseumDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(MuseumDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MuseumDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MuseumDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MuseumDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MuseumDetailView, self).get_template_names()


class MuseumCreateView(CreateView):
    model = Museum
    form_class = MuseumForm
    # fields = ['name']
    template_name = "arosenius-admin-django/museum_create.html"
    success_url = reverse_lazy("museum_list")

    def __init__(self, **kwargs):
        return super(MuseumCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(MuseumCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MuseumCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MuseumCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(MuseumCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MuseumCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MuseumCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MuseumCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(MuseumCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MuseumCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MuseumCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(MuseumCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MuseumCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("museum_detail", args=(self.object.pk,))


class MuseumUpdateView(UpdateView):
    model = Museum
    form_class = MuseumForm
    # fields = ['name']
    template_name = "arosenius-admin-django/museum_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "museum"

    def __init__(self, **kwargs):
        return super(MuseumUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MuseumUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(MuseumUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(MuseumUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MuseumUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(MuseumUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(MuseumUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(MuseumUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(MuseumUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(MuseumUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(MuseumUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(MuseumUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(MuseumUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(MuseumUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MuseumUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MuseumUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MuseumUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("museum_detail", args=(self.object.pk,))


class MuseumDeleteView(DeleteView):
    model = Museum
    template_name = "arosenius-admin-django/museum_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "museum"

    def __init__(self, **kwargs):
        return super(MuseumDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(MuseumDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(MuseumDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(MuseumDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(MuseumDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(MuseumDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(MuseumDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(MuseumDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(MuseumDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(MuseumDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(MuseumDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("museum_list")
