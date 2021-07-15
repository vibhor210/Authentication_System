from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('landing', views.landing, name="landing"),
    path('logout', views.log_out, name="logout"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)