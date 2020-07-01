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

 También dispone de un método de clase `random_graph`, que genera un método aleatorio.

El módulo closest string incluye unicamente dos funciones: `closest_string` y `minimum_distance`. Estas funciones trabajan sobre la clase bitarray que se puede encontrar [aquí](https://pypi.org/project/bitarray/).

El módulo `qbf` incluye la clase `naiveQBF` que provee un esqueleto para la resolucion de fórmulas cuantificadas.


- `append_formula`
- `propagate_literal`
- `add_clause`
- `add_quantifiers`
- `negate`
- `__solve`
- `solve`

Para más información sobre cualquiera de los métodos o funciones, por favor, lea la documentación asociada (docstring). El módulo `utility` es usado por nosotros para realizar algunas tareas transecionales del desarrollo de los módulos. Sin embargo las funciones están disponibles y documentadas para aquellos interesados en reducir problemas a SAT, aunque este no es el proposito principal de la clase. 

Los módulos `closest_string` y `graph` están implementadas con acceso a (logging)[https://docs.python.org/3/howto/logging.html#logging-basic-tutorial].


## Test

En la carpeta test tenemos diversos script que implementant test classes basados en `unittest`. Para ejecutarlos, corra la orden

```
python -m test.my_testfyle
```

desde este directorio. 
