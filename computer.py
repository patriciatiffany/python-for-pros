from pydantic import BaseModel


class Computer(BaseModel):
    brand: str
    ram_gb: int
    hard_drive_gb: int


laptop = Computer(brand="apple", ram_gb=16, hard_drive_gb=512)
print(laptop)
