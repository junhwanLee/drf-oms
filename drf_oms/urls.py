from django.contrib import admin
from django.urls import path, include

from accounts.views import LoginView
from knox.views import LogoutView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/login', LoginView.as_view()),
    path('auth/logout', LogoutView.as_view(), name='knox_logout'),
    path('orders/', include('orders.urls')),
    path('accounts/', include('accounts.urls')),  # added
]