from django.urls import path
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
    path('add_product/',views.data),
    path('delete/<int:qk>/',views.delete_data),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
