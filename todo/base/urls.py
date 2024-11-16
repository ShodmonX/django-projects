from django.urls import path

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path(route='', view=views.TaskList.as_view(), name='tasks'),
    path(route='task/<int:pk>/', view=views.TaskDetail.as_view(), name='task'),
    path(route='create-task/', view=views.TaskCreate.as_view(), name='task-create'),
    path(route='task-update/<int:pk>/', view=views.TaskUpdate.as_view(), name='task-update'),
    path(route='task-delete/<int:pk>/', view=views.TaskDelete.as_view(), name='task-delete'),

    path(route='login/', view=views.CustomLoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(next_page='tasks'), name='logout'),
    path(route='register/', view=views.RegisterPageView.as_view(), name='register'),
]