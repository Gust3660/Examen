import re
from collections import deque

OPERADORES = [
    ("swap 0-1", lambda s: [s[1], s[0], s[2], s[3]]),
    ("swap 1-2", lambda s: [s[0], s[2], s[1], s[3]]),
    ("swap 2-3", lambda s: [s[0], s[1], s[3], s[2]]),
]


def parse_estado(texto):
    if texto is None:
        return None
    if isinstance(texto, list):
        return [str(x).strip() for x in texto if str(x).strip() != ""]
    texto = str(texto).strip()
    if texto.startswith("[") and texto.endswith("]"):
        texto = texto[1:-1]
    partes = [parte.strip() for parte in re.split(r"[\s,;]+", texto) if parte.strip() != ""]
    return partes


def estado_a_tupla(estado):
    return tuple(estado)


def esta_en_lista(estado, lista):
    estado_t = estado_a_tupla(estado)
    for item in lista:
        if isinstance(item, Nodo):
            if estado_a_tupla(item.estado) == estado_t:
                return True
        else:
            if estado_a_tupla(item) == estado_t:
                return True
    return False


class Nodo:
    def __init__(self, estado, padre=None, accion=None):
        self.estado = estado
        self.padre = padre
        self.accion = accion

    def camino(self):
        nodo = self
        camino = []
        while nodo is not None:
            camino.append({
                "estado": nodo.estado,
                "accion": nodo.accion,
            })
            nodo = nodo.padre
        return list(reversed(camino))


def expandir(nodo):
    sucesores = []
    for nombre, operador in OPERADORES:
        nuevo_estado = operador(nodo.estado)
        sucesores.append(Nodo(nuevo_estado, padre=nodo, accion=nombre))
    return sucesores


def buscar_dfs_iterativo(estado_inicial, solucion):
    visitados = []
    frontera = [Nodo(estado_inicial)]
    orden_visitados = []

    while frontera:
        nodo = frontera.pop()
        orden_visitados.append(nodo.estado)
        visitados.append(nodo.estado)

        if nodo.estado == solucion:
            return {
                "encontrado": True,
                "camino": nodo.camino(),
                "visitados": orden_visitados,
            }

        dato_nodo = nodo.estado
        hijos = []

        for nombre, operador in OPERADORES:
            nuevo_estado = operador(dato_nodo)
            if not esta_en_lista(nuevo_estado, visitados) and not esta_en_lista(nuevo_estado, frontera):
                hijo = Nodo(nuevo_estado, padre=nodo, accion=nombre)
                frontera.append(hijo)
                hijos.append(hijo)

        nodo.hijos = hijos

    return {"encontrado": False, "camino": [], "visitados": orden_visitados}


def buscar_dfs_recursivo(estado_inicial, solucion):
    orden_visitados = []

    def dfs(nodo):
        estado_t = estado_a_tupla(nodo.estado)
        if estado_t in visitados:
            return None
        visitados.add(estado_t)
        orden_visitados.append(nodo.estado)
        if nodo.estado == solucion:
            return nodo

        dato_nodo = nodo.estado
        hijos = []
        for nombre, operador in OPERADORES:
            nuevo_estado = operador(dato_nodo)
            hijo = Nodo(nuevo_estado, padre=nodo, accion=nombre)
            hijos.append(hijo)
        nodo.hijos = hijos

        for nodo_hijo in nodo.hijos:
            if not esta_en_lista(nodo_hijo.estado, orden_visitados):
                resultado = dfs(nodo_hijo)
                if resultado is not None:
                    return resultado
        return None

    visitados = set()
    raiz = Nodo(estado_inicial)
    solucion_nodo = dfs(raiz)
    if solucion_nodo:
        return {
            "encontrado": True,
            "camino": solucion_nodo.camino(),
            "visitados": orden_visitados,
        }
    return {"encontrado": False, "camino": [], "visitados": orden_visitados}


def buscar_bfs(estado_inicial, solucion):
    visitados = []
    frontera = deque([Nodo(estado_inicial)])
    orden_visitados = []

    while frontera:
        nodo = frontera.popleft()
        orden_visitados.append(nodo.estado)
        visitados.append(nodo.estado)
        if nodo.estado == solucion:
            return {
                "encontrado": True,
                "camino": nodo.camino(),
                "visitados": orden_visitados,
            }

        dato_nodo = nodo.estado
        hijos = []
        for nombre, operador in OPERADORES:
            nuevo_estado = operador(dato_nodo)
            if not esta_en_lista(nuevo_estado, visitados) and not esta_en_lista(nuevo_estado, frontera):
                hijo = Nodo(nuevo_estado, padre=nodo, accion=nombre)
                frontera.append(hijo)
                hijos.append(hijo)
        nodo.hijos = hijos

    return {"encontrado": False, "camino": [], "visitados": orden_visitados}


def resolver_todas_las_busquedas(estado_inicial, solucion):
    return {
        "inicial": estado_inicial,
        "solucion": solucion,
        "dfs": buscar_dfs_iterativo(estado_inicial, solucion),
        "dfs_recursiva": buscar_dfs_recursivo(estado_inicial, solucion),
        "bfs": buscar_bfs(estado_inicial, solucion),
    }
