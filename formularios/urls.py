from django.urls import path
from . import views

urlpatterns = [
    path('asociados/', views.asociados, name="asociados"),
    path('colaborador/', views.colaborador, name="colaborador"),
    path('dirigente/', views.dirigente, name="dirigente"),
    path('gracias/', views.gracias, name="gracias")
]
