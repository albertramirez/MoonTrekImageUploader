from django.urls import path

from . import views

app_name = "upload"
# Upload App url is linked in the main project urls
urlpatterns= [
    path('', views.upload, name="upload") #here is the upload view path url patterns
]