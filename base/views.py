from django.shortcuts import render

rooms = [
    {'id':1, 'name':'Lets learn python!'},
    {'id':2, 'name':'Design with me!!'},
    {'id':3, 'name':'Back end slaves!'},
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None

    # O loop for abaixo basicamente confere qual índex de rooms é o pedido na URL.
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room':room}
    return render(request, 'base/room.html', context)