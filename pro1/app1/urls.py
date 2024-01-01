from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.entry,name='entry'),
    path('index/',views.index),
    path('signup/',views.signup),
    path('table/',views.table),
    path('menu/',views.menu),
    path('data/',views.data),
    path('product/',views.product),
    path('ragistration/',views.ragistration),
    path("delete/<int:pk>/",views.delete,name='delete')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
