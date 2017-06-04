from django.contrib.auth.models import User
from models import Loan
from serializers import LoanSerializer, UserSerializer
from permisions import IsOwnerOrReadOnly
from rest_framework import generics, permissions, renderers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class LoanList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanSynopsis(generics.GenericAPIView):
    queryset = Loan.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        loan = self.get_object()
        return Response(loan.synopsis)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'loans': reverse('loan-list', request=request, format=format)
    })