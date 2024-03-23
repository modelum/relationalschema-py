
from .relationalschema import getEClassifier, eClassifiers
from .relationalschema import name, nsURI, nsPrefix, eClass
from .relationalschema import NamedElement, RelationalSchema, Table, Column, Key, FKey, ReferentialAction


from . import relationalschema

__all__ = ['NamedElement', 'RelationalSchema', 'Table',
           'Column', 'Key', 'FKey', 'ReferentialAction']

eSubpackages = []
eSuperPackage = None
relationalschema.eSubpackages = eSubpackages
relationalschema.eSuperPackage = eSuperPackage

Key.columns.eType = Column
FKey.columns.eType = Column
FKey.refsTo.eType = Key
RelationalSchema.tables.eType = Table
Table.columns.eType = Column
Table.keys.eType = Key
Table.fks.eType = FKey
Table.owner.eType = RelationalSchema
Table.owner.eOpposite = RelationalSchema.tables
Column.owner.eType = Table
Column.owner.eOpposite = Table.columns
Key.owner.eType = Table
Key.owner.eOpposite = Table.keys
FKey.owner.eType = Table
FKey.owner.eOpposite = Table.fks

otherClassifiers = [ReferentialAction]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
