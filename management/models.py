from django.db import models
from django.urls import reverse


class User(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    user_photo = models.ImageField('User Photo', upload_to='user_photos/')
    employee_date = models.DateField('Employee date', auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('user_detail', args=[self.id])

    def get_user_devices_list(self):
        return reverse('user_devices_list', args=[self.id])


class Buyer(models.Model):
    buyer_name = models.CharField('Buyer Name', max_length=50, unique=True)

    def __str__(self):
        return self.buyer_name

    @staticmethod
    def get_absolute_url():
        return reverse('buyer_list')


class Team(models.Model):
    team_name = models.CharField('Team Name', max_length=50, unique=True)

    def __str__(self):
        return self.team_name

    @staticmethod
    def get_absolute_url():
        return reverse('team_list')


class DeviceType(models.Model):
    device_type = models.CharField('Device type', max_length=50, unique=True)

    def __str__(self):
        return self.device_type

    @staticmethod
    def get_absolute_url():
        return reverse('devicetype_list')


class Device(models.Model):
    item_number = models.AutoField('Item number', primary_key=True)
    device_name = models.CharField('Device Name', max_length=50)
    price = models.IntegerField('Price')
    purchase_date = models.DateField('Purchase_date', auto_now=True)
    paid_by = models.ForeignKey(Buyer, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    configuration = models.URLField('URL for configuration')
    device_photo = models.ImageField('Device Photo', upload_to='device_photos/')
    device_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT)

    def __str__(self):
        return self.device_name

    def get_absolute_url(self):
        return reverse('device_detail', args=[self.item_number])

    def is_busy(self):
        check = Assignment.objects.filter(device_id=self.item_number)
        return check


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    device = models.OneToOneField(Device, on_delete=models.PROTECT)
    comment = models.TextField('Comment')
    assignment_date = models.DateField('Assignment date', auto_now=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

    @staticmethod
    def get_absolute_url():
        return reverse('assignment_list')
