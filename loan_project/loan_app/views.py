from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from models import Loan
from serializers import LoanSerializer


@api_view(['GET', 'POST'])
def loan_list(request, format=None):
    """
    List all loans, or create a new loan.
    """
    if request.method == 'GET':
        loans = Loan.objects.all()
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def loan_detail(request, pk, format=None):
    """
    Retrieve, update or delete a loan instance.
    """
    try:
        loan = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanSerializer(loan)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanSerializer(loan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)