from django.urls import path
from excursions import views


app_name = 'excursions'

urlpatterns = [
    path('', views.ExcursionListView.as_view(), name='excursion-list'),
    path('create/', views.ExcursionCreateView.as_view(), name='excursion-create'),
    path('destinations/', views.DestinationListView.as_view(), name='destination-list'),
    path('features/', views.FeatureListView.as_view(), name='feature-list'),
    path('features/create/', views.FeatureCreateView.as_view(), name='feature-create'),
    path('destinations/create/', views.DestinationCreateView.as_view(), name='destination-create'),
    path('destinations/<int:pk>/edit/', views.DestinationEditView.as_view(), name='destination-edit'),
    path('destinations/<int:pk>/delete/', views.DestinationDeleteView.as_view(), name='destination-delete'),
    path('features/<int:pk>/edit/', views.FeatureEditView.as_view(), name='feature-edit'),
    path('features/<int:pk>/delete/', views.FeatureDeleteView.as_view(), name='feature-delete'),
    path('<slug:slug>/', views.ExcursionDetailView.as_view(), name='excursion-detail'),
    path('<slug:slug>/edit/', views.ExcursionEditView.as_view(), name='excursion-edit'),
    path('<slug:slug>/delete', views.ExcursionDeleteView.as_view(), name='excursion-delete'),
]
