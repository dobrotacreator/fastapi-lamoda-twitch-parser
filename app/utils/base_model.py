from datetime import datetime

from pydantic import BaseModel, field_validator


class BaseWithTimeModel(BaseModel):
    created_at: datetime = None

    @field_validator('created_at', mode="before")
    def val_created_at(cls, value):
        if isinstance(value, str):
            try:
                return datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValueError('Invalid datetime format. Please use the format "YYYY-MM-DD HH:MM:SS".')
        return value
