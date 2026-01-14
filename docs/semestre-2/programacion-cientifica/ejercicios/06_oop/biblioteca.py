from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Dict, List, Optional

# =========================
# MODELOS
# =========================

class Autor:
    def __init__(self, Nombre: str, Nacionalidad: str):
        self.Nombre = Nombre
        self.Nacionalidad = Nacionalidad

    def __str__(self) -> str:
        return f"{self.Nombre} ({self.Nacionalidad})"


class Libro:
    def __init__(self, Titulo: str, ISBN: str, Autor: Autor):
        self.Titulo = Titulo
        self.ISBN = ISBN
        self.Autor = Autor
        self.Disponible = True

    def __str__(self) -> str:
        return f"'{self.Titulo}' de {self.Autor.Nombre} (ISBN: {self.ISBN}) - {'Disponible' if self.Disponible else 'Prestado'}"

    def cambiar_estado(self) -> None:
        self.Disponible = not self.Disponible


class Cliente:
    def __init__(self, Nombre: str, Email: str, Numero_cliente: int):
        self.Nombre = Nombre
        self.Email = Email
        self.Numero_cliente = Numero_cliente
        self.prestamos: List[Prestamo] = []

    def __str__(self) -> str:
        return f"{self.Numero_cliente} - {self.Nombre} <{self.Email}>"


class Prestamo:
    def __init__(self, Cliente: Cliente, Libro: Libro, Fecha_prestamo: datetime, Fecha_devolucion: datetime):
        self.Cliente = Cliente
        self.Libro = Libro
        self.Fecha_prestamo = Fecha_prestamo
        self.Fecha_devolucion = Fecha_devolucion

    def __str__(self) -> str:
        fp = self.Fecha_prestamo.strftime('%d/%m/%Y')
        fd = self.Fecha_devolucion.strftime('%d/%m/%Y')
        return f"{self.Libro.Titulo} -> {self.Cliente.Nombre} | {fp} a {fd}"

    def realizar_prestamo(self) -> bool:
        if self.Libro.Disponible:
            self.Libro.cambiar_estado()
            return True
        return False

    def verificar_retraso(self) -> str:
        fecha_actual = datetime.now()
        if fecha_actual > self.Fecha_devolucion:
            dias_retraso = (fecha_actual - self.Fecha_devolucion).days
            multa = dias_retraso * 0.50
            return f"Retraso de {dias_retraso} días. Multa a pagar: ${multa:.2f}"
        return "El préstamo está en fecha."


class Biblioteca:
    def __init__(self):
        self.libros: List[Libro] = []
        self.clientes: List[Cliente] = []
        self.prestamos: List[Prestamo] = []

    # ---- Altas ----
    def agregar_libro(self, libro: Libro) -> None:
        # Evitar ISBN duplicado
        if any(l.ISBN == libro.ISBN for l in self.libros):
            raise ValueError("Ya existe un libro con ese ISBN")
        self.libros.append(libro)

    def agregar_cliente(self, cliente: Cliente) -> None:
        if any(c.Numero_cliente == cliente.Numero_cliente for c in self.clientes):
            raise ValueError("Ya existe un cliente con ese número")
        self.clientes.append(cliente)

    # ---- Búsquedas ----
    def buscar_libros(self, texto: str) -> List[Libro]:
        t = texto.lower().strip()
        return [
            l for l in self.libros
            if t in l.Titulo.lower() or t in l.Autor.Nombre.lower() or t in l.ISBN.lower()
        ]

    def obtener_libro_por_isbn(self, isbn: str) -> Optional[Libro]:
        for l in self.libros:
            if l.ISBN == isbn:
                return l
        return None

    def obtener_cliente_por_numero(self, numero: int) -> Optional[Cliente]:
        for c in self.clientes:
            if c.Numero_cliente == numero:
                return c
        return None

    # ---- Préstamos ----
    def realizar_prestamo(self, cliente: Cliente, libro: Libro, dias: int = 7) -> bool:
        if not libro.Disponible:
            return False
        if len(cliente.prestamos) >= 3:
            return False

        fecha_hoy = datetime.now()
        fecha_dev = fecha_hoy + timedelta(days=dias)
        p = Prestamo(cliente, libro, fecha_hoy, fecha_dev)

        if p.realizar_prestamo():
            self.prestamos.append(p)
            cliente.prestamos.append(p)
            return True
        return False

    def devolver_libro(self, cliente: Cliente, libro: Libro) -> bool:
        prestamo = next((p for p in cliente.prestamos if p.Libro == libro), None)
        if not prestamo:
            return False

        # vuelve a estar disponible
        if not libro.Disponible:
            libro.cambiar_estado()

        cliente.prestamos.remove(prestamo)
        # Mantener historial general (opcional): lo dejamos en self.prestamos
        return True


