"""online_Car_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from car.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Home,name='home'),
    path('about/',about,name='about'),
    path('logout/',Logout,name='logout'),
    path('view_about/',view_about,name='view_about'),
    path('contact_update/',contact_update,name='contact_update'),
    path('contact/',Contact1,name='contact'),
    path('login/',Admin_Login,name='login'),
    path('admin_home/',Admin_Home,name='admin_home'),
    path('add_car/',Add_car,name='add_car'),
    path('add_company/',Add_company,name='add_company'),
    path('view_company/',View_Company,name='view_company'),
    path('view_car/',View_Car,name='view_car'),
    path('view_enquery/',view_enquery,name='view_enquery'),
    path('view_seenenquery/',view_seenenquery,name='view_seenenquery'),
    path('car_list/',car_list,name='car_list'),
    path('search_enquery/',search_enquery,name='search_enquery'),
    path('company_list/',company_list,name='company_list'),
    path('car_detail/(?P<pid>[0-9]+)',car_detail,name='car_detail'),
    path('company_detail/(?P<pid>[0-9]+)',company_detail,name='company_detail'),
    path('edit_car/(?P<pid>[0-9]+)',edit_car,name='edit_car'),
    path('edit_company/(?P<pid>[0-9]+)',edit_company,name='edit_company'),
    path('delete_company/(?P<pid>[0-9]+)',delete_company,name='delete_company'),
    path('delete_car/(?P<pid>[0-9]+)',delete_car,name='delete_car'),
    path('enquery_detail/(?P<pid>[0-9]+)',enquery_detail,name='enquery_detail'),
    path('seen_enquery/(?P<pid>[0-9]+)',seen_enquery,name='seen_enquery'),

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
