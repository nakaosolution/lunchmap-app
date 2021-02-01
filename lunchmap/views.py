from django.urls import reverse_lazy
from django.views import generic
from .models import Category, Shop

# クラスベース
class IndexView(generic.ListView):
    model = Shop

class DetailView(generic.DetailView):
    model = Shop