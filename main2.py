from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, constr
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, Session

# Banco de dados (SQLite para exemplo)
DATABASE_URL = "sqlite:///./usuarios.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Modelo do banco de dados
class UsuarioDB(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)

# Criar a tabela
Base.metadata.create_all(bind=engine)

# Pydantic model (entrada e saída)
class UsuarioCreate(BaseModel):
    nome: constr(min_length=1, max_length=50)

class UsuarioOut(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True

# FastAPI app
app = FastAPI()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas
@app.get("/usuarios", response_model=list[UsuarioOut])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(UsuarioDB).all()

@app.post("/usuarios", response_model=UsuarioOut)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = UsuarioDB(nome=usuario.nome)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.get("/usuarios/{id}", response_model=UsuarioOut)
def obter_usuario(id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioDB).filter(UsuarioDB.id == id).first()
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
