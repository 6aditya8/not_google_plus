import json

from django.contrib.auth import authenticate, login

from rest_framework import permissions,viewsets
from rest_framework.response import Response
from rest_framework import status, views

from .models import Account
from .serializers import AccountSerializer
from .permissions import IsAccountOwner


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

    def get_permissions(self):

        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status = status.HTTP_201_CREATED)

        return Response({
                        'status': 'Bad Request',
                        'message': "Account couldn't be created"
        }, status = status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    
    def post(self, request, format = None):
        data = json.loads(request.body)
        email = data.get('email', None)
        password = data.get('password', None)
        account = authenticate(email = email, password = password)

        if account is not None:

            if account.is_active:
                login(request, account)
                serialized = AccountSerializer(account)
                
                return Response(serialized.data)

            else:
                return Response({
                    'status':'UnAuthorized',
                    'message': 'This account has been disabled',
                }, status = tatus.HTTP_401_UNAUTHORIZED)

        else:
            return Response({
                    'status':'UnAuthorized',
                    'message': 'Username or Password is incorrect',
                }, status = tatus.HTTP_401_UNAUTHORIZED)
