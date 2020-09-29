from django.conf.urls import url
from django.urls import re_path

from management.views import AssignmentListView, UserListView, DeviceListView, UserDeviceListView, SearchResultsView, \
    DeviceDetailView, UserDetailView, UserCreateView, DeviceCreateView, TeamCreateView, BuyerCreateView, \
    DeviceTypeCreateView, AssignmentCreateView, UserUpdateView, DeviceUpdateView, BuyerUpdateView, AssignmentUpdateView, \
    TeamUpdateView, DeviceTypeUpdateView, UserDeleteView, AssignmentDeleteView, DeviceDeleteView, TeamDeleteView, \
    DeviceTypeDeleteView, BuyerDeleteView, TeamListView, BuyerListView, DeviceTypeListView

app_name = 'management'

urlpatterns = (
    re_path(r'^$', AssignmentListView.as_view(), name='assignment_list'),
    url(r'user_list$', UserListView.as_view(), name='user_list'),
    url(r'user_devices_list/(?P<pk>[0-9]+)/$', UserDeviceListView.as_view(), name='user_devices_list'),
    url(r'device_list$', DeviceListView.as_view(), name='device_list'),
    url(r'team_list$', TeamListView.as_view(), name='team_list'),
    url(r'buyer_list$', BuyerListView.as_view(), name='buyer_list'),
    url(r'devicetype_list$', DeviceTypeListView.as_view(), name='devicetype_list'),

    url(r'user_detail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user_detail'),
    url(r'device_detail/(?P<pk>[0-9]+)/$', DeviceDetailView.as_view(), name='device_detail'),

    url(r'user_create$', UserCreateView.as_view(), name='user_create'),
    url(r'device_create$', DeviceCreateView.as_view(), name='device_create'),
    url(r'team_create$', TeamCreateView.as_view(), name='team_create'),
    url(r'buyer_create$', BuyerCreateView.as_view(), name='buyer_create'),
    url(r'devicetype_create$', DeviceTypeCreateView.as_view(), name='devicetype_create'),
    url(r'assignment_create$', AssignmentCreateView.as_view(), name='assignment_create'),

    url(r'user_update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name='user_update'),
    url(r'device_update/(?P<pk>[0-9]+)/$', DeviceUpdateView.as_view(), name='device_update'),
    url(r'team_update/(?P<pk>[0-9]+)/$', TeamUpdateView.as_view(), name='team_update'),
    url(r'buyer_update/(?P<pk>[0-9]+)/$', BuyerUpdateView.as_view(), name='buyer_update'),
    url(r'devicetype_update/(?P<pk>[0-9]+)/$', DeviceTypeUpdateView.as_view(), name='devicetype_update'),
    url(r'assignment_update/(?P<pk>[0-9]+)/$', AssignmentUpdateView.as_view(), name='assignment_update'),

    url(r'user_delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(success_url="management:user_list"),
        name='user_delete'),
    url(r'device_delete/(?P<pk>[0-9]+)/$', DeviceDeleteView.as_view(success_url="management:device_list"),
        name='device_delete'),
    url(r'team_delete/(?P<pk>[0-9]+)/$', TeamDeleteView.as_view(success_url="management:team_list"),
        name='team_delete'),
    url(r'buyer_delete/(?P<pk>[0-9]+)/$', BuyerDeleteView.as_view(success_url="management:buyer_list"),
        name='buyer_delete'),
    url(r'devicetype_delete/(?P<pk>[0-9]+)/$', DeviceTypeDeleteView.as_view(success_url="management:devicetype_list"),
        name='devicetype_delete'),
    url(r'assignment_delete/(?P<pk>[0-9]+)/$', AssignmentDeleteView.as_view(success_url="/"), name='assignment_delete'),

    url(r'search_results$', SearchResultsView.as_view(), name='search_results'),
)
