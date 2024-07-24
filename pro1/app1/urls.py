from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('sign_in/',views.entry,name='sign_ip'),
    path('signup/',views.signup,name='signup'),
    path('log_out/<int:qk>/',views.log_out,name='log_out'),
    path('menu/',views.menu),
    path('base/',views.base),
    path('all_entry/',views.all_product),
    path('add_product/',views.data),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
