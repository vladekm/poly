import zope.interface as interface

from library import Polygon


class IMonogonProvides(interface.Interface):
    def create():
        pass

    def read():
        pass

    def update():
        pass

    def delete():
        pass


class Monogon(Polygon):
    def __init__(self):
        needs = {}
        provides = {
            'input':{
                'interface': IMonogonProvides,
            }
        }
        super(Monogon, self).__init__(provides, needs)


class BrokenInterface(Exception):
    pass
