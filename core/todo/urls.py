from django.urls import path
from . import views



urlpatterns = [
	path('', views.TaskList.as_view(), name='tasks'),
	path('task/<int:pk>/', views.TaskDetail.as_view(), name='detail'),
	path('create/', views.TaskCreate.as_view(), name='task-create'),
	path('update/<int:pk>/', views.TaskEdit.as_view(), name='update'),
	path('delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
	
]