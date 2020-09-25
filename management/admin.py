from django.contrib import admin

from management.models import User, Device, Team, Buyer, Assignment, DeviceType


class AssignmentDateAdmin(admin.ModelAdmin):
    readonly_fields = ('assignment_date',)


class PurchaseDateAdmin(admin.ModelAdmin):
    readonly_fields = ('purchase_date',)


class EmployeeDateAdmin(admin.ModelAdmin):
    readonly_fields = ('employee_date',)


admin.site.register(User, EmployeeDateAdmin)
admin.site.register(Device, PurchaseDateAdmin)
admin.site.register(Team)
admin.site.register(Buyer)
admin.site.register(DeviceType)
admin.site.register(Assignment, AssignmentDateAdmin)
