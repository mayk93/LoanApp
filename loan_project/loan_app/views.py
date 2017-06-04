from django.contrib.auth.models import User
from models import Loan
from serializers import LoanSerializer, UserSerializer
from permisions import IsOwnerOrReadOnly
from rest_framework import generics, permissions


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


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer