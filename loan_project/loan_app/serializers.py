from rest_framework import serializers
from models import Loan


class LoanSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    company = serializers.CharField(required=True, allow_blank=False, max_length=100)
    sector = serializers.CharField(required=True, allow_blank=False, max_length=100)
    synopsis = serializers.CharField(style={'base_template': 'textarea.html'},
                                     required=False, allow_blank=True, max_length=500)
    amount = serializers.IntegerField(required=True)
    approved = serializers.BooleanField(default=False)

    def create(self, validated_data):
        """
        Create and return a new `Loan` instance, given the validated data.
        """
        return Loan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Loan` instance, given the validated data.
        """
        instance.created = validated_data.get('created', instance.created)
        instance.company = validated_data.get('company', instance.company)
        instance.sector = validated_data.get('sector', instance.sector)
        instance.synopsis = validated_data.get('synopsis', instance.synopsis)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.approved = validated_data.get('approved', instance.approved)
        instance.save()

        return instance