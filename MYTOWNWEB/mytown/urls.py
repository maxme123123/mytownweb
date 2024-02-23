from django.urls  import path

from . import views


urlpatterns = [
    path('workerlogin/', views.workerlogin),
     path('addreports/', views.addreports),


]
