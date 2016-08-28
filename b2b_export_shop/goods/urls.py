from django.conf.urls import url
from goods.views import GoodsView, GoodView

urlpatterns = [
    url(r'^$', GoodsView.as_view(), name = 'goods'),
    url(r'(?P<pk>\d+)/detail/$', GoodView.as_view(), name='good'),
]