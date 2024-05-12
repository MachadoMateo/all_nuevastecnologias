import pandas as pd
import random

nombres = ["Alejandro", "Valeria", "Gabriel", "Isabel", "Sergio", "Diego", "Daniel", "Carolina", "Héctor", "Julieta"]
apellidos = ["Ramírez", "Castillo", "Medina", "Vargas", "Herrera", "Jiménez", "Gómez", "Rojas", "Fuentes", "Santana"]
asignaturas = ["Matemáticas", "Historia", "Ciencias", "Literatura", "Física", "Química", "Geografía", "Biología", "Inglés", "Economía"]


# Generar datos ficticios
datos = []
for _ in range(100):
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    asignatura = random.choice(asignaturas)
    nota = random.randint(60, 100)  # Nota aleatoria entre 60 y 100
    datos.append([nombre, apellido, asignatura, nota])

# Crear DataFrame con los datos
df = pd.DataFrame(datos, columns=["Nombre", "Apellido", "Asignatura", "Nota"])

# Guardar DataFrame en un archivo CSV
df.to_csv("datos_estudiantes.csv", index=False)

print("Archivo CSV generado exitosamente.")
df

df.to_csv("datos.csv", index=False)
df

df[ (df['Nota'] < 80) & (df['Asignatura'] == 'Economía') ][['Nombre', 'Apellido', 'Asignatura']]