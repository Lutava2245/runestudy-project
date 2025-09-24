from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Reward, Skill, User
from .serializers import RewardSerializer, SkillSerializer, UserSerializer


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
    
    return Response({'Nenhum usuário encontrado': 'Tente outros filtros'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def userDetail(request, pk):
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except User.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)


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
    try:
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except User.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def userDelete(request, pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        return Response('Usuário deletado com sucesso!', status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def skillList(request):
    skills = Skill.objects.filter(**request.query_params.dict()) if request.query_params else Skill.objects.all()

    if skills:
        serializer = SkillSerializer(skills, many=True)
        return Response(serializer.data)
    
    return Response({'Nenhuma habilidade encontrada': 'Tente outros filtros'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def skillDetail(request, pk):
    try:
        skill = Skill.objects.get(id=pk)
        serializer = SkillSerializer(skill, many=False)
        return Response(serializer.data)
    except Skill.DoesNotExist:
        return Response({'error': 'Habilidade não encontrada'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def skillCreate(request):
    skill = SkillSerializer(data=request.data)

    if Skill.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This skill already exists")
    
    if skill.is_valid():
        skill.save()
        return Response(skill.data)
    
    return Response(skill.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def skillUpdate(request, pk):
    try:
        skill = Skill.objects.get(id=pk)
        serializer = SkillSerializer(instance=skill, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Skill.DoesNotExist:
        return Response({'error': 'Habilidade não encontrada'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def skillDelete(request, pk):
    try:
        skill = Skill.objects.get(id=pk)
        skill.delete()
        return Response('Habilidade deletada com sucesso!', status=status.HTTP_204_NO_CONTENT)
    except Skill.DoesNotExist:
        return Response({'error': 'Habilidade não encontrada'}, status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def rewardList(request):
    rewards = Reward.objects.filter(**request.query_params.dict()) if request.query_params else Reward.objects.all()

    if rewards:
        serializer = RewardSerializer(rewards, many=True)
        return Response(serializer.data)
    
    return Response({'Nenhuma recompensa encontrada': 'Tente outros filtros'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def rewardDetail(request, pk):
    try:
        reward = Reward.objects.get(id=pk)
        serializer = RewardSerializer(reward, many=False)
        return Response(serializer.data)
    except Reward.DoesNotExist:
        return Response({'error': 'Recompensa não encontrada'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def rewardCreate(request):
    reward = RewardSerializer(data=request.data)

    if Reward.objects.filter(**request.data).exists():
        raise serializers.ValidationError("This reward already exists")
    
    if reward.is_valid():
        reward.save()
        return Response(reward.data)
    
    return Response(reward.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def rewardUpdate(request, pk):
    try:
        reward = Reward.objects.get(id=pk)
        serializer = RewardSerializer(instance=reward, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Reward.DoesNotExist:
        return Response({'error': 'Recompensa não encontrada'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def rewardDelete(request, pk):
    try:
        reward = Reward.objects.get(id=pk)
        reward.delete()
        return Response('Recompensa deletada com sucesso!', status=status.HTTP_204_NO_CONTENT)
    except Reward.DoesNotExist:
        return Response({'error': 'Recompensa não encontrada'}, status=status.HTTP_404_NOT_FOUND)