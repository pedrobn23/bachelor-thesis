# Desarrollo de código

En esta carpeta encontramos el desarrollo de código realizado. A su vez, al dividimos en dos subcarpetas:

- `SATreduce`: realizamos el desarrollo de la biblioteca, descrita en la sección 7 del trabajo.
- `test`: realizamos casos de prueba para automatizar los test de mantenimiento de cada clase.

A continuación describiremos la estructura interna de cada clase así como su funcionalidad y como utilizar su contenido. 

## SATreduce

Esta es una biblioteca que implementa varias reducciones de problemas NP-Duros a SAT. Disponemos de tres módulos principales: `graph`, `closest\_string` y `qbf`.

<p align="center">
  <img width="460" src="https://github.com/pedrobn23/TFG/blob/master/tesis/img/distribucion.png">
</p>
<p align="center">
	Representación de los distintos módulos incluidos en la biblioteca. En gris podemos ver las reducciones realizadas en cada módulo.
</p>

El módulo `graph` incluye la clase `Graph`. Esta realiza una representación de un grafo basado en un diccionario, donde cada nodo está emparejado con un objeto de tipo `set` que contiene todos los nodos adyacentes a él. Consideramos grafos no-dirigidos y sin múltiples caminos entre nodo y nodo. Esta clase dispone de los métodos de objeto:
- `vertices`
- `edges`
- `add_vertex`
- `add_edge`
- `add_from_text`
- `iterate_edges`
- `find_hamiltonian_path`
- `coloring`
- `minimun_coloring`
- `dominating_subset`
- `minimun_dominating_subset`

Para más información sobre estos métodos, por favor, lea la documentación asociada (docstring). También dispone de un método de clase `random_graph`, que genera un método aleatorio.



