"""booksharing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from accounts.views import MyProfileView
from books import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('django.contrib.auth.urls')),

    path('', views.Index.as_view(), name='index'),
    path('book/list/', views.BookList.as_view(), name='book-list'),
    path('book/author/list/', views.AuthorList.as_view(), name='author-list'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('book/update/<int:pk>/', views.BookUpdate.as_view(), name='book-update'),
    path('book/delete/<int:pk>/', views.BookDelete.as_view(), name='book-delete'),
    path('book/author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('book/author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),

    path('accounts/my-profile/<int:pk>/', MyProfileView.as_view(), name='my-profile'),


]
