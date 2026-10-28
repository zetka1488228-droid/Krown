from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import database as db
import uvicorn

app = FastAPI()

# Разрешаем запросы с сайта
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/products")
def get_products():
    return db.get_products()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
