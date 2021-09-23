from unittest import TestCase

from client.client import getAttack

class TestClient(TestCase):
    def getAttack(self):
        # GIVEN
        entier=1

        # WHEN
        result = getAttack(entier)
        # THEN
        self.assertEqual(result, 1)
