from fastapi import FastAPI, Query
import json

app= FastAPI()

with open('../bddatos.json', 'r') as file:
    datos = json.load(file)

@app.get('/datos')
def index(
    ciudad: str = Query(None, title="Ciudad"),
    sexo: str = Query(None, title="Sexo"),
    nivel_educativo: str = Query(None, title="Nivel Educativo")
):
    resultados_filtrados = datos
    if ciudad:
        resultados_filtrados = [dato for dato in resultados_filtrados if dato['ciudad'] == ciudad]
    if sexo:
        resultados_filtrados = [dato for dato in resultados_filtrados if dato['sexo'] == sexo]
    if nivel_educativo:
        resultados_filtrados = [dato for dato in resultados_filtrados if dato['nivel_educativo'] == nivel_educativo]

    return resultados_filtrados
    

