from django.urls import path, include

import restaurant.views as views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("tables", views.BookingViewSet)

urlpatterns = [
    path("menu/", views.MenuItemView.as_view(), name="menu-list"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    path("booking/", include(router.urls)),
    path('api-token-auth/', obtain_auth_token)
]   