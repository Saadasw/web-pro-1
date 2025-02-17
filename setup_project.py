import os

folders = [
    "app/api/v1", "app/models", "app/schemas", "app/services", "app/core",
    "tests", "migrations"
]
files = {
    "app/api/v1": ["auth.py", "employees.py", "services.py", "projects.py", "__init__.py"],
    "app/models": ["user.py", "employee.py", "service.py", "__init__.py"],
    "app/schemas": ["user.py", "employee.py", "service.py", "__init__.py"],
    "app/services": ["auth_service.py", "employee_service.py", "__init__.py"],
    "app/core": ["config.py", "security.py", "database.py", "__init__.py"],
    "tests": ["test_auth.py", "test_employee.py", "__init__.py"],
    "app": ["main.py"],
    "": [".env", "requirements.txt", "README.md"]
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for folder, file_list in files.items():
    for file in file_list:
        open(os.path.join(folder, file), 'w').close()

print("✅ FastAPI project structure created!")
