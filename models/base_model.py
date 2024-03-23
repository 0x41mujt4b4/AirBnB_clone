from uuid import uuid4 as uuid
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        # if kwargs is not None:
        #    for key, value in kwargs.iteritems():
        #        pass
        self.id = str(uuid())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    @property
    def _created_at(self):
        return self.created_at.isoformat()

    @_created_at.setter
    def _created_at(self, value):
        self.created_at = value

    @property
    def _updated_at(self):
        return self.updated_at.isoformat()

    @_updated_at.setter
    def _updated_at(self, value):
        self.updated_at = value

    def __str__(self):
        return f"[{self.__class__.__name__} ({self.id}) {self.__dict__}]"

    def save(self):
        self.updated_at = datetime.today()

    def to_dict(self):
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self._created_at
        dict_copy["updated_at"] = self._updated_at
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
