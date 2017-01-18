from django.conf.urls import url, include
from .views import helloAli, GetAli, postAli
from django.conf import settings
from django.conf.urls.static import static


app_name = 'AliExpress'

urlpatterns = [
    url(r'^$', GetAli,name='index'),
    url(r'^postShopify/$', postAli, name="postToShopifyAli"),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)