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

    # Test 4: BCNF y 4FN. Esperamos FNBC: False y 4FN: False
    print("\nTest 4: usando la relvar original: ")
    print("¿Está en BCNF?", is_relvar_in_bcnf(relvar))
    print("¿Está en 4NF?", is_relvar_in_4nf(relvar))

    ## Test 5: BCNF y 4FN. Esperamos FNBC: True y 4FN: True
    print("\nTest 5: una relvar que está en 4FN: ")
    fd_4nf = FunctionalDependency("{ID} -> {Nombre, Correo, Telefono}")
    relvar_4nf = Relvar(
        heading=["ID", "Nombre", "Correo", "Telefono"],
        functional_dependencies=[fd_4nf],
        multivalued_dependencies=[]  # no se necesitan dependencias multivaluadas, con las funcionales basta
    )
    print(f"Nueva relvar: {relvar_4nf}")
    print("Dependencias funcionales:")
    for fd in relvar_4nf.functional_dependencies:
        print(fd)
    print("Dependencias multivaluadas:")
    for mvd in relvar_4nf.multivalued_dependencies:
        print(mvd)
        
    print("¿Está en BCNF?", is_relvar_in_bcnf(relvar_4nf))
    print("¿Está en 4NF?", is_relvar_in_4nf(relvar_4nf))

    ## Test 6: BCNF y 4FN. Esperamos FNBC: True y 4FN: False
    print("\nTest 6: usando una relvar que está en FNBC pero no en 4FN: ")
    fd1 = FunctionalDependency("{Estudiante,Clase} -> {Calificacion}")
    fd2 = FunctionalDependency("{Estudiante,Clase} -> {Libro}") 
    mvd = MultivaluedDependency("{Clase} ->-> {Libro}")

    relvar_sBCn4 = Relvar(
        heading=["Estudiante", "Clase", "Calificacion", "Libro"],
        functional_dependencies=[fd1, fd2],
        multivalued_dependencies=[mvd]
    )
    print(f"Relvar que está en FNBC pero no 4FN: {relvar_sBCn4}")
    print("Dependencias funcionales:")
    for fd in relvar_sBCn4.functional_dependencies:
        print(fd)
    print("Dependencias multivaluadas:")
    for mvd in relvar_sBCn4.multivalued_dependencies:
        print(mvd)

    print("¿Está en BCNF?", is_relvar_in_bcnf(relvar_sBCn4))
    print("¿Está en 4NF?", is_relvar_in_4nf(relvar_sBCn4))


#prueba actividades 1 y 2


from components import FunctionalDependency, MultivaluedDependency, Attribute

def test_functional_dependencies():
    print("=== FunctionalDependency Tests ===")
    # Caso 1: trivial porque {B} ⊆ {A,B}
    fd1 = FunctionalDependency("{A,B}->{B}")
    print(f"{fd1} → trivial? {fd1.is_trivial()}   # esperado: True")

    # Caso 2: no trivial porque {C} ⊄ {A,B}
    fd2 = FunctionalDependency("{A,B}->{C}")
    print(f"{fd2} → trivial? {fd2.is_trivial()}   # esperado: False")
    print()

def test_multivalued_dependencies():
    print("=== MultivaluedDependency Tests ===")
    # Definimos el esquema R = {A, B, C}
    R = {Attribute('A'), Attribute('B'), Attribute('C')}

    # Caso 1: trivial porque {B} ⊆ {A,B}
    mvd1 = MultivaluedDependency("{A,B}->->{B}")
    print(f"{mvd1} → trivial? {mvd1.is_trivial(R)}   # esperado: True")

    # Caso 2: trivial porque X∪Y == R ({A,B}∪{A,C} = {A,B,C})
    mvd2 = MultivaluedDependency("{A,B}->->{A,C}")
    print(f"{mvd2} → trivial? {mvd2.is_trivial(R)}   # esperado: True")

    # Caso 3: trivial porque X∪Y == R ({A,B}∪{C} = {A,B,C})
    mvd3 = MultivaluedDependency("{A,B}->->{C}")
    print(f"{mvd3} → trivial? {mvd3.is_trivial(R)}   # esperado: True")

if __name__ == "__main__":
    test_functional_dependencies()
    test_multivalued_dependencies()

