from django.urls import path,include
from . import views
urlpatterns = [
   path('register/', views.register, name='register'),
   path('login/', views.custom_login, name='login'),
   path('logout/', views.custom_logout, name='logout'),
   path('activate/<uidb64>/<token>', views.activate, name='activate'),
   path("passwordchange/", views.password_change, name="password_change"),
   path("passwordreset/", views.password_reset_request, name="password_reset"),
   path('reset/<uidb64>/<token>/', views.passwordResetConfirm, name='password_reset_confirm'),
   path('oauth/', include('social_django.urls', namespace='social')),
]
