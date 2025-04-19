from .components import FunctionalDependency, Attribute, Relvar


def closure(attributes: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> set[Attribute]:
    closure_set = set(attributes)
    changed = True

    while changed:
        changed = False
        for fd in functional_dependencies:
            if fd.determinant.issubset(closure_set):
                new_attributes = fd.dependant - closure_set
                if new_attributes:
                    closure_set.update(new_attributes)
                    changed = True

    return closure_set



def is_superkey(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
   return closure(attributes, functional_dependencies) == heading


def is_key(attributes: set[Attribute], heading: set[Attribute], functional_dependencies: set[FunctionalDependency]) -> bool:
    superkey = is_superkey(attributes, heading, functional_dependencies)
    reduced = True

    for attr in attributes:
        subset = attributes - {attr}
        if is_superkey(subset, heading, functional_dependencies):
            reduced = False

    return superkey and reduced


def is_relvar_in_bcnf(relvar: Relvar):
    bcnf = True
    for fd in relvar.functional_dependencies:
        if not fd.is_trivial() and not is_superkey(fd.determinant, relvar.heading, relvar.functional_dependencies):
            bcnf = False
            break
    return bcnf


def is_relvar_in_4nf(relvar: Relvar):
    # TODO: Actividad 7
    raise NotImplementedError()
