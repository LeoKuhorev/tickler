from django.urls import path


from .views import employee_list

urlpatterns = [
    # Employees list view
    path('', employee_list, name='employee-list'),
]
