from django.urls import path, include
from borrowings.views import BorrowingViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register("borrowings", BorrowingViewSet, basename="borrowings")

urlpatterns = [
    path("", include(router.urls)),
    path(
        'borrowings/<int:pk>/return_borrowing/',
        BorrowingViewSet.as_view({'post': 'return_borrowing'}),
        name='return_borrowing'
    ),
]


app_name = "borrowings"
