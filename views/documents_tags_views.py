from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DocumentsTags
from ..forms import DocumentsTagsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentsTagsListView(ListView):
    model = DocumentsTags
    template_name = "arosenius-admin-django/documents_tags_list.html"
    paginate_by = 20
    context_object_name = "documents_tags_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentsTagsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsTagsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsTagsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentsTagsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentsTagsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentsTagsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentsTagsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentsTagsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentsTagsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentsTagsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsTagsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsTagsListView, self).get_template_names()


class DocumentsTagsDetailView(DetailView):
    model = DocumentsTags
    template_name = "arosenius-admin-django/documents_tags_detail.html"
    context_object_name = "documents_tags"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentsTagsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsTagsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsTagsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsTagsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsTagsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsTagsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsTagsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsTagsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsTagsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsTagsDetailView, self).get_template_names()


class DocumentsTagsCreateView(CreateView):
    model = DocumentsTags
    form_class = DocumentsTagsForm
    # fields = ['document', 'tag']
    template_name = "arosenius-admin-django/documents_tags_create.html"
    success_url = reverse_lazy("documents_tags_list")

    def __init__(self, **kwargs):
        return super(DocumentsTagsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentsTagsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsTagsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsTagsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentsTagsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsTagsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsTagsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsTagsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsTagsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsTagsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsTagsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsTagsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsTagsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_tags_detail", args=(self.object.pk,))


class DocumentsTagsUpdateView(UpdateView):
    model = DocumentsTags
    form_class = DocumentsTagsForm
    # fields = ['document', 'tag']
    template_name = "arosenius-admin-django/documents_tags_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_tags"

    def __init__(self, **kwargs):
        return super(DocumentsTagsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsTagsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsTagsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsTagsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsTagsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsTagsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsTagsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentsTagsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsTagsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsTagsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsTagsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsTagsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsTagsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsTagsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsTagsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsTagsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsTagsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_tags_detail", args=(self.object.pk,))


class DocumentsTagsDeleteView(DeleteView):
    model = DocumentsTags
    template_name = "arosenius-admin-django/documents_tags_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_tags"

    def __init__(self, **kwargs):
        return super(DocumentsTagsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsTagsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentsTagsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentsTagsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsTagsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsTagsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsTagsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsTagsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsTagsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsTagsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsTagsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_tags_list")
