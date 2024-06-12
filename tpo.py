import random
def main():
    productos = [1,2,3,4,5,6]
    stock = [2,2,2,2,2,2]
    precios = [50,10,55,20,25,30] 
    nombreProducto = ["Placas de video","Memorias Ram","Procesadores","Disocs HDD","Discos SSD","Discos Nvme"]
    ValorFinalCompra = []
    print("Hola Bienvenido a la casita del hardware")
    print("MENU")
    print("1. Comprar")
    print("2. Ver carrito")
    print("3. Finalizar Pago")
    print("-1. Finalizar ")
    opcion = int(input("Ingrese una opcion o -1 para finalizar: "))
    while (opcion < 1 or opcion > 3) and opcion != -1:
        print("MENU")
        print("1. Comprar")
        print("2. Ver carrito")
        print("3. Finalizar Pago")
        print("-1. Finalizar ")
        opcion = int(input("Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida"))
    while (opcion <= 3) and (opcion >= 1) and (opcion != -1):
        if opcion == 1:
            ValorCompra = comprar(productos,stock,precios, nombreProducto)
            print("Hola Bienvenido a la casita del hardware")
            print("MENU")
            print("1. Comprar")
            print("2. Ver carrito")
            print("3. Finalizar Pago")
            print("-1. Finalizar ")
            opcion = int(input("Ingrese una opcion o -1 para finalizar: "))
        elif opcion == 3:
            ValorFinal = pago(ValorCompra)
            ValorFinalCompra.append(ValorFinal)
            opcion = int(input("Ingrese -1 para finalizar: "))
            while opcion != -1:
                opcion = int(input("Usted ya ha realizado el pago, le suplicamos cerrar el tramite"))

    
def comprar(productos,stock,precios, nombreProducto):
    carritoProducto=[]
    carrito=[]
    montoTotal = 0
    
    print("Producto 			Identificador	Stock 		Precio")
    
    for i in range(len(productos)):
        print("%15s \t %8d\t %8d \t %8d" %(nombreProducto[i], productos[i],stock[i], precios[i]))
    ident = int(input("Ingrese el identificador del producto que desea agregar al carrito o -1 para finalizar"))
    
    while (ident not in productos) and (ident != -1):
        ident = int(input("Usted ingreso un producto no existente. Ingrese un producto para agregar al carrito o -1 para finalizar"))

    while (ident in productos) and (ident != -1):
        cantidad = validacionRango(2,-1,"Ingrese la cantidad de productos deseada","Lamentamos informale que no poseemos suficiente stock disponible, seleccioan una cantidad distinta", "Usted ingreso una cantidad no valida para el sistema, ingrese una cantidad valida")
        indice = buscarElemento(ident,productos)     
        indiceCarrito = buscarElemento(productos[indice],carritoProducto)
        
        if indiceCarrito != -1:
            carrito[indiceCarrito] += precios[indiceCarrito]*cantidad
        else:
            carritoProducto.append(productos[indice])
            carrito.append(precios[indice]*cantidad)
        
        for i in range(len(productos)):
            print("%15s \t %8d\t %8d \t %8d" %(nombreProducto[i], productos[i],stock[i], precios[i]))
        ident = int(input("Ingrese un producto para agregar al carrito o -1 para finalizar"))

    
    for i in range(len(carrito)):
        montoTotal += carrito[i]
    print(montoTotal)
    return montoTotal
    
def validacionRango(rango2,cf,texto,textoEM, textoEm):
    valor = int(input(texto))
    
    while (valor < 1 or valor > rango2) and valor!= cf:
        if valor > rango2:
            valor=int(input(textoEM))
        elif valor < 1:
            valor=int(input(textoEm))
            
    return valor


def buscarElemento(valorBuscado,lista):
    pos=-1
    i=0
    
    while pos==-1 and i<(len(lista)):
        if lista[i] == valorBuscado:
            pos = i
        i+=1    
    
    return pos    

def pago(ValorCompra):
    print("1. Efectivo")
    print("2. Tarjetas Debito o Credito")
    print("3. Trasnferencia")
    Fpago = int(input("Seleccione un medio de pago"))
    while (Fpago < 1 or Fpago > 3):
        print("1. Efectivo")
        print("2. Tarjetas Debito o Credito")
        print("3. Trasnferencia")
        Fpago = int(input("Ingreso un medio de pago no valido. Vuelva a ingresar un medio de pago"))
    
    usuario = random.randint(1,2)
    if (usuario % 2) == 0:
        if Fpago == 1:
            Descuento = (ValorCompra * 20) / 100
            ValorFinal = ValorCompra - Descuento
            print(ValorFinal)
        elif Fpago == 2: 
            Descuento = (ValorCompra * 10) / 100
            ValorFinal = ValorCompra - Descuento
            print(ValorFinal)
        else:
            Descuento = (ValorCompra * 15) / 100
            ValorFinal = ValorCompra - Descuento
            print(ValorFinal)
    else:
        if Fpago == 1:
            Descuento = (ValorCompra * 5) / 100
            ValorFinal = ValorCompra - Descuento
            print(ValorFinal)
        elif Fpago == 2:
            ValorFinal = ValorCompra
            print(ValorFinal)
        else:
            Descuento = (ValorCompra * 3) / 100
            ValorFinal = ValorCompra - Descuento
            print(ValorFinal)
    return ValorFinal
        
if __name__ == "__main__":
    main()
