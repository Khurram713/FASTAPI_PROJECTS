from pydantic import BaseModel, ConfigDict, field_validator
import re

class StudentCreate(BaseModel):
    name: str
    age: int
    email: str
    CNIC: str

    @field_validator("CNIC")
    @classmethod
    def format_cnic(cls, v: str) -> str:
        # remove hyphens and spaces
        digits = re.sub(r"\D", "", v)

        if len(digits) != 13:
            raise ValueError("CNIC must contain exactly 13 digits")

        # auto format: #####-#######-#
        return f"{digits[:5]}-{digits[5:12]}-{digits[12]}"

class StudentResponse(StudentCreate):
    id : int

    model_config = ConfigDict(from_attributes=True)