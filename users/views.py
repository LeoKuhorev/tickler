from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import CustomUser, Profile
from .serializers import ProfileSerializer, UserSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def token_blacklist(request):
    """Blacklist the given refresh token
    """
    try:
        refresh_token = request.data["refresh_token"]
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_202_ACCEPTED)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile(request):
    """
    Retrieve or update profile info
    """
    try:
        user = request.user
        profile = user.profile
    except (Profile.DoesNotExist, CustomUser.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated & IsAdminUser])
def user_list(request):
    users = CustomUser.objects.filter(profile__manager=request.user).order_by('id')
    serialized_users = []
    
    for user in users:
        serialized_profile = ProfileSerializer(user.profile).data
        serialized_user = UserSerializer(user).data
        serialized_user.update(serialized_profile)
        serialized_users.append(serialized_user)
        
    return Response(serialized_users, status=status.HTTP_200_OK)
