# Cálculo del saldo
# INICIO

# Obtener saldo actual
saldo = float(input('Dame saldo actual (puede ser entero o flotante): '))

# Obtener porcentaje de interés
interes_porcentaje = float(input('Dame el porcentaje de interés: ')) / 100

# Inicializar la variable interes
interes = 0

# Empieza la condición
if saldo < 10000.00:
    interes = saldo * interes_porcentaje  # Calcula el interés
    saldo += interes  # Incrementa el saldo con el interés
    print(f"Se está cobrando un interés de {interes:.2f}")
else:
    saldo += 10.04  # Se incrementa el saldo en 10.04

# Fin del if
print(f"Saldo final es {saldo:5.2f}")
# FIN
