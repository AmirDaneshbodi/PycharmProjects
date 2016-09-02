__author__ = 'sebasanper'

from openmdao.main.api import Component
from openmdao.lib.datatypes.api import Float


class ParaboloidScaledShift(Component):
    """ Evaluates the equation f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3 """

    # set up interface to the framework
    x = Float(0.0, iotype='in', desc='The variable x')
    y = Float(0.0, iotype='in', desc='The variable y')

    f_xy = Float(0.0, iotype='out', desc='F(x,y)')

    def execute(self):
        """f(x,y) = (x-3)^2 + xy + (y+4)^2 - 3
        Optimal solution (minimum): x = 6.6667; y = -7.3333
        """

        x = self.x
        y = self.y

        self.f_xy = (1000*x-3)**2 + (1000*x)*(0.01*(y+1000)) + (0.01*(y+1000)+4)**2 - 3