from rest_framework.viewsets import ModelViewSet
from .models import Customer, Product, Employee, TaskBoard
from .serializers import CustomerSerializer, ProductSerializer, EmployeeSerializer, TaskBoardSerializer

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TaskBoardViewSet(ModelViewSet):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer

    def get_queryset(self):
        status = self.request.query_params.get('status')
        employee_id = self.request.query_params.get('assigned_to')
        queryset = super().get_queryset()
        if status:
            queryset = queryset.filter(status=status)
        if employee_id:
            queryset = queryset.filter(assigned_to_id=employee_id)
        return queryset
