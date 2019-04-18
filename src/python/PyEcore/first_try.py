import sys

sys.path.append('../../../../pyuml2')


from pyecore.ecore import EClass, EAttribute, EString, EObject
from pyecore.resources import ResourceSet
import pyuml2.uml as uml

def main():
    print('hallo hallo')

    Graph = EClass('Graph')   # we create a 'Graph' concept
    Node = EClass('Node')     # We create a 'Node' concept

    print(Graph)

    rset = ResourceSet()
    rset.metamodel_registry[uml.nsURI] = uml
    ressource = rset.get_resource('model/PyEcore_Test.uml')
    print(ressource.contents)
    for obj in ressource.contents:
        print('\t{0}'.format(obj))
    model = ressource.contents[0]

    print(model.name)
    print(model.__dict__.keys())
    print(model.__dict__['packagedElement'][0].name)
    # print(model.packagedElement)
    # for el in model.packagedElement:
    #     print(el.name)
    #     for el1 in el.packagedElement:
    #         print('\t{0}'.format(el1.name))
    #         print('\t\t{0}'.format(type(el1)))
    #         if isinstance(el1, uml.uml.Class):
    #             print('\t\tClass : '.format(el1.name))
    #             print(el1.__dict__.keys())
    #             print(el1.ownedAttribute.__dict__)
    # print(model.nestedPackage)


if __name__ == '__main__':
    main()