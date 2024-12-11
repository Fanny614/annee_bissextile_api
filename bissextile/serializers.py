from rest_framework import serializers

from bissextile.models import Bissextile


class BissextileSerializer(serializers.Serializer):
    endpoint_utilise = serializers.CharField(max_length=100, required=False)
    # Pour le premier endpoint
    annee = serializers.IntegerField(required=False)
    # Pour le deuxième endpoint
    annee_debut = serializers.IntegerField(required=False, allow_null=True)
    annee_fin = serializers.IntegerField(required=False, allow_null=True)
    # Osef pour le deuxième endpoint
    is_bissextile = serializers.BooleanField(required=False, allow_null=True)
    # Pour le deuxième endpoint
    annees_bissextiles = serializers.CharField(max_length=100, required=False, allow_null=True)

    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Bissextile.objects.create(**validated_data)
