from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from goods.models import Good

# Create your views here.
class GoodsView(ListView):
    model = Good
    template_name = 'goods.html'
    paginate_by = 10

    def get_queryset(self):
        goods = Good.objects.all()
        #Сортируем по рейтингу
        goods = goods.order_by('-rating')
        return goods

class GoodView(DetailView):
    model = Good
    template_name = 'good.html'