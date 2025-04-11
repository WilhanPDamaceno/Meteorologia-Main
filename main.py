from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from weatherModel import SessionLocal, WeatherData
from fastapi.responses import HTMLResponse

app = FastAPI()

# Modelo de entrada para a API
class WeatherRequest(BaseModel):
    temperature: str

# Função para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota raiz com HTML simples
@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <html>
        <head>
            <title>Teste da api</title>
        </head>
        <body>
            <h1>Dá um beijo na careca do professor para mim S2</h1>
        </body>
    </html>
    """

# Rota para adicionar dados com documentação melhorada
@app.post("/weather/", response_model=WeatherRequest, summary="Adiciona dados meteorológicos")
def add_weather(data: WeatherRequest, db: Session = Depends(get_db)):
    """
    Adiciona informações meteorológicas no banco de dados.

    - **city**: Nome da cidade  
    - **temperature**: Temperatura registrada  
    """
    
    weather = WeatherData(temperature=data.temperature)
    db.add(weather)
    db.commit()
    db.refresh(weather)
    return data
    

# Rota para obter todos os registros
@app.get("/weather/", summary="Retorna todas as cidades registradas")
def get_weather(db: Session = Depends(get_db)):
    """Retorna uma lista com todas as cidades e suas temperaturas armazenadas no banco."""
    return db.query(WeatherData).all()
