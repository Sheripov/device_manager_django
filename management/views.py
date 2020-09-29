from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Q, ProtectedError
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from management.models import Assignment, User, Device, Team, Buyer, DeviceType


# Create Views
class UserCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = User
    fields = ['first_name', 'last_name', 'user_photo']
    template_name = 'management/user/user_create.html'


class DeviceTypeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = DeviceType
    fields = ['device_type']
    template_name = 'management/device/devicetype_create.html'


class TeamCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Team
    fields = ['team_name']
    template_name = 'management/team/team_create.html'


class BuyerCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Buyer
    fields = ['buyer_name']
    template_name = 'management/buyer/buyer_create.html'


class DeviceCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Device
    fields = ['device_name', 'price', 'paid_by', 'team', 'configuration', 'device_type', 'device_photo']
    template_name = 'management/device/device_create.html'


class AssignmentCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'polls.can_add'
    model = Assignment
    fields = ['user', 'device', 'comment']
    template_name = 'management/assignment/assignment_create.html'


# Update Views
class AssignmentUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_edit'
    model = Assignment
    fields = ['user', 'device', 'comment']
    template_name = 'management/assignment/assignment_create.html'


class BuyerUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_add'
    model = Buyer
    fields = ['buyer_name']
    template_name = 'management/buyer/buyer_create.html'


class UserUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_add'
    model = User
    fields = ['first_name', 'last_name', 'user_photo']
    template_name = 'management/user/user_create.html'


class DeviceUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_add'
    model = Device
    fields = ['device_name', 'price', 'paid_by', 'team', 'configuration', 'device_type', 'device_photo']
    template_name = 'management/device/device_create.html'


class TeamUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_add'
    model = Team
    fields = ['team_name']
    template_name = 'management/team/team_create.html'


class DeviceTypeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'polls.can_add'
    model = DeviceType
    fields = ['device_type']
    template_name = 'management/device/devicetype_create.html'


# Delete Views
class AssignmentDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Assignment
    template_name = 'management/confirm_delete.html'


class UserDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = User
    template_name = 'management/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'management/confirm_delete.html', {'Protected_Error': 'Protected_Error'})


class DeviceDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Device
    template_name = 'management/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'management/confirm_delete.html', {'Protected_Error': 'Protected_Error'})


class TeamDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Team
    template_name = 'management/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'management/confirm_delete.html', {'Protected_Error': 'Protected_Error'})


class DeviceTypeDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = DeviceType
    template_name = 'management/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'management/confirm_delete.html', {'Protected_Error': 'Protected_Error'})


class BuyerDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'polls.can_delete'
    model = Buyer
    template_name = 'management/confirm_delete.html'

    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            return render(request, 'management/confirm_delete.html', {'Protected_Error': 'Protected_Error'})


# List Views
class AssignmentListView(ListView):
    model = Assignment
    context_object_name = 'assignment_list_data'
    queryset = Assignment.objects.order_by('assignment_date')
    template_name = 'management/assignment/assignment_list.html'


class UserListView(ListView):
    model = User
    context_object_name = 'user_list_data'
    queryset = User.objects.order_by('employee_date')
    template_name = 'management/user/user_list.html'


class UserDeviceListView(ListView):
    model = Assignment
    context_object_name = 'user_devices'
    template_name = 'management/user/user_device_list.html'

    def get_queryset(self):
        return Assignment.objects.filter(user_id=self.kwargs['pk'])


class DeviceListView(ListView):
    model = Device
    context_object_name = 'device_list'
    queryset = Device.objects.order_by('purchase_date')
    template_name = 'management/device/device_list.html'


class TeamListView(ListView):
    model = Team
    context_object_name = 'team_list'
    template_name = 'management/team/team_list.html'


class BuyerListView(ListView):
    model = Buyer
    context_object_name = 'buyer_list'
    template_name = 'management/buyer/buyer_list.html'


class DeviceTypeListView(ListView):
    model = DeviceType
    context_object_name = 'devicetype_list'
    template_name = 'management/device/devicetype_list.html'


# Detail Views
class UserDetailView(DetailView):
    model = User
    context_object_name = 'user_detail'
    template_name = 'management/user/user_detail.html'


class DeviceDetailView(DetailView):
    model = Device
    context_object_name = 'device_detail'
    template_name = 'management/device/device_detail.html'


# Search Views
class SearchResultsView(ListView):
    model = Device
    template_name = 'management/device/device_list.html'
    context_object_name = 'device_list'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        object_list = Device.objects.filter(
            Q(device_name__icontains=query) | Q(device_name__icontains=query)
        )
        return object_list
