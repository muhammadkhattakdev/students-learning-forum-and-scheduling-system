from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('scheduling_app.urls')),
    path('auth/', include('auth_app.urls')),
    path('forum/', include('forum.urls'),)
]
