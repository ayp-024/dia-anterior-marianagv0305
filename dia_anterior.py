"""
Codifica tu solución en este archivo.
"""
"""
Tarea:    Siguiente día
Autor:    Mariana García Vera
Fecha:    4/nov/2024
Grupo:    ESI-232
Profesor: Jorge A. Zaldívar Carrillo
Descripción: Día Anterior
"""

# Declaraciones
def es_bisiesto(anho):
  " Determina si un año es bisiesto"
  if (anho % 400 == 0
      or anho % 4 == 0 and anho % 100 != 0
     ):
      return True
  else:
    return False


def dias_mes (mes, anho):
  "Calcula el número de días que tiene un mes"
  if mes in [1,3,5,7,8,10,12]:
    dias_mes = 31
  elif mes in [4,6,9,11]:
    dias_mes = 30
  else:
    if es_bisiesto(anho):
      dias_mes = 29
    else:
      dias_mes = 28
  return dias_mes

# Programa principal
def main():
    # Entradas
    dia = int(input("Día: "))
    mes = int(input("Mes: "))
    anho = int(input("Año: "))

    # Proceso
    def dia_anterior(dia, mes, anho):
        "Resta un día a la fecha"
    dia -= 1
    if dia == 0:
        mes -= 1
        if mes == 0:
            mes = 12
            anho -=1
        dia = dias_mes(mes,anho)
    
    # Salidas
    print()
    print("Día:", dia)
    print("Mes:", mes)
    print("Año: ", anho)


if __name__ == "__main__":
    main()