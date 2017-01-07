from django.conf.urls import url, include
from .views import hello, supp, PostToShpify
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ChinaVasion'

urlpatterns = [
    url(r'^$', hello,name='index'),
    url(r'^supp/$', supp, name="supp"),
    url(r'^postprod/$', PostToShpify, name="postToShopify"),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)