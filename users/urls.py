from django.urls import path
from users import views


urlpatterns = [
    path('auth/', views.OTPView.as_view()),
    path('confirm/', views.OTPConfirmView.as_view()),
]