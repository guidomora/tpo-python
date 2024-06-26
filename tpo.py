import random
def main():
    usuarios = [45,32,65]
    
    nombreCategorias = ["GPU"]
    codigoCategoria = [23]
    
    productos = [1,2,3,4]
    nombreProducto = ["Placa RADEON 4545","Placa nvidia 4060", "Placa rtx 3070ti", "Placa RADEON rx 7900"]
    categoriaProducto=[23,23,23,23]
    stock = [2,2,2,2]
    carritoProducto=[]
    carrito=[]
    
    
    precios = [50,10,55,20,] 
    ValorFinalCompra = []
    ValorCompra=0
    
    validacionLista(usuarios,"Ingrese su ID de usuario: ", "El ID de usuario es incorrecto ingrese unn ID valido: ")
    
    imprimirMenu()
        
    opcion = validacionRango(1,3,-1,"Ingrese una opcion o -1 para finalizar: ", "Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida: ")
        
    while opcion != -1:
        
        if opcion == 1:
            ValorCompra = comprar(productos,stock,precios, nombreProducto,codigoCategoria,nombreCategorias,categoriaProducto,carritoProducto,carrito)
            
            if ValorCompra != -1:
                imprimirMenuFinal()
                opcion = validacionRango(1,2,-1,"Ingrese una opcion o -1 para finalizar: ", "Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida: ")
                while opcion != -1:
                    if opcion == 1:
                        Espacio = bubble_sort(carrito,nombreProducto)
                        carritoDeCompras(carritoProducto,carrito,productos,precios,nombreProducto)
                        imprimirMenuFinal()
                        opcion = validacionRango(1,2,-1,"Ingrese una opcion o -1 para finalizar: ", "Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida: ")
                    elif opcion == 2:
                        ValorFinal = pago(ValorCompra)
                        ValorFinalCompra.append(ValorFinal)
                        print("El producto con mas valor vendido fue: ", carrito[Espacio-1], "y el producto con menor valor vendido fue: ", carrito[0])
                        opcion = int(input("Ingrese -1 para finalizar: "))

        elif opcion == 2 and ValorCompra == 0:
            print("No se ha realizado ninguna compra")
            imprimirMenu()
            opcion = validacionRango(1,3,-1,"Ingrese una opcion o -1 para finalizar: ", "Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida: ")
        
        elif opcion == 3:
            if ValorCompra == 0:
                print("No se ha realizado ninguna compra")
                imprimirMenu()
                opcion = validacionRango(1,3,-1,"Ingrese una opcion o -1 para finalizar: ", "Usted ingreso una opcion no valida para el sistema, ingrese una opcion valida: ")
            else:
                ValorFinal = pago(ValorCompra)
                ValorFinalCompra.append(ValorFinal)


    
def comprar(productos,stock,precios, nombreProducto,codigoCategoria,nombreCategorias,categoriaProducto,carritoProducto,carrito):
    montoTotal = 0
    
    categoria = imprimirCategoria(codigoCategoria,nombreCategorias)
    
    imprimirProductosCategoria(categoria,categoriaProducto,nombreProducto,productos,stock,precios)
        
    ident = validarProducto(productos)

    while  ident != -1:
        indice = buscarElemento(ident,productos)     
        indiceCarrito = buscarElemento(productos[indice],carritoProducto)
        
        cantidad = validacionSimple(1,stock[indice],"Ingrese la cantidad que desea adquirir: ","Ingreso una cantidad superior al stock, ingrese un valor valida:  ")
                
        if indiceCarrito != -2:
            carrito[indiceCarrito] += precios[indiceCarrito]*cantidad
        else:
            carritoProducto.append(productos[indice])
            carrito.append(precios[indice]*cantidad)
        
        imprimirProductosCategoria(categoria,categoriaProducto,nombreProducto,productos,stock,precios)
        ident = validarProducto(productos)
    
        
    if len(carrito) > 0:
        for i in range(len(carrito)):
            montoTotal += carrito[i]
        print(montoTotal)
    else:
        montoTotal = -1
        
    return montoTotal
    
def validacionSimple(rango1,rango2,texto,textoEM):
    valor = int(input(texto))
    
    while valor < rango1 or valor > rango2:
        valor = int(input(textoEM))
            
    return valor

