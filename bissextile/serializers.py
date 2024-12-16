from rest_framework import serializers

from bissextile.models import Bissextile


class BissextileSingleSerializer(serializers.Serializer):
    annee = serializers.IntegerField(required=True)

    def create(self, validated_data):
        return Bissextile.objects.create(**validated_data)




class BissextileRangeSerializer(serializers.Serializer):
    annee_debut = serializers.IntegerField(required=True, allow_null=True)
    annee_fin = serializers.IntegerField(required=True, allow_null=True)

    def create(self, validated_data):
        return Bissextile.objects.create(**validated_data)

    def validate(self, attrs):
        if attrs['annee_debut'] > attrs['annee_fin']:
            raise serializers.ValidationError()
        return attrs

class BissextileHistorySerializer(serializers.Serializer):
    endpoint_utilise = serializers.CharField(max_length=100, required=False)
    annee = serializers.IntegerField(required=False)
    is_bissextile = serializers.BooleanField(required=False, allow_null=True)

    annee_debut = serializers.IntegerField(required=False, allow_null=True)
    annee_fin = serializers.IntegerField(required=False, allow_null=True)
    annees_bissextiles = serializers.CharField(max_length=100, required=False, allow_null=True)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)
