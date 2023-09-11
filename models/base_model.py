#!/usr/bin/python3

from datetime import datetime
# from models import storage
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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # storage.new(self)

    def __str__(self) -> str:
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        self.updated_at = datetime.now()
        # storage.save()

    def to_dict(self):
        upd_dict = {
            'created_at': self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            '__class__': self.__class__.__name__,
        }
        return {**self.__dict__, **upd_dict}


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))