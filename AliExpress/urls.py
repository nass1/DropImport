from django.conf.urls import url, include
from .views import helloAli
from django.conf import settings
from django.conf.urls.static import static


app_name = 'AliExpress'

urlpatterns = [
    url(r'^$', helloAli,name='index'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)