def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    vuelto_pesos = int(vuelto)
    vuelto_centavos = int((vuelto - vuelto_pesos) * 100)
    print(f'Ingresar gasto: \n{expense} \nDinero recibido: \n{money} \n \nVuelto \n \nPesos:\n{vuelto_pesos}\nCentavos:\n{vuelto_centavos} ')

change()
