from django.urls import path
from .views import RealtorListView,RealtorView,TopsellerView

urlpatterns = [
    path('', RealtorListView.as_view()),
    path('topseller', TopsellerView.as_view()),
    path('<pk>', RealtorView.as_view()),
]
