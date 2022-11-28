from django.urls import path

from articles import views


urlpatterns = [
    path('', views.main_page, name='main'),
    path('<int:article_id>', views.article_page, name='article'),
]