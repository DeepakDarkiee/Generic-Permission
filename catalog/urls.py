
from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='index' ),
    path('userperm',views.user_gains_perms,name='userperm' ),
    path('group',views.group_gains_perms,name='group' ),
    path('books/',views.BookListView.as_view(),name='books' ),
    path('books_detail/<int:pk>',views.BookDetailView.as_view(),name='books_detail' ),
    path('books_update/<int:pk>',views.BookUpdateView.as_view(),name='books_update' ),
    path('book/<int:pk>/delete/',views.BookDeleteView.as_view(),name='books_delete' ),
    path('books_create/',views.BookCreateView.as_view(),name='books_create' ),
]
