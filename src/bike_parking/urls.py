"""
URL configuration for bike_parking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from drf_spectacular import views as drf_spectacular_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(r"api/auth/", include("knox.urls")),
    path(
        "api/schema/", drf_spectacular_views.SpectacularAPIView.as_view(), name="schema"
    ),
    path(
        "api/schema/swagger-ui/",
        drf_spectacular_views.SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        drf_spectacular_views.SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/users/", include("user.urls")),
    path("api/partner_location/", include("partner_location.urls")),
    path("api/reservation/", include("reservation.urls")),
    path("api/subscription/", include("subscription.urls")),
]
