from django.contrib import admin
from django.urls import path
from django.conf.urls import include # add this
urlpatterns = [
    path('', include('dog_api.urls')), # add this
    path('admin/', admin.site.urls),
]