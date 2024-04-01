"""Definition of meta model 'relationalschema'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'relationalschema'
nsURI = 'http://www.modelum.es/relationalschema'
nsPrefix = 'relationalschema'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ReferentialAction = EEnum('ReferentialAction', literals=[
                          'NO_ACTION', 'CASCADE', 'SET_NULL', 'SET_DEFAULT'])


class NamedElement(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name


class Key(EObject, metaclass=MetaEClass):

    constraintname = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    isPK = EAttribute(eType=EBoolean, unique=True, derived=False,
                      changeable=True, default_value=True)
    columns = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    owner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, columns=None, constraintname=None, owner=None, isPK=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if constraintname is not None:
            self.constraintname = constraintname

        if isPK is not None:
            self.isPK = isPK

        if columns:
            self.columns.extend(columns)

        if owner is not None:
            self.owner = owner


class FKey(EObject, metaclass=MetaEClass):

    onDelete = EAttribute(eType=ReferentialAction, unique=True, derived=False,
                          changeable=True, default_value=ReferentialAction.NO_ACTION)
    onUpdate = EAttribute(eType=ReferentialAction, unique=True, derived=False,
                          changeable=True, default_value=ReferentialAction.CASCADE)
    constraintname = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    columns = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    refsTo = EReference(ordered=True, unique=True, containment=False, derived=False)
    owner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, columns=None, refsTo=None, onDelete=None, onUpdate=None, constraintname=None, owner=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if onDelete is not None:
            self.onDelete = onDelete

        if onUpdate is not None:
            self.onUpdate = onUpdate

        if constraintname is not None:
            self.constraintname = constraintname

        if columns:
            self.columns.extend(columns)

        if refsTo is not None:
            self.refsTo = refsTo

        if owner is not None:
            self.owner = owner


class RelationalSchema(NamedElement):

    version = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    location = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    tables = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, version=None, tables=None, location=None, **kwargs):

        super().__init__(**kwargs)

        if version is not None:
            self.version = version

        if location is not None:
            self.location = location

        if tables:
            self.tables.extend(tables)


class Table(NamedElement):

    columns = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    keys = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    fks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    owner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, columns=None, keys=None, fks=None, owner=None, **kwargs):

        super().__init__(**kwargs)

        if columns:
            self.columns.extend(columns)

        if keys:
            self.keys.extend(keys)

        if fks:
            self.fks.extend(fks)

        if owner is not None:
            self.owner = owner


class Column(NamedElement):

    datatype = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    size = EAttribute(eType=EInt, unique=True, derived=False, changeable=True, default_value=0)
    nullable = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=False)
    defaultvalue = EAttribute(eType=EString, unique=True, derived=False,
                              changeable=True, default_value='NULL')
    owner = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, datatype=None, size=None, nullable=None, defaultvalue=None, owner=None, **kwargs):

        super().__init__(**kwargs)

        if datatype is not None:
            self.datatype = datatype

        if size is not None:
            self.size = size

        if nullable is not None:
            self.nullable = nullable

        if defaultvalue is not None:
            self.defaultvalue = defaultvalue

        if owner is not None:
            self.owner = owner
