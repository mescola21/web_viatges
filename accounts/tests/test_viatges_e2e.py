from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from accounts.models import User, Destinacio, Viatge
import time

class ViatgesE2ETest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = Options()
        options.add_argument("--headless")  # Ejecutar Chrome en modo headless
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        cls.browser = webdriver.Chrome(options=options)
        cls.browser.implicitly_wait(10)  # Espera implícita

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        # Crear un usuario para login
        self.test_user = User.objects.create_user(username="testuser", password="testpass123")
        # Crear una destinació para las reservas
        self.destinacio = Destinacio.objects.create(nom="Barcelona", pais="Espanya", continent="Europa")

    def login(self):
        self.browser.get(f'{self.live_server_url}/accounts/login/')
        self.browser.find_element(By.NAME, "username").send_keys("testuser")
        self.browser.find_element(By.NAME, "password").send_keys("testpass123")
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        WebDriverWait(self.browser, 10).until(
            EC.url_to_be(f'{self.live_server_url}/')
        )

    def test_crear_editar_eliminar_viatge(self):
        self.login()

        # Crear viatge: ir a la página de reserva de viatge
        self.browser.get(f'{self.live_server_url}/accounts/reserva/{self.destinacio.nom}/')

        # Rellenar formulario reserva
        num_persones_input = self.browser.find_element(By.NAME, "num_persones")
        num_persones_input.clear()
        num_persones_input.send_keys("3")

        data_inici_input = self.browser.find_element(By.NAME, "data_inici")
        data_inici_input.clear()
        data_inici_input.send_keys("2025-06-01")

        data_fi_input = self.browser.find_element(By.NAME, "data_fi")
        data_fi_input.clear()
        data_fi_input.send_keys("2025-06-10")

        # Enviar formulario
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Esperar confirmación reserva exitosa
        WebDriverWait(self.browser, 10).until(
            EC.text_to_be_present_in_element((By.TAG_NAME, "body"), "Reserva realitzada")
        )

        # Verificar que el viatge se creó
        viatge_creat = Viatge.objects.filter(user=self.test_user, destinacio=self.destinacio).first()
        self.assertIsNotNone(viatge_creat)
        self.assertEqual(viatge_creat.num_persones, 3)

        # Editar viatge: ir a página editar
        self.browser.get(f'{self.live_server_url}/accounts/editar-viatge/{viatge_creat.id}/')

        # Cambiar número de personas
        num_persones_edit = self.browser.find_element(By.NAME, "num_persones")
        num_persones_edit.clear()
        num_persones_edit.send_keys("5")

        # Guardar cambios
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Esperar redirección al perfil
        WebDriverWait(self.browser, 10).until(
            EC.url_contains('/accounts/profile')
        )

        # Refrescar el objeto de la BD para comprobar cambios
        viatge_creat.refresh_from_db()
        self.assertEqual(viatge_creat.num_persones, 5)

        # Eliminar viatge: ir a perfil y hacer submit de eliminar
        self.browser.get(f'{self.live_server_url}/accounts/profile/')

        # Encontrar el form para eliminar el viatge (buscamos por action)
        form_eliminar = self.browser.find_element(By.CSS_SELECTOR, f'form[action="/accounts/eliminar_viatge/{viatge_creat.id}/"]')
        form_eliminar.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Esperar redirección al perfil
        WebDriverWait(self.browser, 10).until(
            EC.url_contains('/accounts/profile')
        )

        # Comprobar que el viatge ya no existe
        self.assertFalse(Viatge.objects.filter(id=viatge_creat.id).exists())
