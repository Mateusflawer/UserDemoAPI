from fastapi import FastAPI
from app.routes import user
from app.core.database import engine
from app.models import user as user_model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="UserDemoAPI", version="1.0.0")

# Configuração de CORS (ajuste conforme necessário)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cria as tabelas no banco de dados
user_model.Base.metadata.create_all(bind=engine)

# Inclui as rotas
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the User Authentication API"}
