from django.urls import path
from .views import SignupView, TaskListCreateView, TaskDetailView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [

path('signup/', SignupView.as_view()),

path('signin/', TokenObtainPairView.as_view()),

path('tasks/', TaskListCreateView.as_view()),

path('tasks/<int:pk>/', TaskDetailView.as_view()),

]