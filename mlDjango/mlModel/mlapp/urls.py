from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('output/<str:result>', views.output, name='output'),
    path('output', views.aboutus, name='output'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('predict_covid', views.predict_covid, name='predict_covid'),
]