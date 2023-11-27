from django.test import TestCase
from django.contrib.auth.models import User  # Import the User model
from app_blog.models import Articulo
from datetime import date

class ArticuloTests(TestCase):
    """En esta clase van todas las pruebas del modelo Articulo."""

    def setUp(self):
       
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_creacion_articulos(self):
        articulo = Articulo(
            titulo="titulo",
            subtitulo="subtitulo",
            cuerpo="cuerpo",
            autor="autor",
            fecha="2023-11-23",
            creador=self.user 
        )
        articulo.save()

        self.assertEqual(Articulo.objects.count(), 1)


    def test_Articulo_str(self):
        articulo = Articulo(
            titulo="titulo",
            subtitulo="subtitulo",
            cuerpo="cuerpo",
            autor="autor",
            fecha="2023-11-23",
            creador=self.user
        )
        articulo.save()


