

from API import obtener_datos
from UI import solicitar_datos_usuario, mostrar_resultados  # Importa desde UI/__init__.py

def main():
    nombre_departamento, limite_registros = solicitar_datos_usuario()
    
    datos_df = obtener_datos(nombre_departamento, limite_registros)
    
    if datos_df.empty:
        print("No se encontraron datos. Saliendo del programa.")
    else:
        mostrar_resultados(datos_df)

if __name__ == "__main__":
    main()





