from django.contrib.auth.models import User
from rest_framework import serializers
from models import Loan


class LoanSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    synopsis = serializers.HyperlinkedIdentityField(view_name='loan-synopsis', format='html')

    class Meta:
        model = Loan
        fields = ('url', 'id', 'owner',
                  'company',
                  'sector', 'synopsis', 'amount', 'approved')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    loans = serializers.HyperlinkedRelatedField(many=True, view_name='loan-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'loans')