from django.urls import path
from .views import timer_view

urlpatterns = [
    path('timer/', timer_view, name='timer-view'),
]