# =========================
# UTILIDADES CLI
# =========================

def input_no_vacio(msg: str) -> str:
    while True:
        v = input(msg).strip()
        if v:
            return v
        print("No puede estar vacío.")


def input_int(msg: str) -> int:
    while True:
        try:
            return int(input(msg).strip())
        except ValueError:
            print("Ingresá un número válido.")


def pausar() -> None:
    input("\nEnter para continuar...")


def imprimir_lista(titulo: str, items: List[object]) -> None:
    print(f"\n=== {titulo} ===")
    if not items:
        print("(vacío)")
        return
    for i, it in enumerate(items, 1):
        print(f"{i}. {it}")


# =========================
# APP INTERACTIVA
# =========================

class AppBiblioteca:
    def __init__(self):
        self.biblio = Biblioteca()
        self.autores: Dict[str, Autor] = {}
        self._cargar_datos_demo()

    def _cargar_datos_demo(self) -> None:
        # Datos mínimos para probar (podés borrar si querés)
        a1 = Autor("Autor 1", "Uruguay")
        a2 = Autor("J. Borges", "Argentina")
        self.autores[a1.Nombre.lower()] = a1
        self.autores[a2.Nombre.lower()] = a2

        self.biblio.agregar_libro(Libro("Libro 1", "1234567890", a1))
        self.biblio.agregar_libro(Libro("Ficciones", "9789875666484", a2))

        self.biblio.agregar_cliente(Cliente("Juan", "juan@example.com", 1))
        self.biblio.agregar_cliente(Cliente("Ana", "ana@example.com", 2))

    # -------- Menú --------
    def run(self) -> None:
        while True:
            self._imprimir_menu()
            op = input("\nElegí una opción: ").strip()

            try:
                if op == "1":
                    self.alta_autor()
                elif op == "2":
                    self.alta_libro()
                elif op == "3":
                    self.alta_cliente()
                elif op == "4":
                    self.listar_libros()
                elif op == "5":
                    self.buscar_libros()
                elif op == "6":
                    self.prestar_libro()
                elif op == "7":
                    self.devolver_libro()
                elif op == "8":
                    self.ver_prestamos_cliente()
                elif op == "9":
                    self.ver_prestamos_totales()
                elif op == "10":
                    self.verificar_retrasos()
                elif op == "0":
                    print("\n¡Chau!")
                    break
                else:
                    print("Opción inválida.")
            except Exception as e:
                print(f"Error: {e}")

            pausar()

    def _imprimir_menu(self) -> None:
        print("\n\n============================")
        print("  GESTOR DE BIBLIOTECA (CLI)")
        print("============================")
        print("1) Alta autor")
        print("2) Alta libro")
        print("3) Alta cliente")
        print("4) Listar libros")
        print("5) Buscar libros")
        print("6) Prestar libro")
        print("7) Devolver libro")
        print("8) Ver préstamos de un cliente")
        print("9) Ver préstamos totales (historial)")
        print("10) Verificar retrasos (de préstamos activos)")
        print("0) Salir")

    # -------- Funciones --------

    def alta_autor(self) -> None:
        nombre = input_no_vacio("Nombre del autor: ")
        nac = input_no_vacio("Nacionalidad: ")
        key = nombre.lower()
        if key in self.autores:
            print("Ya existe ese autor.")
            return
        self.autores[key] = Autor(nombre, nac)
        print("Autor agregado.")

    def alta_libro(self) -> None:
        titulo = input_no_vacio("Título: ")
        isbn = input_no_vacio("ISBN: ")
        autor_nombre = input_no_vacio("Autor (nombre): ")
        key = autor_nombre.lower()
        autor = self.autores.get(key)
        if not autor:
            # Crear autor en el momento
            print("No existe ese autor. Vamos a crearlo.")
            nac = input_no_vacio("Nacionalidad del autor: ")
            autor = Autor(autor_nombre, nac)
            self.autores[key] = autor

        self.biblio.agregar_libro(Libro(titulo, isbn, autor))
        print("Libro agregado.")

    def alta_cliente(self) -> None:
        nombre = input_no_vacio("Nombre: ")
        email = input_no_vacio("Email: ")
        numero = input_int("Número de cliente: ")
        self.biblio.agregar_cliente(Cliente(nombre, email, numero))
        print("Cliente agregado.")

    def listar_libros(self) -> None:
        imprimir_lista("Libros", self.biblio.libros)

    def buscar_libros(self) -> None:
        texto = input_no_vacio("Buscar por título/autor/ISBN: ")
        res = self.biblio.buscar_libros(texto)
        imprimir_lista("Resultados", res)

    def prestar_libro(self) -> None:
        numero = input_int("Número de cliente: ")
        cliente = self.biblio.obtener_cliente_por_numero(numero)
        if not cliente:
            print("Cliente no encontrado.")
            return

        isbn = input_no_vacio("ISBN del libro: ")
        libro = self.biblio.obtener_libro_por_isbn(isbn)
        if not libro:
            print("Libro no encontrado.")
            return

        dias = input_int("Días de préstamo (default 7): ")
        if dias <= 0:
            dias = 7

        ok = self.biblio.realizar_prestamo(cliente, libro, dias=dias)
        if ok:
            # obtener el préstamo recién creado (último del cliente)
            p = cliente.prestamos[-1]
            print(f"Préstamo exitoso. Devolver el: {p.Fecha_devolucion.strftime('%d/%m/%Y')}")
        else:
            if not libro.Disponible:
                print("No se puede: el libro ya está prestado.")
            elif len(cliente.prestamos) >= 3:
                print("No se puede: el cliente ya tiene 3 préstamos activos.")
            else:
                print("No se pudo realizar el préstamo.")

    def devolver_libro(self) -> None:
        numero = input_int("Número de cliente: ")
        cliente = self.biblio.obtener_cliente_por_numero(numero)
        if not cliente:
            print("Cliente no encontrado.")
            return

        if not cliente.prestamos:
            print("Ese cliente no tiene préstamos activos.")
            return

        imprimir_lista("Préstamos activos del cliente", cliente.prestamos)
        isbn = input_no_vacio("ISBN del libro a devolver: ")
        libro = self.biblio.obtener_libro_por_isbn(isbn)
        if not libro:
            print("Libro no encontrado.")
            return

        ok = self.biblio.devolver_libro(cliente, libro)
        print("Devuelto correctamente." if ok else "Ese cliente no tiene ese libro en préstamo.")

    def ver_prestamos_cliente(self) -> None:
        numero = input_int("Número de cliente: ")
        cliente = self.biblio.obtener_cliente_por_numero(numero)
        if not cliente:
            print("Cliente no encontrado.")
            return
        imprimir_lista(f"Préstamos activos de {cliente.Nombre}", cliente.prestamos)

    def ver_prestamos_totales(self) -> None:
        imprimir_lista("Historial de préstamos (incluye devueltos)", self.biblio.prestamos)

    def verificar_retrasos(self) -> None:
        activos: List[Prestamo] = []
        for c in self.biblio.clientes:
            activos.extend(c.prestamos)

        print("\n=== Retrasos (préstamos activos) ===")
        if not activos:
            print("No hay préstamos activos.")
            return

        for p in activos:
            print(f"- {p} | {p.verificar_retraso()}")


if __name__ == "__main__":
    AppBiblioteca().run()
