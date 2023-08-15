from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='homepage'),
    path('inputform/', views.InputFormView.as_view(), name='inputform'),
    path('showtasks/', views.ShowTasksListView.as_view(), name='showtasks'),
    path('completed/', views.CompletedListView.as_view(), name='completed'),
    path('deletetasks/<int:pk>', views.TaskDeleteView.as_view(), name='deletetasks'),
    path('updatetasks/<int:pk>', views.TaskUpdateView.as_view(), name='updatetasks'),
    path('completetasks/<int:pk>', views.CompleteTaskUpdateView, name='completetasks'),
]
