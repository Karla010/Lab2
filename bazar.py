class Prenda:
    def __init__(self, nombre, precio, talla):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla

class Seccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

class Bazar:
    def __init__(self):
        self.secciones = {}
        self.compras = []

    def agregar_seccion(self, seccion):
        self.secciones[seccion.nombre] = seccion

    def agregar_prenda_a_seccion(self, nombre_seccion, prenda):
        if nombre_seccion in self.secciones:
            self.secciones[nombre_seccion].agregar_prenda(prenda)
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")

    def mostrar_secciones(self):
        for i, seccion in enumerate(self.secciones.values()):
            print(f"{i + 1}. {seccion.nombre}")

    def mostrar_prendas(self, nombre_seccion):
        seccion = self.secciones.get(nombre_seccion)
        if seccion:
            for i, prenda in enumerate(seccion.prendas):
                print(f"{i + 1}. {prenda.nombre} (Talla: {prenda.talla}) - ${prenda.precio:.2f}")
        else:
            print(f"Sección '{nombre_seccion}' no encontrada.")

    def agregar_prenda_a_compras(self, prenda):
        self.compras.append(prenda)

    def mostrar_lista_compras(self):
        if not self.compras:
            print("No hay prendas en la lista de compras.")
        else:
            for prenda in self.compras:
                print(f"{prenda.nombre} (Talla: {prenda.talla}) - ${prenda.precio:.2f}")

    def calcular_total_compras(self):
        total = sum(prenda.precio for prenda in self.compras)
        print(f"Total de la compra: ${total:.2f}")

def main():
    bazar = Bazar()

    # Crear secciones
    secciones = ["Camisetas", "Pantalones", "Zapatos", "Accesorios"]
    for nombre_seccion in secciones:
        bazar.agregar_seccion(Seccion(nombre_seccion))

    # Crear prendas y asignarlas a secciones
    prendas = [
        Prenda("Camiseta Blanca", 15.00, "M"),
        Prenda("Pantalón Vaquero", 30.00, "L"),
        Prenda("Zapatillas Deportivas", 50.00, "42"),
        Prenda("Gorra Negra", 10.00, "Única"),
        Prenda("Bufanda Roja", 20.00, "Única")
    ]

    prendas_por_seccion = {
        "Camisetas": ["Camiseta Blanca"],
        "Pantalones": ["Pantalón Vaquero"],
        "Zapatos": ["Zapatillas Deportivas"],
        "Accesorios": ["Gorra Negra", "Bufanda Roja"]
    }

    for prenda in prendas:
        for nombre_seccion, nombres_prendas in prendas_por_seccion.items():
            if prenda.nombre in nombres_prendas:
                bazar.agregar_prenda_a_seccion(nombre_seccion, prenda)

    while True:
        print("\n1. Agregar prenda a la lista de compras")
        print("2. Ver lista de compras")
        print("3. Calcular total de la compra")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("Secciones disponibles:")
            bazar.mostrar_secciones()
            indice_seccion = int(input("Ingrese el número de la sección: ")) - 1
            nombre_seccion = secciones[indice_seccion]
            print(f"Prendas disponibles en la sección {nombre_seccion}:")
            bazar.mostrar_prendas(nombre_seccion)
            indice_prenda = int(input("Ingrese el número de la prenda: ")) - 1
            prenda = bazar.secciones[nombre_seccion].prendas[indice_prenda]
            bazar.agregar_prenda_a_compras(prenda)
            print(f"Prenda '{prenda.nombre}' agregada a la lista de compras.")

        elif opcion == '2':
            bazar.mostrar_lista_compras()

        elif opcion == '3':
            bazar.calcular_total_compras()

        elif opcion == '4':
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
