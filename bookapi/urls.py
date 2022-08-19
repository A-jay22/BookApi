from django.contrib import admin
from django.urls import path
#from .views import book_list, book_create, book
from .views import BookList, BookCreate,  BookDetails

urlpatterns = [
    #path('', book_create),
    #path('<int:pk>', book),
    #path('list/', book_list)
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetails.as_view())
]
