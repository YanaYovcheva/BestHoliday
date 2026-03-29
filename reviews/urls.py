from django.urls import path
from reviews import views


app_name = 'reviews'

urlpatterns = [
    path('create/<slug:slug>/', views.CommentCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.CommentEditView.as_view(), name='edit'),
    path('<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete'),
]