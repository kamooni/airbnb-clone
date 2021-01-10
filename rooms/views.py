from datetime import datetime
from django.shortcuts import render  # response에 html을 넣어서 전달할 수 있게 해준다 !


def all_rooms(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_rooms.html", context={"now": now, "hungry": hungry})
