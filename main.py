from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Usuario(BaseModel):
    nome: str

dados = [
    {"id": 1, "nome": "Henrique"},
    {"id": 2, "nome": "Maria"}
]

@app.get("/usuarios")
def listar_usuarios():
    return dados

@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    novo = {"id": len(dados) + 1, "nome": usuario.nome}
    dados.append(novo)
    return novo

@app.get("/usuarios/{id}")
def obter_usuario(id: int):
    usuario = next((u for u in dados if u["id"] == id), None)
    if usuario:
        return usuario
    raise HTTPException(status_code=404, detail="Usuário não encontrado")