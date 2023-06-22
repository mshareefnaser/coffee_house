from django.urls import path
from .views import CoffeeListView, CoffeeDetailView, CoffeeCreateView, CoffeeUpdateView, CoffeeDeleteView

urlpatterns = [
    path('coffee/', CoffeeListView.as_view(), name='coffee_list'),
    path('coffee/<int:pk>/', CoffeeDetailView.as_view(), name='coffee_detail'),
    path('coffee/create/', CoffeeCreateView.as_view(), name='coffee_create'),
    path('coffee/<int:pk>/update/', CoffeeUpdateView.as_view(), name='coffee_update'),
    path('coffee/<int:pk>/delete/', CoffeeDeleteView.as_view(), name='coffee_delete'),
]