from normalization.components import Relvar, FunctionalDependency, MultivaluedDependency, Attribute
from normalization.algorithms import closure, is_superkey, is_key


if __name__ == "__main__":
    fd1 = FunctionalDependency("{RFC} -> {Nombre, CP}")
    fd2 = FunctionalDependency("{FolioF} -> {RFC}")
    fd3 = FunctionalDependency("{FolioF} -> {MontoF, IVA, FechaF}")
    fd4 = FunctionalDependency("{FolioF} -> {RegimenF, CFDI}")
    fd5 = FunctionalDependency("{FolioP} -> {MontoP, FechaP}")
    fd6 = FunctionalDependency("{FolioP} -> {FolioF}")
    fd7 = FunctionalDependency("{MontoF} -> {IVA}")

    mvd1 = MultivaluedDependency("{RFC} ->-> {RegimenC}")

    relvar = Relvar(
        heading=["Nombre", "RFC", "CP", "RegimenF", "RegimenC", "CFDI", "FolioF", "MontoF", "IVA", "FechaF", "Producto", "FolioP", "MontoP", "FechaP"],
        functional_dependencies=[fd1, fd2, fd3, fd4, fd5, fd6],
        multivalued_dependencies=[mvd1]
    )

    print(f"Relvar: {relvar}")

    print("\nFunctional dependencies:")
    for fd in relvar.functional_dependencies:
        print(fd)

    print("\nMultivalued dependencies:")
    for mvd in relvar.multivalued_dependencies:
        print(mvd)
        
    # Pruebas de cierre, superllave y llave

    # Test 1: Probar con un conjunto de atributos que sabemos debe ser superllave y llave 
    atributos1 = {Attribute("FolioP"), Attribute("Producto"), Attribute("RegimenC")}
    print("\nTest 1: Atributos {Producto, FolioP, RegimenC}")
    print("Cierre de atributos:", closure(atributos1, relvar.functional_dependencies))
    print("¿Es superclave?", is_superkey(atributos1, relvar.heading, relvar.functional_dependencies))
    print("¿Es clave candidata?", is_key(atributos1, relvar.heading, relvar.functional_dependencies))

    # Test 2: No es ni superllave ni llave
    atributos2 = {Attribute("RFC")}
    print("\nTest 2: Atributo {RFC}")
    print("Cierre de atributos:", closure(atributos2, relvar.functional_dependencies))
    print("¿Es superclave?", is_superkey(atributos2, relvar.heading, relvar.functional_dependencies))
    print("¿Es clave candidata?", is_key(atributos2, relvar.heading, relvar.functional_dependencies))
    
     # Test 3: Test superllave no reducida, no es llave
    atributos3 = {Attribute("RegimenC"), Attribute("FolioP"), Attribute("Producto"), Attribute("CFDI")}
    print("\nTest 3: Atributos {RFC, FolioP, Producto}")
    print("Cierre de atributos:", closure(atributos3, relvar.functional_dependencies))
    print("¿Es superclave?", is_superkey(atributos3, relvar.heading, relvar.functional_dependencies))
    print("¿Es clave candidata?", is_key(atributos3, relvar.heading, relvar.functional_dependencies))