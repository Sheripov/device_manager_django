import datetime
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from API.serializers import UserSerializer, TeamSerializer, BuyerSerializer, DeviceTypeSerializer, DeviceSerializer, \
    AssignmentSerializer
from management.models import User, Team, Buyer, DeviceType, Device, Assignment


class UserSerializerTestCase(TestCase):
    def test_get_user_list(self):
        user_1 = User.objects.create(
            user_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            first_name='User1',
            last_name='Test1', )

        user_2 = User.objects.create(
            first_name='User2',
            last_name='Test2',
            user_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user2.png', 'rb').read()),
        )
        url = reverse('management:user_list')
        response = self.client.get(url)
        data = UserSerializer([user_1, user_2], many=True).data
        expected_data = [
            {
                'id': user_1.id,
                'first_name': 'User1',
                'last_name': 'Test1',
                'user_photo': user_1.user_photo.url,
                'employee_date': str(datetime.date.today()),
            },
            {
                'id': user_2.id,
                'first_name': 'User2',
                'last_name': 'Test2',
                'user_photo': user_2.user_photo.url,
                'employee_date': str(datetime.date.today()),
            }

        ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)


class TeamSerializerTestCase(TestCase):
    def test_get_team_list(self):
        test_1 = Team.objects.create(team_name='qwerty')
        test_2 = Team.objects.create(team_name='dsds')
        url = reverse('team_list')
        response = self.client.get(url)
        data = TeamSerializer([test_1, test_2], many=True).data
        expected_data = [
            {
                'id': test_1.id,
                'team_name': 'qwerty',
            },
            {
                'id': test_2.id,
                'team_name': 'dsds',
            }

        ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)


class BuyerSerializerTestCase(TestCase):
    def test_get_buyer_list(self):
        test_1 = Buyer.objects.create(buyer_name='qwerty')
        test_2 = Buyer.objects.create(buyer_name='dsds')
        url = reverse('buyer_list')
        response = self.client.get(url)
        data = BuyerSerializer([test_1, test_2], many=True).data
        expected_data = [
            {
                'id': test_1.id,
                'buyer_name': 'qwerty',
            },
            {
                'id': test_2.id,
                'buyer_name': 'dsds',
            }

        ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)


class DeviceTypeSerializerTestCase(TestCase):
    def test_get_devicetype_list(self):
        test_1 = DeviceType.objects.create(device_type='qwerty')
        test_2 = DeviceType.objects.create(device_type='dsds')
        url = reverse('devicetype_list')
        response = self.client.get(url)
        data = DeviceTypeSerializer([test_1, test_2], many=True).data
        expected_data = [
            {
                'id': test_1.id,
                'device_type': 'qwerty',
            },
            {
                'id': test_2.id,
                'device_type': 'dsds',
            }

        ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)


class DeviceSerializerTestCase(TestCase):
    def test_get_device_list(self):
        buyer = Buyer.objects.create(buyer_name='qwe')
        team = Team.objects.create(team_name='qwerty')
        devicetype = DeviceType.objects.create(device_type='asd')
        test_1 = Device.objects.create(
            device_name='qwerty',
            price=123,
            paid_by=buyer,
            team=team,
            configuration='http://127.0.0.1:51431/',
            device_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            device_type=devicetype,
        )
        test_2 = Device.objects.create(
            device_name='qwerty2',
            price=321,
            paid_by=buyer,
            team=team,
            configuration='http://127.0.0.1:514312/',
            device_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            device_type=devicetype,
        )
        url = reverse('devicetype_list')
        response = self.client.get(url)
        data = DeviceSerializer([test_1, test_2], many=True).data
        expected_data = [
            {
                'item_number': test_1.item_number,
                'device_name': 'qwerty',
                'price': 123,
                'purchase_date': str(datetime.date.today()),
                'paid_by': buyer.id,
                'team': team.id,
                'configuration': 'http://127.0.0.1:51431/',
                'device_photo': test_1.device_photo.url,
                'device_type': devicetype.id,
            },
            {
                'item_number': test_2.item_number,
                'device_name': 'qwerty2',
                'price': 321,
                'purchase_date': str(datetime.date.today()),
                'paid_by': buyer.id,
                'team': team.id,
                'configuration': 'http://127.0.0.1:514312/',
                'device_photo': test_2.device_photo.url,
                'device_type': devicetype.id,
            }

        ]

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)


class AssignmentSerializerTestCase(TestCase):
    def test_get_devicetype_list(self):
        user = User.objects.create(
            user_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            first_name='User3',
            last_name='Test3', )
        buyer = Buyer.objects.create(buyer_name='qweq')
        team = Team.objects.create(team_name='qwertyq')
        devicetype = DeviceType.objects.create(device_type='asdq')
        device = Device.objects.create(
            device_name='qwertyq',
            price=1232,
            paid_by=buyer,
            team=team,
            configuration='http://127.0.0.1:514312/',
            device_photo=SimpleUploadedFile(name='user.png', content=open('media/tmp/user.png', 'rb').read()),
            device_type=devicetype,
        )
        test_1 = Assignment.objects.create(
            user=user,
            device=device,
            comment='test comment',
            assignment_date=str(datetime.date.today()),

        )

        url = reverse('management:assignment_list')
        response = self.client.get(url)
        data = AssignmentSerializer(test_1).data
        expected_data = {
            'id': test_1.id,
            'user': user.id,
            'device': device.item_number,
            'comment': 'test comment',
            'assignment_date': str(datetime.date.today()),
        }
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, data)
