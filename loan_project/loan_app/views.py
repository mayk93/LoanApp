from django.contrib.auth.models import User

from models import Loan
from serializers import LoanSerializer, UserSerializer
from permisions import IsOwnerSuperUserOrReadOnly
from rest_framework import permissions, renderers, viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    # authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerSuperUserOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def synopsis(self, request, *args, **kwargs):
        loan = self.get_object()
        return Response(loan.synopsis)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'loans': reverse('loan-list', request=request, format=format)
    })