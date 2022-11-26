from django.contrib import admin
from django.urls import path
from api.views import addTask,getTask,getDelet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addTask/', addTask),
    path('getask/<int:id>', getTask),
    path('getdelet/<int:id>', getDelet),
]
