from py2neo import Graph, Node, Relationship
owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
# fileread = open('michiel_variables.dat', 'r')
#
# def node_var(name1):
#    owfgraph.create(Node("Variable", name=name1))
#
# for line in fileread:
#     node_var(line[:-1])
#
# fileread.close()
#
# def node_mod(number):
#    owfgraph.create(Node("Model", name="m"+number))
#
# for n in range(171):
#    node_mod(str(n))

exe = owfgraph.run

model_number = 'LPC alternative'

model_desc = 'Alternative model to calculate LPC.'

var_names = ['actualised total energy yield without electrical and array losses', 'actualised total bottom lease costs', 'LPC', 'actualised total infield cable costs', 'actualised costs without bottom lease and infield cable costs', 'efficiency of electrical network', 'array efficiency']

# exe("create (v:Variable{author:'sebastian', name:'" + model_desc[0] + "'})")
# exe("match (m:Model{name:'" + model_number + "'}) set m.description='" + model_desc + "'")

for var in var_names:
    exe("match (v:Variable{name:'" + var + "'}) return v").dump()
    # exe("match (m:Model{name:'" + model_number + "'}), (v:Variable{name:'" + var + "'}) create (v)-[r:APPEARS_IN]->(m)")
#
# print model_number
