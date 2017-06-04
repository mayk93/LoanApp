from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from models import Loan
from serializers import LoanSerializer


@csrf_exempt
def loan_list(request):
    """
    List all loans, or create a new loan.
    """
    if request.method == 'GET':
        snippets = Loan.objects.all()
        serializer = LoanSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LoanSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def loan_detail(request, pk):
    """
    Retrieve, update or delete a loan.
    """
    try:
        snippet = Loan.objects.get(pk=pk)
    except Loan.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LoanSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LoanSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)