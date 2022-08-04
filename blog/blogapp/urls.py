from django.urls import path
from blogapp import views


app_name = 'blogapp'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('create/', views.create_post, name='create-post'),
    path('tags/', views.tags, name='create-tag'),
    path('category/', views.tags, name='create-category'),
    path('post/<int:id>/', views.post, name='post'),
]

