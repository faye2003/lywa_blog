from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from blog.views import ArticleListView
from blog.views import ArticleDetailView
from blog.views import ArticleCreateView
from blog.views import ArticleUpdateView
from blog.views import ArticleDeleteView

from . import views

urlpatterns = [
    path("", ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
    path("create/", ArticleCreateView.as_view(), name="article_form"),
    path("update/<int:pk>/", ArticleUpdateView.as_view(), name="article_update_form"),
    path("delete/<int:pk>/", ArticleDeleteView.as_view(), name="article_check_delete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)