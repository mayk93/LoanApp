from django.contrib.auth.models import User
from rest_framework import serializers
from models import Loan


class LoanSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Loan
        fields = ('id', 'company', 'sector', 'synopsis', 'amount', 'approved')


class UserSerializer(serializers.ModelSerializer):
    loans = serializers.PrimaryKeyRelatedField(many=True, queryset=Loan.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'loans')