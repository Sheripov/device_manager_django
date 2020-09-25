from rest_framework.serializers import ModelSerializer

from management.models import User, Team, Buyer, DeviceType, Device, Assignment


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'user_photo', 'employee_date']


class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'team_name']


class BuyerSerializer(ModelSerializer):
    class Meta:
        model = Buyer
        fields = ['id', 'buyer_name']


class DeviceTypeSerializer(ModelSerializer):
    class Meta:
        model = DeviceType
        fields = ['device_type', 'id']


class DeviceSerializer(ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'item_number',
            'device_name',
            'price',
            'purchase_date',
            'paid_by',
            'team',
            'configuration',
            'device_photo',
            'device_type',
        ]


class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            'user',
            'device',
            'comment',
            'assignment_date',
            'id',
        ]
