from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import DocumentsPersons
from ..forms import DocumentsPersonsForm
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.http import Http404


class DocumentsPersonsListView(ListView):
    model = DocumentsPersons
    template_name = "arosenius-admin-django/documents_persons_list.html"
    paginate_by = 20
    context_object_name = "documents_persons_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(DocumentsPersonsListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPersonsListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPersonsListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(DocumentsPersonsListView, self).get_queryset()

    def get_allow_empty(self):
        return super(DocumentsPersonsListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(DocumentsPersonsListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(DocumentsPersonsListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(DocumentsPersonsListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(DocumentsPersonsListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(DocumentsPersonsListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPersonsListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPersonsListView, self).get_template_names()


class DocumentsPersonsDetailView(DetailView):
    model = DocumentsPersons
    template_name = "arosenius-admin-django/documents_persons_detail.html"
    context_object_name = "documents_persons"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(DocumentsPersonsDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPersonsDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPersonsDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPersonsDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPersonsDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPersonsDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPersonsDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPersonsDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPersonsDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPersonsDetailView, self).get_template_names()


class DocumentsPersonsCreateView(CreateView):
    model = DocumentsPersons
    form_class = DocumentsPersonsForm
    # fields = ['document', 'person']
    template_name = "arosenius-admin-django/documents_persons_create.html"
    success_url = reverse_lazy("documents_persons_list")

    def __init__(self, **kwargs):
        return super(DocumentsPersonsCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(DocumentsPersonsCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPersonsCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsPersonsCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(DocumentsPersonsCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsPersonsCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsPersonsCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsPersonsCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsPersonsCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsPersonsCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPersonsCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPersonsCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPersonsCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_persons_detail", args=(self.object.pk,))


class DocumentsPersonsUpdateView(UpdateView):
    model = DocumentsPersons
    form_class = DocumentsPersonsForm
    # fields = ['document', 'person']
    template_name = "arosenius-admin-django/documents_persons_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_persons"

    def __init__(self, **kwargs):
        return super(DocumentsPersonsUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPersonsUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(DocumentsPersonsUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(DocumentsPersonsUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPersonsUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPersonsUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPersonsUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(DocumentsPersonsUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(DocumentsPersonsUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(DocumentsPersonsUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(DocumentsPersonsUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(DocumentsPersonsUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(DocumentsPersonsUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPersonsUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPersonsUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPersonsUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPersonsUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_persons_detail", args=(self.object.pk,))


class DocumentsPersonsDeleteView(DeleteView):
    model = DocumentsPersons
    template_name = "arosenius-admin-django/documents_persons_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "documents_persons"

    def __init__(self, **kwargs):
        return super(DocumentsPersonsDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(DocumentsPersonsDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(DocumentsPersonsDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(DocumentsPersonsDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(DocumentsPersonsDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(DocumentsPersonsDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(DocumentsPersonsDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(DocumentsPersonsDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(DocumentsPersonsDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(DocumentsPersonsDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(DocumentsPersonsDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("documents_persons_list")
