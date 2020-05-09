from django.urls import path, include
from .views import TaskView

app_name = "todo"

urlpatterns=[
    path('todo/', TaskView.as_view()),
    path('todo/<int:pk>', TaskView.as_view()),
    path('todo/<int:pk>/execute/', TaskView.as_view()),
    path('todo/', include('rest_auth.urls')),
]