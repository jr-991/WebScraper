from fastapi import FastAPI

app = FastAPI(title="Real Estate API", description="API for managing real estate listings", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "The Real Estate API is running"}