from django.urls import path,include
from. import views

urlpatterns = [
    path("modeltask/",views.mtask,name="modeltask"),
]