from fastapi import FastAPI
from pydantic import BaseModel
import json

class Item(BaseModel):
    NIM: int
    Name: str

app = FastAPI()

@app.post('/student')
async def add_student(student: Item):
    with open("student.json", "r") as read_file:
        data = json.load(read_file)
    student_list = []
    new = {"NIM" : student.nim, "NAMA" : student.nama}

    student_list.append(student)
    return {"message": "Sucess"}

async def get_student():
    with open("student.json", "w") as outfile:
        json.dump(student_list, outfile)