from django.contrib import admin
from django.urls import path 
from vege import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.index , name= "home"),
    path('show' , views.show , name= "show"),
    path('delete-receipe/<id>/' , views.delete_receipe , name="delete_receipe"),
    path('update-receipe/<id>/' , views.update_receipe , name="update_receipe"),
    path('ragister' , views.ragister , name= "ragister"),
    path('login-page' , views.login_page, name= "login_page"),
    path('logout' , views.logout_page, name= "logout_page"),
    




]
