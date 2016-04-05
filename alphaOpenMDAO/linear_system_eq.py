# __author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
#
# from openmdao.api import Component, Group, Problem
#
#
# class Eq1(Component):
#     def __init__(self):
#         super(Eq1, self).__init__()
#         self.add_param('x', val=0.0)
#         self.add_param('y', val=0.0)
#         self.add_param('z', val=0.0)
#         self.add_state('res', val=0.0)
#
#     def apply_linear(self, params, unknown, resids):
#         resids['res'] = 2.0 * params['x'] + params['y'] + 3.0 * params['z'] - 1.0
#
#
# class Eq2(Component):
#     def __init__(self):
#         super(Eq2, self).__init__()
#         self.add_param('x', val=0.0)
#         self.add_param('y', val=0.0)
#         self.add_param('z', val=0.0)
#         self.add_state('res', val=0.0)
#
#     def apply_linear(self, params, unknown, resids):
#         resids['res'] = 2.0 * params['x'] + 6.0 * params['y'] + 8.0 * params['z'] - 3.0
#
#
# class Eq3(Component):
#     def __init__(self):
#         super(Eq3, self).__init__()
#         self.add_param('x', val=0.0)
#         self.add_param('y', val=0.0)
#         self.add_param('z', val=0.0)
#         self.add_state('res', val=0.0)
#
#     def apply_linear(self, params, unknown, resids):
#         resids['res'] = 6.0 * params['x'] + 8.0 * params['y'] + 18.0 * params['z'] - 5.0
#
#
# comp1 = Eq1()
# comp2 = Eq2()
# comp3 = Eq3()
#
# group = Group()
# group.add('comp1', comp1, promotes=['x', 'y', 'z'])
# group.add('comp2', comp2, promotes=['x', 'y', 'z'])
# group.add('comp3', comp3, promotes=['x', 'y', 'z'])
#
# root = group
#
# problem = Problem(root)
# problem.setup()
# problem.run()
#
# print problem.root.x, problem.root.y, problem.root.z

from scipy.sparse.linalg import gmres
from numpy import matrix, array

A = matrix('1.0 0.0 1.0; 0.0 -3.0 1.0; 2.0 1.0 3.0')
b = array([6.0, 7.0, 15.0])

print gmres(A, b)[0]