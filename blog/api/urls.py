from django.urls import path
from . import views
# from .views import ItemListView, ItemDetailView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = [
    
    path('',include(router.urls)),
    path('token/',TokenObtainPairView.as_view()),
    path('token/refresh/',TokenRefreshView.as_view()),
    
    # path('items/', ItemListView.as_view(), name='item_list'),
    # path('items/<int:id>', ItemDetailView.as_view(), name='item_detail'),
    
    # path('items/', views.item_list, name='item_list'),
    # path('items/<int:id>', views.item_detail, name='item_detail'),
]