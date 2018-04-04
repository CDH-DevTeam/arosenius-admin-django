from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Images
from ..forms import ImagesForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class ImagesListView(ListView):
    model = Images
    template_name = "arosenius-admin-django/images_list.html"
    paginate_by = 20
    context_object_name = "images_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(ImagesListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImagesListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImagesListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(ImagesListView, self).get_queryset()

    def get_allow_empty(self):
        return super(ImagesListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(ImagesListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(ImagesListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(ImagesListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(ImagesListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(ImagesListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(ImagesListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImagesListView, self).get_template_names()


class ImagesDetailView(DetailView):
    model = Images
    template_name = "arosenius-admin-django/images_detail.html"
    context_object_name = "images"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(ImagesDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImagesDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImagesDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImagesDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImagesDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(ImagesDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ImagesDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImagesDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImagesDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImagesDetailView, self).get_template_names()


class ImagesCreateView(CreateView):
    model = Images
    form_class = ImagesForm
    # fields = ['file', 'page_number', 'page_side', 'page_ider']
    template_name = "arosenius-admin-django/images_create.html"
    success_url = reverse_lazy("images_list")

    def __init__(self, **kwargs):
        return super(ImagesCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(ImagesCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImagesCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ImagesCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(ImagesCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ImagesCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ImagesCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ImagesCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(ImagesCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ImagesCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ImagesCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(ImagesCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImagesCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("images_detail", args=(self.object.pk,))


class ImagesUpdateView(UpdateView):
    model = Images
    form_class = ImagesForm
    # fields = ['file', 'page_number', 'page_side', 'page_ider']
    template_name = "arosenius-admin-django/images_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "images"

    def __init__(self, **kwargs):
        return super(ImagesUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImagesUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(ImagesUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(ImagesUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImagesUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImagesUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(ImagesUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(ImagesUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(ImagesUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(ImagesUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(ImagesUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(ImagesUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(ImagesUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(ImagesUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImagesUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImagesUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImagesUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("images_detail", args=(self.object.pk,))


class ImagesDeleteView(DeleteView):
    model = Images
    template_name = "arosenius-admin-django/images_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "images"

    def __init__(self, **kwargs):
        return super(ImagesDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(ImagesDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(ImagesDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(ImagesDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(ImagesDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(ImagesDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(ImagesDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(ImagesDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(ImagesDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(ImagesDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(ImagesDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("images_list")
