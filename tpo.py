def main():
    productos = [12,43,547,123,86,34]
    stock = [2,2,2,2,2,2]
    precios = [2,2,2,2,2,2] 
    nombreProducto = ["nom1","nom2","nom3","nom4","nom5","nom6"]
    
    print("Hola Bienvenido a la casita del hardware")
    print("MENU")
    print("1. Comprar")
    
    opcion = int(input("Ingrese una opcion o -1 para finalizar: "))
    
    while opcion != -1:
        if opcion == 1:
            comprar(productos,stock,precios)
            
        opcion = int(input("Ingrese una opcion o -1 para finalizar: "))
    
    
def comprar(productos,stock,precios):
    carritoProducto=[]
    carrito=[]
    montoTotal = 0
    
    print("Los productos son :", productos)
    id = int(input("Ingrese un producto para agregar al carrito o -1 para finalizar"))
    cantidad = int(input("Ingrese una cantidad mayor a 0"))
    
    while id != -1:
        indice = buscarElemento(id,productos)     
        indiceCarrito = buscarElemento(productos[indice],carritoProducto)
        
        if indiceCarrito != -1:
            carrito[indiceCarrito] += precios[indiceCarrito]*cantidad
        else:
            carritoProducto.append(productos[indice])
            carrito.append(precios[indice]*cantidad)
            
        id = int(input("Ingrese un producto para agregar al carrito o -1 para finalizar"))
        cantidad = int(input("Ingrese una cantidad mayor a 0"))
    
    for i in range(len(carrito)):
        montoTotal += carrito[i]

    return montoTotal
    
def validacionRango(rango1,rango2,cf,texto,textoE):
    valor = int(input(texto))

    while (valor<rango1 or valor>rango2) and valor!=cf:
        valor=int(input(textoE))
    return valor


def buscarElemento(valorBuscado,lista):
    pos=-1
    i=0
    
    while pos==-1 and i<(len(lista)):
        if lista[i] == valorBuscado:
            pos = i
        i+=1    
    
    return pos    
    
if _name_ == "_main_":
    main()