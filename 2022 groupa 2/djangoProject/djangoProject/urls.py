"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from CarShopApp.views import index, repairs, edit_fix, delete_fix

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('repairs/', repairs, name='repairs'),
    path('edit/<int:fix_id>', edit_fix, name='edit_fix'),
    path('delete/<int:fix_id>', delete_fix, name='delete_fix'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
