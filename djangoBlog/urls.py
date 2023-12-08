from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('contact/', views.contact),
    path('categories/', views.categories),
    path('about/', views.about),
    path('authorisation/', views.authorisation),
    path('registration/', views.registration)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)