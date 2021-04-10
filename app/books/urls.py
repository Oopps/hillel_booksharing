from django.urls import path

from books import views


urlpatterns = [

    path('list/', views.BookList.as_view(), name='book-list'),
    path('author/list/', views.AuthorList.as_view(), name='author-list'),
    path('create/', views.BookCreate.as_view(), name='book-create'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('update/<int:pk>/', views.BookUpdate.as_view(), name='book-update'),
    path('delete/<int:pk>/', views.BookDelete.as_view(), name='book-delete'),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name='author-delete'),
    path('list/download/xlsx', views.export_books_to_xlsx, name='download-xlsx'),
    path('list/my-books/', views.MyBookList.as_view(), name='my-book-list'),
    path('list/my-requested-books/', views.MyRequestedBooks.as_view(), name='my-requested-books'),
    path('list/requested-books/', views.RequestedBooks.as_view(), name='requested-books'),
    path('req-books/confirm/<int:request_id>/', views.RequestBookConfirm.as_view(), name='req-books-confirm'),
    path('req-books/reject/<int:request_id>/', views.RequestBookReject.as_view(), name='req-books-reject'),
    path('create/book/request/<int:book_id>/', views.RequestBookCreate.as_view(), name='create-book-request'),
    path('req-books/sent-via-email/<int:request_id>/', views.RequestBookSentViaEmail.as_view(), name='sent-via-email'),
    path('req-books/book-received/<int:request_id>/', views.RequestBookReceivedBook.as_view(), name='book-received'),
    path('req-books/book-return/<int:request_id>/', views.RequestBookReturn.as_view(), name='book-return'),
    path('req-books/owner-received/<int:request_id>/', views.RequestBookOwnerReceived.as_view(), name='owner-received'),

]
