from django.urls import path

from . import views

urlpatterns = [
    
 
     path("create_<slug:slug>/",views.CreateSoundAPIView.as_view()),
     path("update_<slug:slug>/<int:pk>",views.UpdateSoundAPIView.as_view()),
     path("delete_<slug:slug>/<int:pk>",views.DeleteSoundAPIView.as_view()),
     path('<slug:slug>', views.ListSoundAPIView.as_view()),

   
 ]