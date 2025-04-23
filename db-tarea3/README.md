# ITAM Primavera 2025 - Tarea de Normalización

---

## Configuración

Este proyecto no tiene dependencias adicionales de Python, por lo que no es 
necesario crear un ambiente virtual. Está desarollado y probado con Python 3.13,
pero debe funcionar con 3.8 o superior.

## Estructura

## a) components.py 
El archivo components.py define las clases fundamentales como:

1. Attribute: Representa un atributo simple en el modelo relacional.
2. Dependency: Clase abstracta base para las dependencias.
3. FunctionalDependency: Implementa las dependencias funcionales con métodos para verificar si son triviales.
4. MultivaluedDependency: Implementa las dependencias multivaluadas con su propia verificación de trivialidad.
5. Relvar: Representa una variable relacional completa con encabezado y conjuntos de dependencias.

Los algoritmos en algorithms.py operan sobre estas estructuras para realizar análisis de normalización.

## b) algorithms.py
1. closure: Calcula el cierre de un conjunto de atributos bajo un conjunto de dependencias funcionales. Es el algoritmo 2. 2.   
fundamental que permite determinar todos los atributos que se pueden derivar de un conjunto inicial.
2. is_superkey: Determina si un conjunto de atributos es una superllave para un esquema relacional. Esto pasa cuando el cierre del conjunto contiene todos los atributos del encabezado.
3. is_key: Verifica si un conjunto de atributos es una llave candidata. Para ello, debe ser una superllave y además no debe existir ningún subconjunto propio que también sea superllave.
4. is_relvar_in_bcnf: Evalúa si una variable relacional está en Forma Normal de Boyce-Codd. Una relvar está en BCNF si para toda dependencia funcional no trivial X → Y, X es una superllave.
5. is_relvar_in_4nf: Verifica si una relvar está en Cuarta Forma Normal. Para ello, debe estar en BCNF y además para toda dependencia multivaluada no trivial X →→ Y, X debe ser una superllave.

## c) example.py
Podemos encontrar ejemplos de aplicación a los métodos de components.py y algorithms.py en example.py, se incluyen descripciones de cada ejemplo de aplicación así como los valores esperados de su ejecución.
 ## Suposiciones y notas adicionales

1. Se asume que los nombres de los atributos son cadenas de caracteres (strings) simples sin espacios.
2. Las dependencias funcionales y multivaluadas se expresan como strings con el formato:
   - DF: "{X,Y,...} -> {A,B,...}"
   - DM: "{X,Y,...} ->-> {A,B,...}" 
3. Los algoritmos implementados no consideran la normalización automática, solo la verificación de formas normales.
4. Para la verificación de 4NF, se requiere que la relvar ya esté en BCNF.
5. Las dependencias triviales no influyen en las verificaciones de formas normales.
