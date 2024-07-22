from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer

# Requisições HTTP dos métodos GET, POST, PUT e DELETE
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request, nick=None):
    if request.method == 'GET':
        return handle_get(request, nick)
    elif request.method == 'POST':
        return handle_post(request)
    elif request.method == 'PUT':
        return handle_put(request, nick)
    elif request.method == 'DELETE':
        return handle_delete(request, nick)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

# LISTAR usuarios
def handle_get(request, nick=None):
    if nick:
        user = get_user_by_nickname(nick)
        if user:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

# POST
def handle_post(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# PUT
def handle_put(request, nick=None):
    if not nick:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = get_user_by_nickname(nick)
    if not user:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE
def handle_delete(request, nick=None):
    if not nick:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    user = get_user_by_nickname(nick)
    if not user:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# LISTAR por nick
def get_user_by_nickname(nick):
    try:
        return User.objects.get(user_nickname=nick)
    except User.DoesNotExist:
        return None
