from django.urls import path, include
from borrowings.views import BorrowingViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet, basename="borrowings")

urlpatterns = [
    path("", include(router.urls)),
]


app_name = "borrowings"
