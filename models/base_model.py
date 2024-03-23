from uuid import uuid4 as uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid())
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        self.updated_at = datetime.today().isoformat()

    def to_dict(self):
        return {**self.__dict__, "__class__": self.__class__.__name__}
