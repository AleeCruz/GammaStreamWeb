
maquina_1 = int(input("Digite o valor da máquina 1: "))
maquina_2 = int(input("Digite o valor da máquina 2: "))
maquina_3 = int(input("Digite o valor da máquina 3: "))
maquina_4 = int(input("Digite o valor da máquina 4: "))
maquina_5 = int(input("Digite o valor da máquina 5: "))

maquinas_por_cantidad_de_piezas = [maquina_1, maquina_2, maquina_3, maquina_4, maquina_5]

maximo = maquina_1
actual = 0

for actual in maquinas_por_cantidad_de_piezas:
    if actual > maximo:
        maximo = actual
        
        
print("La maquina con mayor cantidad de piezas es:", maximo)