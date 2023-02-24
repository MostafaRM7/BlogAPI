from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView

from blog.models import Article


# Create your views here.

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'

    def get_queryset(self):
        return Article.objects.filter(status=True)


class ArticleDetailView(DetailView):
    def get_object(self, **kwargs):
        return get_object_or_404(Article.objects.filter(status=True), pk=self.kwargs['pk'])


class AccountActivationView(DetailView):
    def get(self, request):
        return render(request, 'active_confirm.html')
