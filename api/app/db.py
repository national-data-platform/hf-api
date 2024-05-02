from app.etl import get_models
import os
import time
from app.models import ModelData
from sqlmodel import SQLModel, create_engine, Session, select
from sqlalchemy_utils.functions import database_exists, create_database

APIDB_URL = os.environ.get("APIDB_URL")

engine = create_engine(APIDB_URL, echo=True)

def create_db_and_tables():
    found = False
    tries = 10
    while tries > 0:
        try:
            print(APIDB_URL)
            print('checking if db exists, try', tries, flush=True)
            if database_exists(APIDB_URL):
                found = True
                print('found db', flush=True)
                break
            else:
                print('attempting to create.', flush=True)
                create_database(APIDB_URL)
        except Exception as e:
            print(e)
            time.sleep(2)

        tries -= 1

    if not found:
        raise ValueError('Unable to create database')

    SQLModel.metadata.create_all(engine)

def init_db():
    print('Checking if model data is empty',flush=True)
    with Session(engine) as session:
        model_data = session.exec(select(ModelData)).all()
    num_records = len(model_data)
    print(f'ModelData table has {num_records} records',flush=True)
    if num_records == 0:
        print('Initializing database with Huggingface model data', flush=True)
        try:
            model_data = get_models()
            with Session(engine) as session:
                for iModel in model_data:
                    session.add(ModelData(**iModel))
                session.commit()
            print(f'Uploading {len(model_data)} records', flush=True)
        except:
            print('Error with uploading huggingface model data', flush=True)