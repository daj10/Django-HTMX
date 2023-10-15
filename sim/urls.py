from django.urls import path
from sim import views

urlpatterns = [
    path('', views.search_view, name='search_view'),
    path('search/', views.search_view, name='search_view'),
    path('search/results/', views.search_results_view, name='search_results_view'),
]
