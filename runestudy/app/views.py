from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'Task List': '/tasks/',
        'Task Detail View': '/tasks/<str:pk>/',
        'Task Create': '/tasks/create/',
        'Task Update': '/tasks/<str:pk>/update/',
        'Task Delete': '/tasks/<str:pk>/delete/',
        'Task List by Skill': '/tasks/?fskill=<str:skill_id>',
        'Skill List': '/skills/',
        'Skill Detail View': '/skills/<str:pk>/',
        'Skill Create': '/skills/create/',
        'Skill Update': '/skills/<str:pk>/update/',
        'Skill Delete': '/skills/<str:pk>/delete/',
        'Reward List': '/rewards/',
        'Reward Detail View': '/rewards/<str:pk>/',
        'Reward Create': '/rewards/create/',
        'Reward Update': '/rewards/<str:pk>/update/',
        'Reward Delete': '/rewards/<str:pk>/delete/',
        'User List': '/users/',
        'User Detail View': '/users/<str:pk>/',
        'User Create': '/users/create/',
        'User Update': '/users/<str:pk>/update/',
        'User Delete': '/users/<str:pk>/delete/',
    }

    return Response(api_urls)


@api_view(['GET'])
def userList(request):
    users = User.objects.filter(**request.query_params.dict()) if request.query_params else User.objects.all()

    if users:
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    return Response({'Nenhum usuário encontrado': 'Tente outros filtros'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def userDetail(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def userCreate(request):
    user = UserSerializer(data=request.data)

    if User.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This user already exists")
    
    if user.is_valid():
        user.save()
        return Response(user.data)
    
    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def userUpdate(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def userDelete(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('Usuário deletado com sucesso!', status=status.HTTP_204_NO_CONTENT)