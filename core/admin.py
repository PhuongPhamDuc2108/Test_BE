from django.contrib import admin
from .models import Customer, Product, Employee, TaskBoard

# Tùy chỉnh giao diện quản trị cho Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')  # Hiển thị các trường này trong danh sách
    search_fields = ('name', 'email', 'phone')  # Tìm kiếm theo các trường này
    list_filter = ('name',)  # Lọc dữ liệu theo tên (có thể thêm các trường khác)

# Tùy chỉnh giao diện quản trị cho Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type_pro', 'price')  # Hiển thị các trường này trong danh sách
    search_fields = ('name', 'type_pro')  # Tìm kiếm theo tên sản phẩm và loại sản phẩm
    list_filter = ('type_pro',)  # Lọc theo loại sản phẩm (phone, laptop, pc)

# Tùy chỉnh giao diện quản trị cho Employee
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position', 'email')  # Hiển thị các trường này trong danh sách
    search_fields = ('name', 'position', 'email')  # Tìm kiếm theo tên, chức vụ và email
    list_filter = ('position',)  # Lọc theo chức vụ nhân sự

# Tùy chỉnh giao diện quản trị cho TaskBoard
class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'assigned_to')  # Hiển thị các trường này trong danh sách
    search_fields = ('title', 'assigned_to__name', 'status')  # Tìm kiếm theo tên công việc, nhân sự và trạng thái
    list_filter = ('status', 'assigned_to')  # Lọc theo trạng thái và nhân sự phân công

# Đăng ký các mô hình vào admin
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TaskBoard, TaskBoardAdmin)
