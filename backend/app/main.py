from fastapi import FastAPI
from app.api.routes.fields import router as fields_router


app = FastAPI(
    title="AgroHydro DSS",
    description="AI-based Decision Support System for Smart Water and Agriculture Management",
    version="1.0.0"
)


app.include_router(fields_router)


@app.get("/")
def root():
    return {
        "message": "AgroHydro DSS API is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }