#!/usr/bin/python3

from datetime import datetime
import uuid


class BaseModel:
    def __init__(self) -> None:
        self.id: uuid = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = datetime.now()

    def __str__(self) -> str:
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        upd_dict = {
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            '__class__': self.__class__.__name__,
        }
        return {**self.__dict__, **upd_dict}

