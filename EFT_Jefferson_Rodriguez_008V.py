import os

# Modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
    '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

# Modelo: [precio, stock]
stock = {
    '8475HD': [387990,10], 
    '2175HD': [327990,4], 
    'JjfFHD': [424990,1],
    'fgdxFHD': [664990,21], 
    '123FHD': [290890,32], 
    '342FHD': [444990,7],
    'GF75HD': [749990,2],
    'UWU131HD': [349990,1], 
    'FS1230HD': [249990,0],
}

def limpiar_pantalla():
    os.system("cls")

def print_menu():
    print("***MENU PRINCIPAL***")
    print("1. Stock marca")
    print("2. Búsqueda por precio")
    print("3. Actualizar precio")
    print("4. Salir")

def stock_marca(marca):
    filtrado = {key: value for key, value in productos.items() if value[0].lower() == marca.lower()}
    
    total = 0
    for key, value in stock.items():
        if key in filtrado:
            total += value[1]
    
    print(f"El stock es: {total}")


def busqueda_precio(p_min: int, p_max: int) -> list | str:
    filtrado = {key: value[0] for key, value in stock.items() if p_min <= value[0] <= p_max and value[1] > 0}
    # filtrado = modelo: precio. La condición value[1] != 0 checkea si el stock es mayor a 0 ^
    lista_notebooks = []
    for key, value in productos.items():
        if key in filtrado:
            lista_notebooks.append(f"{value[0]}--{key}")
    if lista_notebooks:
        return f"Los notebooks ente los precios consultas son: {sorted(lista_notebooks)}"
    return "No hay notebooks en ese rango de precios."
    
def actualizar_precio(modelo, p) -> bool: #Si existe return True. si no false 
    try:
        stock[modelo][0] = p
        return True
    except ValueError:
        return False

def elegir_opcion(max) -> int:
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= max:
                return opcion
            raise ValueError
        except ValueError:
            print("Debe seleccionar una opción válida")

def main():
    limpiar_pantalla()
    while True:

        print_menu()
        opcion = elegir_opcion(4)
        
        if opcion == 1:
            print("\nConsultar stock marca: -----------------")
            stock_marca(input("Ingrese marca a consultar: "))
        
        elif opcion == 2:
            print("\nBusqueda por precio: --------------------")
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min > p_max:
                        raise SyntaxError  
                    print(busqueda_precio(p_min, p_max))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
                except SyntaxError:
                    print("Recuerde que el valor mínimo tiene que ser menor que el máximo")

        elif opcion == 3:
            print("\nActualizar precio: --------------------")
            continuar = True
            while continuar:
                modelo = input("Ingrese modelo a actualizar: ")
                precio_incorrecto = True
                while precio_incorrecto:
                    try:
                        p = int(input("Ingrese precio nuevo: "))
                        if p < 0:
                            raise SyntaxError
                        precio_incorrecto = False
                    except ValueError:
                        print("Debe ingresar valores enteros!!")
                    except SyntaxError:
                        print("Debe ingresar valores enteros positivos!!")

                if actualizar_precio(modelo, p):
                    print("Precio actualizado!!")
                    elegido = ""
                    while elegido not in ("si", "no", "s", "n"):
                        elegido = input("Desea actualizar otro precio (s/n): ").lower()
                        if elegido in ("no", "n"):
                            continuar = False
                else:
                    print("El modelo no existe!!")

        elif opcion == 4:
            limpiar_pantalla()
            print("Programa finalizado.")
            break

        print("----------------------------------------")
        input("Aprete ENTER para continuar             ")
        limpiar_pantalla()
main()
