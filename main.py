import json

from fastapi import FastAPI, Query
from mongoengine import connect
from models import Employee
from mongoengine.queryset.visitor import Q

app = FastAPI()
connect(db="hrms", host="localhost", port=27017)


@app.get('/')
def get_hello():
    return {"msg": "Hello"}


@app.get('/search_employees')
def search_employees(name, age: int = Query(None, gt=18)):
    employees = json.loads(Employee.objects.filter(Q(name__icontains=name) | Q(age=age)).to_json())
    return {'employee': employees}
