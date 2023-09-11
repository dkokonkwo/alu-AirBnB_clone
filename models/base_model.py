#!/usr/bin/python3

from datetime import datetime
from models import storage
import uuid


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        if len(kwargs) != 0:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    time = datetime.strptime(value, date_format)
                    setattr(self, key, time)
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id: uuid = str(uuid.uuid4())
            self.created_at: datetime = datetime.now()
            self.updated_at: datetime = datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        upd_dict = {
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            '__class__': self.__class__.__name__,
        }
        return {**self.__dict__, **upd_dict}
