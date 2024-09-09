from django.shortcuts import render
from django.http import HttpResponse

rooms =[
    {"id":1, "name": "One"},
    {"id":2, "name": "Two"},
    {"id":3, "name": "Three"},
]

def Home(request):
    context = {"rooms":rooms}
    return render(request,"base/home.html",context)

def Room(request,pk):
    selectedRoom = None
    for room in rooms:
        if room["id"] == int(pk):
            selectedRoom = room
    context = {"room": selectedRoom}
    return render(request,"base/room.html",context)
