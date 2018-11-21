#coding=utf-8
from jsonschema import validate
schema={"type":"object","properties":{"price":{"type":"number"},"name":{"type":"string"}}}

validate({"name" : "Eggs", "price" : 12},schema)