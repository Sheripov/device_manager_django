import io
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from management import models


def generate_photo_file():
    file = io.BytesIO()
    image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test.png'
    file.seek(0)
    return file


class UserTests(APITestCase):
    def test_create_read_user(self):
        """
        Ensure we can create a new user object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        url = reverse('management:user_list')
        photo_file = generate_photo_file()
        data = {
            'first_name': 'Farruh',
            'last_name': 'Sheripov',
            'user_photo': photo_file,
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.User.objects.count(), 1)
        self.assertEqual(models.User.objects.get().first_name, 'Farruh')


class TeamTests(APITestCase):
    def test_create_team(self):
        """
        Ensure we can create a new team object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        url = reverse('team-list')
        data = {
            'team_name': 'Farruh',
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Team.objects.count(), 1)
        self.assertEqual(models.Team.objects.get().team_name, 'Farruh')


class BuyerTests(APITestCase):
    def test_create_buyer(self):
        """
        Ensure we can create a new buyer object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        url = reverse('buyer-list')
        data = {
            'buyer_name': 'Farruh',
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Buyer.objects.count(), 1)
        self.assertEqual(models.Buyer.objects.get().buyer_name, 'Farruh')


class DeviceTypeTests(APITestCase):
    def test_create_devicetype(self):
        """
        Ensure we can create a new device type object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        url = reverse('devicetype-list')
        data = {
            'device_type': 'Farruh',
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.DeviceType.objects.count(), 1)
        self.assertEqual(models.DeviceType.objects.get().device_type, 'Farruh')


class DeviceTests(APITestCase):
    def test_create_device(self):
        """
        Ensure we can create a new device object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        url = reverse('device-list')
        photo_file = generate_photo_file()
        data = {
            'device_name': 'qwerty',
            'price': 123,
            'paid_by': models.Buyer.objects.create(buyer_name='Farruh').id,
            'team': models.Team.objects.create(team_name='Farruh').id,
            'configuration': 'http://127.0.0.1:51431/',
            'device_photo': photo_file,
            'device_type': models.DeviceType.objects.create(device_type='Farruh').id,
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Device.objects.count(), 1)
        self.assertEqual(models.Device.objects.get().device_name, 'qwerty')


class AssignmentTests(APITestCase):
    def test_create_assignment(self):
        """
        Ensure we can create a new assignment object.
        """
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)
        photo_file = generate_photo_file()
        url = reverse('assignment-list')
        user = models.User.objects.create(
            user_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            first_name='User3',
            last_name='Test3', )
        buyer = models.Buyer.objects.create(buyer_name='qweq')
        team = models.Team.objects.create(team_name='qwertyq')
        devicetype = models.DeviceType.objects.create(device_type='asdq')
        device = models.Device.objects.create(
            device_name='qwertyq',
            price=1232,
            paid_by=buyer,
            team=team,
            configuration='http://127.0.0.1:514312/',
            device_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            device_type=devicetype, )
        data = {
            'user': models.User.objects.get().id,
            'device': models.Device.objects.get().item_number,
            'comment': 'test comment',
        }

        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Assignment.objects.count(), 1)
        self.assertEqual(models.Assignment.objects.get().user_id, 1)
