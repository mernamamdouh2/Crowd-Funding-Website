from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('rate/<int:project_id>/<int:rating>/', views.rate, name='rating'),
    path('edit_user_profile/', views.edit_user_profile, name='edit_user_profile'),
    path('delete_user_profile/', views.delete_user_profile, name='delete_user_profile'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('delete_project/<int:project_id>/', views.delete_project, name='delete_project'),
    path('categories/', views.category_list, name='category_list'),
    path('projects/<int:pk>/', views.project_details, name='project_details'),
]
handler404 = 'indexapp.views.handler404'
