from rest_framework import permissions,viewsets

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