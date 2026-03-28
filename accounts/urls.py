from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterAppUserView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/edit/', views.ProfileEditView.as_view(), name='profile-edit'),

]