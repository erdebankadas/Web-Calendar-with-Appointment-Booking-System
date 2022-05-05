from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"), 
    path('home', views.Home, name="home"),
    path('appointment', views.Appointment, name="appointment"),
    path('user_signup', views.User_Registration, name="user_signup"),
    path('user_login', views.User_Login, name="user_login"),
    #path('user_logout', views.user_logout, name="user_logout"),
    path("signup", views.register, name = "signup"),
    path("login", views.login, name = "login"),
    path('logout', views.logout, name = "logout"),
    path('contact', views.Contact, name = "contact"),
    path('manage_appointment', views.manage_appointment, name = "manage_appointment"),
    path('cancel_appointment/<int:id>', views.cancel_appointment, name = "cancel_appointment"),
    path('profile/<int:id>', views.Profile, name = "profile"),
    path('profile', views.Profile_all, name = "profile_all"),
    path('reschedule/<int:id>', views.reschedule_appointment, name = "reschedule"),
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
