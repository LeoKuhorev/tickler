from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def employee_list(request):
    user = request.user
    employees = Employee.objects.filter(manager=user)
    if len(employees) > 0:
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_200_OK)
