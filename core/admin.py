from django.contrib import admin
from .models import Customer, Product, Employee, TaskBoard


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'address', 'phone')  
    search_fields = ('name', 'email', 'address''phone')  
    list_filter = ('address',)  


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_pro', 'price')  
    search_fields = ('name', 'type_pro')  
    list_filter = ('type_pro',)  


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'email')  
    search_fields = ('name', 'position', 'email') 
    list_filter = ('position',)  

class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assigned_to') 
    search_fields = ('title', 'assigned_to__name', 'status')  
    list_filter = ('status', 'assigned_to')  

# Đăng ký các mô hình vào admin
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TaskBoard, TaskBoardAdmin)
