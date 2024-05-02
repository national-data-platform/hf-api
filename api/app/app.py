from fastapi import FastAPI
from app.db import create_db_and_tables, init_db, engine
from app.models import ModelData
from sqlmodel import Session, select


#if these change, need to change the nginx files
sensordata_kml_filename= 'sensordata.kml'

app = FastAPI()

@app.on_event("startup")
def on_starup():
    create_db_and_tables()
    init_db()

@app.get("/")
async def main():
    return {"NDP Huggingface API"}

@app.get("/v1/models")
def get_model_data():
    with Session(engine) as session:
        model_data = session.exec(select(ModelData)).all()
        return model_data