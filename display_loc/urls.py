from django.urls import path
from django.views.generic import ListView
from .models import ISSLocation

urlpatterns = [
    path('', ListView.as_view(model=ISSLocation, paginate_by=15), name='home'),
]