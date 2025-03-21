from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from blog.models import Article

class ArticleListView(ListView):
    model = Article
    paginate_by = 100

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
class ArticleDetailView(DetailView):
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
class ArticleCreateView(CreateView):
    model = Article
    fields = ["titre", "contenu", "date_publication", "auteur", "image"]

class ArticleUpdateView(UpdateView):
    model = Article
    fields = ["titre", "contenu", "date_publication", "auteur", "image"]
    template_name_suffix = "_update_form"

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("article_list")
    template_name_suffix = "_check_delete"



