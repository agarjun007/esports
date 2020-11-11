from django.urls import path
from . import views



urlpatterns = [
  path('trial/',views.gh,name='trial'),
]