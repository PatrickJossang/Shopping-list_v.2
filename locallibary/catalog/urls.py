from django.urls    import path
from .              import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items/', views.ItemListView.as_view(),name='items'),
    path('item/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('store/', views.StoreListView.as_view(),name='store'),
    path('store/<int:pk>', views.StoreDetailView.as_view(), name='store-detail'),
    path('myitems/', views.UsersItemsByListView.as_view(), name='my-items'),
    path('item/<uuid:pk>/renew/', views.renew_item, name='renew-item'),
    path('store/create/', views.StoreCreate.as_view(), name='store-create'),
    path('store/<int:pk>/update/', views.StoreUpdate.as_view(), name='store-update'),
    path('store/<int:pk>/delete/', views.StoreDelete.as_view(), name='store-delete'),
    path('item/create/', views.ItemCreate.as_view(), name='item-create'),
    path('item/<int:pk>/update/', views.ItemUpdate.as_view(), name='item-update'),
    path('item/<int:pk>/delete/', views.ItemDelete.as_view(), name='item-delete'),
]