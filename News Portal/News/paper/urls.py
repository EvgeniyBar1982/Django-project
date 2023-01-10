from django.urls import path
from .views import index,detail


urlpatterns = [
    path('paper_list/', index, name='index'),
    path('news/<int:pk>/', detail, name='detail')

]
