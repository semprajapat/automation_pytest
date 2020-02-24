from django.urls import path
from .views import DataView

d1 = DataView.as_view({
    'get':'list',
    'post':'create',
})

d2 = DataView.as_view({
    'get':'retrieve',
    'put':'update',
    'delete':'destroy'
})
urlpatterns = [
    path('getdata/',d1),
    path('getdata/<int:pk>',d2),
]