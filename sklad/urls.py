from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from users import views
from users.views import LoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/choice/', include('main.urls'), name='choice'),
    path('product/', include('product.urls'), name="product"),
    path('food/', include('food.urls'), name="food"),
    path('', include('users.urls')),
    path('users/login', views.LoginView.as_view(), name='login'),
    path('users/logout', views.LoginView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)