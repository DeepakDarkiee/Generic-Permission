from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import Book
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import Permission, User,Group
from django.contrib.contenttypes.models import ContentType
# -----------------------------------------------------------------------------------------------------
# ----------------------------------------book section-------------------------------------------
# Create your views here.
def user_gains_perms(request):
    user=User.objects.get(username='pragya')
    content_type = ContentType.objects.get_for_model(Book,for_concrete_model=False)
    book_permissions = Permission.objects.filter(content_type=content_type)
    # print(book_permissions)
    for permission in book_permissions:
        # print(permission.codename)
        if permission.codename == 'delete_book':
            user.group_permissions.add(permission)
        
    return HttpResponse("done")

def group_gains_perms(request):
    # groups = Group.objects.create(name="Supervisory")
    group = Group.objects.get(name="Manager")
    user=User.objects.get(username='rashi')
    user.groups.add(group)
    content_type = ContentType.objects.get_for_model(Book,for_concrete_model=False)
    # permission = Permission.objects.create(codename='add_book',name='Can add book',   content_type=content_type)
    group_book_permissions = Permission.objects.filter(content_type=content_type)
    for permission in group_book_permissions:
        # print(permission.codename)
        if permission.codename == 'add_book':
            group.permissions.add(permission)

    return HttpResponse("done Group")

class IndexView(TemplateView):
    template_name = "home.html"


class BookListView(generic.ListView):
    model = Book
    template_name = "index.html"
    context_object_name= "book_list"


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "detail.html"
    context_object_name= "book_detail"

class BookCreateView(generic.CreateView):
    model = Book
    template_name = "createbook.html"
    fields = ('book_name', 'book_author','book_id' )
    success_url = reverse_lazy('books')

    
class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = "updatebook.html"
    context_object_name= "updatebook.html"
    fields = ('book_name', 'book_author','book_id' )

    success_url = reverse_lazy('books')

class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'deletebook.html'
    success_url = reverse_lazy('books')

# ---------------------------------section end---------------------------------------