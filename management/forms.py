from django.forms import ModelForm

from management.models import Assignment, User, Device, Team


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = ['user', 'device', 'assignment_date', 'comment']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'user_photo']


class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['device_name', 'price', 'paid_by', 'team', 'configuration', 'device_type', 'device_photo']


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['team_name']


class BuyerForm(ModelForm):
    class Meta:
        model = Team
        fields = ['buyer_name']
