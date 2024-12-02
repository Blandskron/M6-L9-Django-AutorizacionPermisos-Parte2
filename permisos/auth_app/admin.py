from django.contrib import admin
from .models import CustomUser, Car

# Configuración personalizada para el modelo CustomUser
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')  # Muestra campos clave en la lista
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')  # Filtros para facilitar la navegación
    search_fields = ('username', 'email', 'first_name', 'last_name')  # Campos para búsqueda rápida
    ordering = ('username',)  # Orden predeterminado por nombre de usuario
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Roles', {'fields': ('role',)}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined')}),
    )

# Configuración personalizada para el modelo Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year')  # Muestra los campos clave en la lista
    search_fields = ('model',)  # Permite buscar por el modelo
    ordering = ('year',)  # Ordena por año
