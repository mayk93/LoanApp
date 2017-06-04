from models import Loan
from serializers import LoanSerializer
from rest_framework import generics


class LoanList(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer