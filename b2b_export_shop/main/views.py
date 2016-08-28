from django.shortcuts import render
from django.views.generic.list import ListView
from goods.models import Good

# Create your views here.
class MainPageView(ListView):
    model = Good
    template_name = 'index.html'
    paginate_by = 3

    def get_queryset(self):
        #Берем только рекомендованные товары
        goods = Good.objects.filter(featured = True)
        #Берем 3 товара
        goods = goods.order_by('-rating')[0:3]
        return goods
