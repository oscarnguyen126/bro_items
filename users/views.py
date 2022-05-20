from .models import User
import hashlib
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


@api_view(['POST'])
@parser_classes([JSONParser])
def register(request):
    data = request.data
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    password_confirm = data.get('password_confirm')

    if not email:
        print('email is not valid')
    else:
        if User.objects.filter(email=email):
            return Response({'This email is already existed'})
        else:
            if password != password_confirm:
                print('Password is not match')
            password = hashlib.sha256(
                str(password).encode('utf-8')).hexdigest()
            user = User(email=email, username=username, password=password)
            user.save()
            return Response(user.to_dict())


def authenticate(email, password):
    password_digest = hashlib.sha256(str(password).encode('utf-8')).hexdigest()
    try:
        user = User.objects.get(email=email, password=password_digest)
    except User.DoesNotExist:
        return None
    return user


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(email=email, password=password)

    if user and user.is_active:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'Authorization': f'Token {token.key}',
            'user': user.to_dict()
        })
    else:
        return Response({'message':'Authentication failed'})


@api_view(['DELETE'])
def log_out(request):
    request.user.auth_token.delete()
    return Response({'message':'Logged out'})
