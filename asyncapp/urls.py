from django.urls import path
from .views import timer_view, async_view, sync_view, home_view

urlpatterns = [
    path('timer/', timer_view, name='timer-view'),  # Rota para o contador de tempo
    path('api/', async_view, name='async_view'),    # Rota para a view assíncrona
    path('sync/', sync_view, name='sync_view'),     # Rota para a view síncrona
    path('', home_view, name='home_view'),          # Rota para a página inicial
]
