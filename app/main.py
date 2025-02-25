import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from app.db import create_db_and_tables

from app.task import routers as Task
from app.product import routers as Product
from app.category import routers as Category
from app.brand import routers as Brand
from app.customer import routers as Customer

# Creación correcta de la app (una sola instancia)
app = FastAPI(
    lifespan=create_db_and_tables,
    title="AppTransactionFastAPI",
    description="API de un Sistema de tareas y productos, usando FastApi con Python.",
    version="v1",
    license_info={"name": "MIT License", "url": "https://opensource.org/license/mit"},
    contact={
        "name": "Henry Douglas Chavarria Zurita",
        "url": "https://github.com/Douglashc/fastapi_product",
        "email": "douglash.dcz@gmail.com",
    },
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://douglashc.github.io"],  # Agrega el dominio de Render
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos
    allow_headers=["*"],  # Permite todos los headers
)

# Incluir routers
app.include_router(Task.router, prefix="/tasks", tags=["Tasks"])
app.include_router(Product.router, prefix="/products", tags=["Products"])
app.include_router(Category.router, prefix="/categories", tags=["Categories"])
app.include_router(Brand.router, prefix="/brands", tags=["Brands"])
app.include_router(Customer.router, prefix="/customers", tags=["Customers"])

@app.get("/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Bienvenido</title>
        </head>
        <body>
            <h1>API con FastAPI!</h1>
        </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
