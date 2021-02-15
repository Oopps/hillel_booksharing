from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [

    path('list/', views.BookList.as_view(), name='book-list'),
    path('author/list/', views.AuthorList.as_view(), name='author-list'),
    path('create/', views.BookCreate.as_view(), name='book-create'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='book-update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='book-delete'),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),

]
