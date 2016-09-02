from openmdao.api import Problem, Group
from .Jensen_wake_main import Jensen
from .wake_CT import Ct
from .wake_total_deficit import TotalWindSpeed
from .wake_layout_order import OrderLayout

top = Problem()
root = top.root = Group()


root.add('wake', Jensen())
root.add('Ct', Ct())
root.add('speed', TotalWindSpeed())
root.add('order', OrderLayout())

root.connect('Ct.CT', 'wake.CT')
root.connect()
