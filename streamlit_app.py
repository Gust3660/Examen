import streamlit as st

from busqueda.logic import parse_estado, resolver_todas_las_busquedas


def formatear_estado(estado):
    return " ".join(str(x) for x in estado)


def mostrar_resultado(nombre, resultado):
    if resultado["encontrado"]:
        st.success(f"{nombre} encontró solución en {len(resultado['camino']) - 1} pasos.")
    else:
        st.error(f"{nombre} no encontró solución con el estado objetivo proporcionado.")

    if resultado["camino"]:
        st.markdown("**Camino de solución**")
        for paso in resultado["camino"]:
            accion = paso["accion"] or "Inicio"
            st.write(f"- **{accion}**: `{formatear_estado(paso['estado'])}`")

    if resultado["visitados"]:
        st.markdown("**Estados visitados**")
        st.write([formatear_estado(estado) for estado in resultado["visitados"]])


def main():
    st.set_page_config(page_title="Buscador de estados", layout="centered")
    st.title("Buscador de estados")
    st.write(
        "Ingresa un estado inicial y un estado objetivo para comparar los algoritmos DFS, DFS recursivo y BFS."
    )

    estado_inicial = st.text_input("Estado inicial", "4 2 3 1")
    estado_objetivo = st.text_input("Estado objetivo", "1 2 3 4")

    if st.button("Resolver"):
        inicial = parse_estado(estado_inicial)
        objetivo = parse_estado(estado_objetivo)

        if not inicial or not objetivo:
            st.error("Ingresa ambos estados en un formato válido, por ejemplo: 4 2 3 1")
            return

        if len(inicial) != len(objetivo):
            st.error("El estado inicial y el estado objetivo deben tener la misma cantidad de elementos.")
            return

        st.markdown("---")
        resultados = resolver_todas_las_busquedas(inicial, objetivo)

        st.header("Resultados")
        mostrar_resultado("DFS iterativo", resultados["dfs"])
        st.markdown("---")
        mostrar_resultado("DFS recursivo", resultados["dfs_recursiva"])
        st.markdown("---")
        mostrar_resultado("BFS", resultados["bfs"])

        st.info("Los resultados se basan en los operadores de intercambio definidos en el modelo.")


if __name__ == "__main__":
    main()

