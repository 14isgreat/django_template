from django.contrib import admin
from django.urls import path, include  # include is used to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('main.urls')),  # Include the app's URLs
]
