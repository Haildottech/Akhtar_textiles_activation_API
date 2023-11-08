from django.urls import path
from .views import DynamicResponse, ChangeResponse

urlpatterns = [
    path('ATactivation-response/', DynamicResponse.as_view(), name='AT-activation-response'),
    path('ATactivation-changeresponse/', ChangeResponse.as_view(), name='AT-activation-change-response'),
]
