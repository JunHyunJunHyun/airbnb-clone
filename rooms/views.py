from math import ceil

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage

from . import models


def all_rooms(request):
    page = request.GET.get("page", 1)
    print("=" * 10)
    print(request)
    print("=" * 10)
    print(request.GET)
    print("=" * 10)
    print(request.GET.get("page"))
    print("=" * 10)
    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:
        rooms = paginator.page(int(page))

        return render(request, "rooms/home.html", {"page": rooms})
    except EmptyPage:
        return redirect("/")