def validacionRango(rango1,rango2,cf,texto,textoEM):
    print("------------------------------------")
    valor = int(input(texto))
    
    while (valor < rango1 or valor > rango2) and valor!= cf:
        valor = int(input(textoEM))
            
    return valor

def validacionLista(lista,texto,textoError):
    valor = int(input(texto))
    indice = buscarElemento(valor,lista)
    
    while indice == -2:
        valor = int(input(textoError))
        indice = buscarElemento(valor,lista)
    
    return valor

def buscarElemento(valorBuscado,lista):
    pos=-2
    i=0
    
    while pos==-2 and i<(len(lista)):
        if lista[i] == valorBuscado:
            pos = i
        i+=1    
    
    return pos    

def pago(ValorCompra):
    print("1. Efectivo")
    print("2. Tarjetas Debito o Credito")
    print("3. Transferencia")
    
    Fpago = validacionSimple(1,3,"Seleccione un medio de pago: ","Ingreso un medio de pago no valido. Vuelva a ingresar un medio de pago: ")
    usuario = random.randint(1,2)
    
    

    if Fpago == 1:
        print("En efectivo se le aplicara un descuento del 10%")
        ValorCompra = ValorCompra * 0.90
        ValorFinal = ValorCompra
        print(ValorFinal)
            
    elif Fpago == 2:
        ValorFinal = ValorCompra
        print(ValorFinal)
    
    elif (Fpago == 3) and (usuario % 2 == 0):
        ValorCompra = ValorCompra * 0.85
        print("Felicidades se le aplicara un descuento promocional del 15 %")
    ValorFinal = ValorCompra   
    return ValorFinal 
   
def imprimirMenu():
    print("Hola Bienvenido a la casita del hardware")
    print("MENU")
    print("1. Comprar")
    print("2. Ver carrito")
    print("3. Finalizar Pago")
    print("-1. Finalizar ")

def imprimirCategoria(codigoCategoria,nombreCategorias):
    print("CATEGORIAS")
    for i in range(len(codigoCategoria)):
        print(codigoCategoria[i],". ",nombreCategorias[i])

    categoria = validacionLista(codigoCategoria,"Ingrese el codigo de una categoria: ", "El codigo de la categoria es incorrecto: ")
    return categoria

def imprimirProductosCategoria(categoria,listaCategorias,nombreProducto,productos,stock,precios):
    print("Producto 			Identificador	Stock 		Precio")
    for i in range(len(listaCategorias)):
        if listaCategorias[i]==categoria:
            print("%15s \t %8d\t %8d \t %8d" %(nombreProducto[i], productos[i],stock[i], precios[i]))   
    
def validarProducto(productos):
    identificador = int(input("Ingrese el identificador del producto que desea agregar al carrito o -1 para finalizar: "))
    indice = buscarElemento(identificador,productos)
    
    while indice == -2 and identificador != -1:
        identificador = int(input("Usted ingreso un producto no existente. Ingrese un producto para agregar al carrito o -1 para finalizar: "))
        indice = buscarElemento(identificador,productos) 
    
    return identificador

def imprimirMenuFinal():
    print("------------------------------------")
    print("1. Ver carrito")
    print("2. Finalizar Pago")
    print("-1. Finalizar ")
    
def carritoDeCompras(carritoProducto,carrito,productos,precios,nombreProducto):
    print("------------------------------------")
    print("Carrito de compras")
    print("Producto\t\t\tPrecio\t\tUnidades")
    for i in range(len(carrito)):
        indice = buscarElemento(carritoProducto[i],productos)

        print("%15s \t %8d \t %3d" %(nombreProducto[indice],carrito[i],(carrito[i]/precios[indice])))

        

def bubble_sort(lista1,lista2):
    Espacio = len(lista1)
    for i in range(0,Espacio-1):
        for j in range(0,Espacio-1-i):
            if (lista1[j] > lista1[j+1]):
                aux = lista1[j]
                lista1[j] = lista1[j+1]
                lista1[j+1] = aux
                
                aux = lista2[j]
                lista2[j] = lista2[j+1]
                lista2[j+1] = aux
    return Espacio
                
    

if __name__ == "__main__":
    main()
