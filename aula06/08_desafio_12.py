# Escreva um programa que leia o arquivo "exemplo2.csv", e converta
# os registros desse CSV para o formato JSON. Escreva um arquivo de saída
# que contenha o conteúdo em JSON.    

import csv
import json

with open("exemplo2.csv", "r") as file:
    dictionary = csv.DictReader(file)
    students = []
    for line in dictionary:
        # This is a list of dictionaries
        students.append(line)

# The list of dicitionaries will be turned into a json format
students_json = json.dumps(students)

# Create a json file1 to write the json list of students
with open("students.json", "w") as file1:
    file1.write(students_json)
