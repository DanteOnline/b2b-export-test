from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from goods.models import Good
from django.http import HttpResponse

# Create your views here.
class GoodsView(ListView):
    model = Good
    template_name = 'goods.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.request.session.get('view', 'grid')
        return super(GoodsView,self).get(request,*args,**kwargs)

    def get_queryset(self):
        goods = Good.objects.all()
        #Сортируем по рейтингу
        goods = goods.order_by('-rating')
        return goods

class GoodView(DetailView):
    model = Good
    template_name = 'good.html'

def change_view(request):
    if request.method == "GET":
        request.session['view'] = request.GET['view']
        return HttpResponse('ok', content_type='text/html')
    else:
        return HttpResponse('no', content_type='text/html')