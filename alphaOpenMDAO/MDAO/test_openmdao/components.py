from openmdao.api import Component, Problem, Group, IndepVarComp


class Comp1(Component):
    def __init__(self):
        super(Comp1, self).__init__()

        self.add_param('x', val=[1,2,3])
        self.add_param('d')
        self.add_output('b', shape=1)
        self.add_output('z', shape=1)

    def solve_nonlinear(self, params, unknowns, resids):

        x = params['x']
        a = 0.0
        for b in x:
            unknowns['b'] = b
            d = params['d']
            a += d ** 2.0

        unknowns['z'] = a


class Comp2(Component):
    def __init__(self):
        super(Comp2, self).__init__()

        self.add_param('y')
        self.add_output('w', shape=1)

    def solve_nonlinear(self, params, unknowns, resids):

        y = params['y']
        unknowns['w'] = y + 3.0

if __name__ == '__main__':
    top = Problem()
    root = top.root = Group()

    root.add('mycomp2', Comp2())
    root.add('mycomp1', Comp1())

    root.connect('mycomp1.b', 'mycomp2.y')
    root.connect('mycomp2.w', 'mycomp1.d')

    top.setup()
    top.run()

    print(top['mycomp1.z'])
