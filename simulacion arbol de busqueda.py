
class Nodo:
    def __init__(self, codigo, nombre, categoria):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.izquierda = None
        self.derecha = None


class BibliotecaDigital:
    def __init__(self):
        self.raiz = None

    def insertar(self, codigo, nombre, categoria):
        nuevo = Nodo(codigo, nombre, categoria)

        if self.raiz is None:
            self.raiz = nuevo
            return

        actual = self.raiz

        while True:
            if codigo < actual.codigo:
                if actual.izquierda is None:
                    actual.izquierda = nuevo
                    return
                actual = actual.izquierda

            elif codigo > actual.codigo:
                if actual.derecha is None:
                    actual.derecha = nuevo
                    return
                actual = actual.derecha

            else:
                print("El codigo ya existe.")
                return

    def buscar(self, codigo):
        actual = self.raiz
        comparaciones = 0

        while actual is not None:
            comparaciones += 1

            if codigo == actual.codigo:
                print("\nDocumento encontrado:")
                print("Codigo:", actual.codigo)
                print("Nombre:", actual.nombre)
                print("Categoria:", actual.categoria)
                print("Comparaciones:", comparaciones)
                return

            elif codigo < actual.codigo:
                actual = actual.izquierda

            else:
                actual = actual.derecha

        print("\nDocumento no encontrado.")
        print("Comparaciones:", comparaciones)

    def preorden(self, nodo):
        if nodo:
            print(nodo.codigo, end=" ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.codigo, end=" ")
            self.inorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.codigo, end=" ")

    def altura(self, nodo):
        if nodo is None:
            return -1

        izquierda = self.altura(nodo.izquierda)
        derecha = self.altura(nodo.derecha)

        return 1 + max(izquierda, derecha)


# Crear biblioteca
biblioteca = BibliotecaDigital()

# Insertar documentos
documentos = [
    (40, "Fundamentos de matematicas", "Matematicas"),
    (20, "Introduccion a la fisica", "Fisica"),
    (60, "Programacion basica", "Ingenieria de Sistemas"),
    (10, "Algebra elemental", "Matematicas"),
    (30, "Mecanica clasica", "Fisica"),
    (50, "Algoritmos computacionales", "Ingenieria de Sistemas"),
    (70, "Circuitos electronicos", "Electronica")
]

for codigo, nombre, categoria in documentos:
    biblioteca.insertar(codigo, nombre, categoria)

# Realizar busquedas
print("=== BUSQUEDA DE DOCUMENTOS ===")
biblioteca.buscar(50)
biblioteca.buscar(67)

# Mostrar recorridos
print("\n=== RECORRIDOS DEL ARBOL ===")

print("Preorden:")
biblioteca.preorden(biblioteca.raiz)

print("\nInorden:")
biblioteca.inorden(biblioteca.raiz)

print("\nPostorden:")
biblioteca.postorden(biblioteca.raiz)

# Calcular altura
print(
    "\n\nAltura del arbol:",
    biblioteca.altura(biblioteca.raiz)
)
