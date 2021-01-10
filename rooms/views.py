from datetime import datetime
from django.shortcuts import render  # response에 html을 넣어서 전달할 수 있게 해준다 !
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
