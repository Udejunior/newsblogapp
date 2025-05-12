from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [


    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('business/', views.business, name='business'),
    path('politics/', views.politics, name='politics'),
    path('entertainment/', views.entertainment, name='entertainment'),
    path('sport/', views.sport, name='sport'),
    path('others/', views.others, name='others'),
]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)