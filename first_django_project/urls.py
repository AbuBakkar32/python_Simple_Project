from django.contrib import admin
from django.urls import path, include

import first_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('first_app.urls')),
]
