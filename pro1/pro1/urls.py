from app1.views import ProductView
from rest_framework import routers
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView,TokenObtainPairView

router = routers.DefaultRouter()
router.register('productapi',ProductView)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    path('rout/',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='obtain_pair_view'),
    path('verifytoken/',TokenVerifyView.as_view(),name='verify_pair_view'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='refresh_pair_view'),
    path('auth/',include('rest_framework.urls'))
]
