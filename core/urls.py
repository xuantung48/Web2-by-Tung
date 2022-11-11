from django.urls import path, include
from .views import Index, Shop, About, Single, Login, Register, Coming, Contact
urlpatterns = [
    path('index/', Index.as_view(), name = "index" ),
    path('shop/', Shop.as_view(), name = "shop"),
    path('about/', About.as_view(), name = "about"),
    path('single/', Single.as_view(), name = "single"),
    path('login/', Login.as_view(), name = "login"),
    path('register/', Register.as_view(), name = "register"),
    path('coming/', Coming.as_view(), name = "coming"),
    path('contact/', Contact.as_view(), name="contact"),
]