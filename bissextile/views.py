from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK

from bissextile.models import Bissextile
from bissextile.serializers import BissextileSingleSerializer, BissextileRangeSerializer, BissextileHistorySerializer
from bissextile.utils import est_bissextile


@api_view(['POST'])
def single(request):
    """"
    Prend en entrée une année.
    Regarde si elle est bissextile.
    Sauvegarde l'information dans la base de donnée.
    Retourne à l'utilisateur si elle est bissextile ou non.
    """
    serializer = BissextileSingleSerializer(data=request.data)
    if serializer.is_valid():
        # On teste si l'année en entrée est bissextile ou non
        is_bis = est_bissextile(serializer.validated_data['annee'])
        # On enregistre dans la base de données
        objet_annee = Bissextile.objects.create(annee=serializer.validated_data['annee'], is_bissextile=is_bis,
                                                endpoint_utilise="Bissextile")
        # On affiche le bon message
        if objet_annee.is_bissextile:
            return Response(f"L'année {objet_annee.annee} est bissextile.", HTTP_200_OK)
        return Response(f"L'année {objet_annee.annee} n'est pas bissextile.", HTTP_200_OK)
    return Response("La requête n'est pas valide", HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list(request):
    """
    Permet de donner l'historique des requêtes effectués ainsi que la sortie de celles-ci
    Rangé par date de création croissante
    """
    serializer = BissextileHistorySerializer(Bissextile.objects.all(), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def rangea(request):
    """
    Prend en entrée un intervalle d'année.
    Regarde toutes les années bissextiles entre ces deux années.
    Sauvegarde l'information dans la basse de donnée.
    Retourne à l'utilisateur toutes les années bissextile.
    """
    serializer = BissextileRangeSerializer(data=request.data)
    if serializer.is_valid():
        annee_debut = serializer.validated_data['annee_debut']
        annee_fin = serializer.validated_data['annee_fin']
        # liste pour stocker les années bissextiles et pouvoir les retourner à l'utilisateur
        liste_annees = []
        # On parcourt tous les années et on regarde si elles sont bissextiles pour les ajouter ou non à la liste que l'on renvoie à l'utilisateur
        for _ in range(annee_fin - annee_debut + 1):
            if est_bissextile(annee_debut):
                liste_annees.append(annee_debut)
            annee_debut += 1
        # On convertit notre liste en chaine de charactère pour l'enregistrer et l'afficher sans les []
        liste_annees = str(liste_annees)[1:-1]
        # On sauvegarde dans la base de données
        Bissextile.objects.create(annee_debut=serializer.data['annee_debut'],
                                  annee_fin=serializer.data['annee_fin'], annees_bissextiles=liste_annees,
                                  endpoint_utilise="Range")
        return Response(f"Les années {liste_annees} sont bissextiles.", HTTP_200_OK)
    return Response(f"La requête n'est pas valide.", HTTP_400_BAD_REQUEST)
