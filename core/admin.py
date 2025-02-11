from django.contrib import admin
from .models import Customer, Product, Employee, TaskBoard

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')

@admin.register(TaskBoard)
class TaskBoardAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    list_filter = ('status', 'assigned_to')
