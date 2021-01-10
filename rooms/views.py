from math import ceil
from datetime import datetime
from django.shortcuts import render  # response에 html을 넣어서 전달할 수 있게 해준다 !
from django.core.paginator import Paginator
from . import models


def all_rooms(request):
    page = request.GET.get("page")
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10)
    rooms = paginator.get_page(page)
    return render(request, "rooms/home.html", {"rooms": rooms})
