from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from management.views import AssignmentListView, UserListView, DeviceListView, UserDeviceListView, SearchResultsView, \
    DeviceDetailView, UserDetailView, UserCreateView, DeviceCreateView, TeamCreateView, BuyerCreateView, \
    DeviceTypeCreateView, AssignmentCreateView, UserUpdateView, DeviceUpdateView, BuyerUpdateView, AssignmentUpdateView, \
    TeamUpdateView, DeviceTypeUpdateView, UserDeleteView, AssignmentDeleteView, DeviceDeleteView, TeamDeleteView, \
    DeviceTypeDeleteView, BuyerDeleteView, TeamListView, BuyerListView, DeviceTypeListView

urlpatterns = [
    url(r'^$', AssignmentListView.as_view(), name='assignment_list'),
    url(r'user-list$', UserListView.as_view(), name='user_list'),
    url(r'user-devices-list/(?P<pk>[0-9]+)/$', UserDeviceListView.as_view(), name='user_devices_list'),
    url(r'device-list$', DeviceListView.as_view(), name='device_list'),
    url(r'team-list$', TeamListView.as_view(), name='team_list'),
    url(r'buyer-list$', BuyerListView.as_view(), name='buyer_list'),
    url(r'devicetype-list$', DeviceTypeListView.as_view(), name='devicetype_list'),

    url(r'user-detail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'device-detail/(?P<pk>[0-9]+)/$', DeviceDetailView.as_view(), name='device_detail'),

    url(r'user-create$', UserCreateView.as_view(), name='user-create'),
    url(r'device-create$', DeviceCreateView.as_view(), name='device-create'),
    url(r'team-create$', TeamCreateView.as_view(), name='team-create'),
    url(r'buyer-create$', BuyerCreateView.as_view(), name='buyer-create'),
    url(r'devicetype-create$', DeviceTypeCreateView.as_view(), name='devicetype-create'),
    url(r'assignment-create$', AssignmentCreateView.as_view(), name='assignment-create'),

    url(r'user-update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name='user-update'),
    url(r'device-update/(?P<pk>[0-9]+)/$', DeviceUpdateView.as_view(), name='device-update'),
    url(r'team-update/(?P<pk>[0-9]+)/$', TeamUpdateView.as_view(), name='team-update'),
    url(r'buyer-update/(?P<pk>[0-9]+)/$', BuyerUpdateView.as_view(), name='buyer-update'),
    url(r'devicetype-update/(?P<pk>[0-9]+)/$', DeviceTypeUpdateView.as_view(), name='devicetype-update'),
    url(r'assignment-update/(?P<pk>[0-9]+)/$', AssignmentUpdateView.as_view(), name='assignment-update'),

    url(r'user-delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(success_url="user-list"), name='user-delete'),
    url(r'device-delete/(?P<pk>[0-9]+)/$', DeviceDeleteView.as_view(success_url="device-list"), name='device-delete'),
    url(r'team-delete/(?P<pk>[0-9]+)/$', TeamDeleteView.as_view(success_url="team-list"), name='team-delete'),
    url(r'buyer-delete/(?P<pk>[0-9]+)/$', BuyerDeleteView.as_view(success_url="buyer-list"), name='buyer-delete'),
    url(r'devicetype-delete/(?P<pk>[0-9]+)/$', DeviceTypeDeleteView.as_view(success_url="devicetype-list"), name='devicetype-delete'),
    url(r'assignment-delete/(?P<pk>[0-9]+)/$', AssignmentDeleteView.as_view(success_url="/"), name='assignment-delete'),

    url(r'search-results$', SearchResultsView.as_view(), name='search-results'),
    ]
