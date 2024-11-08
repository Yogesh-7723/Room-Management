from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.index),
    path('sign_in/',views.signin,name='sign_in'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('log_out/<int:qk>/',views.log_out,name='log_out'),
    path('menu/',views.menu),
    path('all_entry/',views.all_product),
    path('add_product/',views.data,name='add_product'),
    path('delete/<int:qk>/',views.delete_data),
    #jwd function and classes
    # path("productapi/",views.ProductView.as_view({'get': 'list'}),name="productapi"),
    # path("productapi/<int:pk>/",views.ProductView.as_view({'get': 'retrieve'}),name="productapi"),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
