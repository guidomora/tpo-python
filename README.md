El programa iniciara con datos ya cargados para cada tipo de articulo: Procesadores, Memorias RAM y 
  Placas de Video (3 para cada tipo especificamente). Cada registro de articulo cuenta con los siguientes 
  datos: Nombre, Categoria, Cantidad en Stock y Precio Unitario.
 
  El programa le pedira al usuario ingresar su codigo de usuario. Una vez hecho esto se le muestra 
  el menu de compras. Las opciones de este menu son las tres categorias de los productos que quiere 
  llevar (CPU, memoria RAM y GPUs) y una opcion de salir del sistema, esto esta acompañado con otra linea que le informa el 
  importe total de su detalle de compra de compras (que inicialmente sera de 0).
  Si el usuario elije alguna opcion de categoria, se le mostrara a continuacion la lista de productos
  correspondientes a dicha categoria, la cantidad de stock y su precio unitario. El cliente entonces
  ingresara el numero de opcion correspondiente del producto que desea llevar y la cantidad de stock 
  a comprar. Si la cantidad de stock deseada es mayor a la cantidad de stock disponible se le notificara 
  que hay stock insuficiente y que vuelva a ingresar la cantidad de stock (salvo que el stock sea 0).
  Una vez que confirme la compra, se le pregunta si quiere agregar algo. En caso de 
  ser positivo, se le vuelve a mostrar el menu de compras para modificar el detalle final de compra., en caso contrario, se le informa el importe
  total del detalle de compra en el cual si hay productos repetidos, aumenta la cantidad, no se ve el producto varias veces. 
  Se le pregunta con que metodo de pago va a abonar. El importe total dependera de 
  dicha opcion siendo de esta manera: Efectivo 10% de descuento del valor final, para las tarjetas es el 100% del pago y para transferencias pensamos utilizar la bibiloteca "random"
  para hacer un calculo segun un valor aleatorio del 1 al 2, si el codigo del usuario es par, se le aplcia un 15% de descuento, de caso contrario, no se le aplcia nada.
  Terminada la compra se sale del sistema y se vuelve a pedir el codigo de usuario del cliente. 
  Para finalizar el codigo de usuario debera ser igual a -1 y se mostrara en pantalla, el total dinero ingresado al sistema, la compra mas alta y la mas baja. 
  Utilizando minimos y maximos.