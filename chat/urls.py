from django.urls import path
from . import views

urlpatterns = [
   path("get-token/<str:email>/",views.create_connection), #Run with admin id
   path("join-room/<str:email>/<int:id>",views.join_room), #user, therapistget-token
   path("leave-room/<str:roomId>",views.leave_room),
   path("get-token/",views.get_token)
]