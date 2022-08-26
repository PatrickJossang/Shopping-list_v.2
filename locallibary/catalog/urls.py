from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListView.as_view(),name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('store/', views.ItemListView.as_view(),name='store'),
    path('store/<int:pk>', views.ItemDetailView.as_view(), name='store-detail'),
]