from django.conf.urls import url
from contacts.views import contactView

urlpatterns = [
    url(r'^$', contactView, name = 'contacts'),
]