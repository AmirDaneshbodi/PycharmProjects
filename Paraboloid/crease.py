__author__ = 'sebasanper'

from openmdao.main.api import Component
from openmdao.lib.datatypes.api import Float
from math import sqrt


class one(Component):

    # set up interface to the framework
    x = Float(0.0, iotype='in', desc='The variable x')
    # y = Float(0.0, iotype='in', desc='The variable y')
    f = Float(0.0, iotype='out', desc='Crease length')

    def execute(self):
        """f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3
        Optimal solution (minimum): x = 6.6667; y = -7.3333
        """

        x = self.x
        # y = self.y

        # self.f = 60.0*x**2+48.0*x*y
        self.f = sqrt(x**2+x**2*3.0/(x-3.0))