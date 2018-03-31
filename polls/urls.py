from django.urls import path, include
from polls.views import polls_detail, polls_list

urlpatterns = [
    path('polls/', polls_list, name='polls_list'),
    path('polls/<int:pk>/', polls_detail, name='polls_detail')
]