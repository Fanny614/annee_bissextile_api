from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from anneebissextile.settings import BASEURL
from bissextile.models import Bissextile
from bissextile.serializers import BissextileSerializer
from bissextile.utils import est_bissextile


class TestBissextile(TestCase):

    def test_est_bissextile(self):
        self.assertTrue(est_bissextile(2024))

    def test_non_bissextile(self):
        self.assertFalse(est_bissextile(2023))


class TestView(TestCase):
    url_single = reverse("single")
    url_range = reverse("range")
    url_history = reverse("history")

    def test_create_est_bissextile(self):
        """
        Test, dans le premier endpoint, qu'en donnant une année bissextile en entrée, on obtient la bonne sortie
        """
        response = self.client.post(path=BASEURL + self.url_single, data={"annee": 2004})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "L'année 2004 est bissextile.")

    def test_create_non_bissextile(self):
        """
        Test, dans le premier endpoint, qu'en donnant une année qui n'est pas bissextile en entrée, on obtient la bonne sortie
        """
        response = self.client.post(path=BASEURL + self.url_single, data={"annee": 2003})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "L'année 2003 n'est pas bissextile.")

    def test_create_requete_invalide(self):
        """
        Test, dans le premier endpoint, qu'en donnant une entrée invalide, on obtient bien le message d'erreur
        """
        response = self.client.post(path=BASEURL + self.url_single, data={"annee": "truc invalide"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), "La requête n'est pas valide")

    def test_list(self):
        """
        Test que l'historique fonctionne (le troisième endpoint)
        """
        serializer = BissextileSerializer(Bissextile.objects.all(), many=True)
        response = self.client.get(path=BASEURL + self.url_history)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data, response.json())

    def test_range(self):
        """
        Test, dans le deuxième endpoint, qu'en donnant un intervalle d'année en entrée,
        on obtient toutes les années bissextile comprise entre ces deux années
        """
        data = {"annee_debut": 1995, "annee_fin": 2000}
        response = self.client.post(path=BASEURL + self.url_range, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), "Les années 1996 sont bissextiles.")

    def test_range_requete_invalide(self):
        """
        Test, dans le deuxième enpoint, qu'en donnant une requête invalide, on obtient bien le message d'erreur
        """
        data_invalide = {"annee_debut": "entree invalide", "annee_fin": 242424}
        response = self.client.post(path=BASEURL + self.url_range, data=data_invalide)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json(), "La requête n'est pas valide.")
