from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

#rooms = [
#    {'id':1, 'name':'Lets learn python!'},
#    {'id':2, 'name':'Design with me!!'},
#    {'id':3, 'name':'Back end slaves!'},
#


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    ## topic__name=q não retorna nada na home, pois topic__name só inclui
    ## o que tem exatamente o topic name. topic__name__contains retorna
    ## tudo na página principal, pois inclui tudo que CONTENHA "q", e nada
    ## está contido em todos os objetos. ;)
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics':topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)

    #room = None

    # O loop for abaixo basicamente confere qual índex de rooms é o pedido na URL.
    #for i in rooms:
    #    if i['id'] == int(pk):
    #        room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')


    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render(request, 'base/room_form.html', context)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.method == 'POST':
        Room.objects.get(id=pk).delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})