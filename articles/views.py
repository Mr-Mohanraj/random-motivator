from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView  # new
from django.urls import reverse_lazy  # new
from .models import Article
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new\
from django.contrib.auth.mixins import LoginRequiredMixin  # new
from django.core.exceptions import PermissionDenied  # new


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'articles/article_new.html'
    fields = ('title', 'body')  # new
    login_url = 'login'

    def form_valid(self, form):  # new
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDetailView(DetailView):  # new
    model = Article
    template_name = 'articles/article_detail.html'

# class ArticleUpdateView(UpdateView): # new
#     model = Article
#     fields = ('title', 'body',)
#     template_name = 'articles/article_edit.html'
# class ArticleDeleteView(DeleteView): # new
#     model = Article
#     template_name = 'articles/article_delete.html'
#     success_url = reverse_lazy('article_list')
