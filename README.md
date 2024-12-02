# **Car Manager - Django Web Application**

Car Manager es una aplicación web construida con Django que permite gestionar información de vehículos y usuarios, con un sistema avanzado de roles y permisos. Incluye un diseño modular y responsivo basado en Bootstrap 5, y aprovecha las mejores prácticas de Django para la extensibilidad y el mantenimiento.

---

## **Características principales**
- **Gestión de Autos:**
  - Registro, visualización y edición de vehículos.
  - Permisos personalizados para acciones específicas como `edit_car`.
- **Sistema de Roles:**
  - Soporte para los roles: **Admin**, **Editor**, y **Viewer**.
  - Asignación dinámica de permisos durante el registro.
- **Autenticación:**
  - Registro, login y logout de usuarios.
  - Redirecciones configurables después del login/logout.
- **Interfaz modular y profesional:**
  - Uso de `base.html` para un diseño uniforme.
  - Componentes reutilizables (`header`, `footer`, `sidebar`) integrados como `include`.
- **Estilo responsivo:**
  - Diseñado con Bootstrap 5 para una experiencia fluida en dispositivos móviles y de escritorio.

---

## **Tecnologías utilizadas**
### **Backend:**
- Python 3.x
- Django 4.x
- Django ORM para la interacción con la base de datos.

### **Frontend:**
- HTML5, CSS3
- Bootstrap 5.3
- JavaScript (para interactividad básica).

### **Base de datos:**
- SQLite (por defecto, fácilmente reemplazable por PostgreSQL o MySQL).

---

## **Requisitos previos**
- Python 3.x instalado.
- Entorno virtual como `venv` o `pipenv`.
- Django instalado (ver instrucciones de instalación).
- Node.js (opcional, para tareas avanzadas de frontend).

---

## **Instalación**

### **1. Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/car-manager.git
cd car-manager
```

### **2. Crear y activar un entorno virtual**
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### **3. Instalar dependencias**
```bash
pip install -r requirements.txt
```

### **4. Realizar migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Crear un superusuario**
```bash
python manage.py createsuperuser
```

### **6. Iniciar el servidor de desarrollo**
```bash
python manage.py runserver
```

### **7. Acceder a la aplicación**
Visita: `http://127.0.0.1:8000/`

---

## **Estructura del proyecto**

```
car-manager/
├── auth_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── auth_app/
│   │   │   ├── base.html
│   │   │   ├── includes/
│   │   │   │   ├── header.html
│   │   │   │   ├── footer.html
│   │   │   │   └── sidebar.html
│   │   │   ├── dashboard.html
│   │   │   ├── edit_car.html
│   │   │   ├── login.html
│   │   │   └── register.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── requirements.txt
├── README.md
└── db.sqlite3
```

---

## **Flujo del usuario**

1. **Registro:** Los usuarios pueden registrarse y seleccionar un rol (Admin, Editor, Viewer).
2. **Login:** Después de iniciar sesión, los usuarios son redirigidos al Dashboard.
3. **Gestión de Autos:**
   - Visualización de todos los autos.
   - Edición de autos (requiere permiso `edit_car`).
4. **Logout:** Los usuarios son redirigidos a la página de login tras cerrar sesión.

---

## **Extensibilidad**
- **Agregar más permisos:**
  En el modelo `Car`, puedes definir nuevos permisos:
  ```python
  class Meta:
      permissions = [
          ('delete_car', 'Can delete car'),
      ]
  ```
  Ejecuta migraciones para aplicarlos:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

- **Diseño personalizable:**
  Modifica `base.html` o los componentes en `includes` para adaptarlos a tus necesidades.

---

## **Contribuir**
1. Haz un fork del repositorio.
2. Crea una rama para tus cambios:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
3. Realiza tus cambios y súbelos:
   ```bash
   git commit -m "Agregué nueva funcionalidad"
   git push origin feature/nueva-funcionalidad
   ```
4. Abre un Pull Request.

---

## **Licencia**
Este proyecto está licenciado bajo la [MIT License](LICENSE).
