from datetime import datetime
from pydantic import BaseModel, ConfigDict, field

# модель данных заявок

class User(BaseModel):
    id: int
    name: str
    age: int = field(gt=0, lt=150) #todo conint чем отличается от этого
    email: str
    password: str
    sum: int = field(gt=0, lt=150000)
    srok: datetime = field(gt=0, lt=datetime(year=2020, month=1, day=1)) #todo faaah
    is_active: bool = False # типа базово она не принята

    income: float


# валидация
# 1. имейл?
# 2. пароль

