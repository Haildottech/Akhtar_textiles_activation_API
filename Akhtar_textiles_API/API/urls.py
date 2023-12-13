from django.urls import path
from .views import DynamicResponse, ChangeResponse,DynamicResponse_desktop,ChangeResponse_desktop

urlpatterns = [
    path('ATactivation-response/', DynamicResponse.as_view(), name='AT-activation-response'),
    path('ATactivation-changeresponse/', ChangeResponse.as_view(), name='AT-activation-change-response'),
    path('ATactivation-desktop-response/', DynamicResponse_desktop.as_view(), name='AT-activation-desktop-response'),
    path('ATactivation-desktop-changeresponse/', ChangeResponse_desktop.as_view(), name='AT-activation-change-desktop-response'),
]
