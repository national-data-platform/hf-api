from sqlmodel import SQLModel, Field
from typing import Optional, List, Dict, Literal
from datetime import datetime

class ModelData(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    modelId: str
    created_at: Optional[datetime]
    private: bool
    downloads: int
    library_name: Optional[str]
    tags: List[str]