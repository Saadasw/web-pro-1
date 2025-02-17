from fastapi import FastAPI
from app.api.v1 import auth, employees, services, projects

app = FastAPI()

# Include API routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(services.router, prefix="/services", tags=["Services"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])

@app.get("/")
def root():
    return {"message": "Welcome to our FastAPI App!"}
