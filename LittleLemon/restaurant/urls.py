from django.urls import path, include
from .views import *
urlpatterns = [
    path('', index, name='home'),
    # path('booking', BookingView.as_view()),
    path('menu', MenuItemsView.as_view()),
    path('menu/<int:pk>', SingleMenuItemView.as_view()),
]