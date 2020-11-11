from django.contrib import admin

from .models import Address, Employee, Expirations


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_one', 'address_two', 'city', 'state', 'zip_code')
    search_fields = ('address_one', 'zip_code')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email',
                    'phone_number', 'address', 'role', 'manager')


@admin.register(Expirations)
class ExpirationsAdmin(admin.ModelAdmin):
    list_display = ('dl_exp', 'ins_exp', 'background_exp',
                    'annual_paperwork_exp', 'employee', )
