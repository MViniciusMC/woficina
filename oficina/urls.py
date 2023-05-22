from django.urls import path
from oficina.views import index

urlpatterns = [
        path('', index)
]