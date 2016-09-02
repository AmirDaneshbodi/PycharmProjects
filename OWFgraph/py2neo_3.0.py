from py2neo import Node, Relationship, Graph, authenticate
from py2neo_v3_functions import DESCRIBES, change_label, change_property, change_relationship, create_node, \
    create_property, create_relationship, delete_node, delete_relationship, make_node, neighbours, find, RELATES_TO, add_label

# authenticate("owfgraph.lr.tudelft.nl:7474", "neo4j", "kluyverweg")
# owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
# localgraph = Graph("http://neo4j:neo4j@localhost:7474/db/data/")
# owfgraph = Graph("http://owfgraph.lr.tudelft.nl:7474/db/data/")

procedure = 'procedure'
attribute = 'attribute'
variable = 'variable'
object_ = 'object'
model = 'model'
describes = 'DESCRIBES'
partof = 'PART_OF'
inputto = 'INPUT_TO'
outputof = 'OUTPUT_OF'
appearsin = 'APPEARS_IN'
variantof = 'VARIANT_OF'
instructs = 'INSTRUCTS'
description = 'description'
unit = 'unit'
value = 'value'
domain = 'domain'
name = 'name'
reference = 'reference'


sxcvtr = {'label': attribute,

             'name': 'structure of the support structure',

             'author': 'sebastian',

             'description': '',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': '',

             'reference': '',

             'note': ''}

f2 = {'label': attribute,

             'name': 'monopile state',

             'author': 'sebastian',

             'description': '',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': '',

             'reference': '',

             'note': ''}


# find('area of incidence of partial wake or multiple wake overlap')

# change_label('MBZ13', 'thrust coefficient', 'Mbz13')
# add_label(variable, 'annual energy production', 'Mbz13')
# change_relationship(variable, 'set of wind turbines', inputto, describes, attribute, 'OWF structure')

create_node(f2)
# create_node(assembly)
# create_node(rna_cost)

# del_relationship('variable', 'distance to coast', 'describes', 'object', 'site')

# delete_node(variable, 'electricity production')

# change_property(model, 'drag coefficient', name, 'drag coefficient of the support structure')

# change_property(variable, 'inertia coefficient', name, 'inertia coefficient of the support structure')

create_relationship(attribute, 'monopile state', describes, object_, 'monopile')
create_relationship(variable, 'lateral force on pile at mudline', describes, attribute, 'monopile state')


# delete_relationship('variable', 'costs of operation and maintenance excluding management costs', 'describes', 'attribute', 'OWF cost')

create_property(variable, 'lateral force on pile at mudline', domain, 'real')
#
create_property(variable, 'lateral force on pile at mudline', unit, 'N')

# create_property(variable, 'annual loss in electrical infrastructure', description, 'Annual energy losses in the whole electrical connection system.')

# delete_node('object', 'foundation')

# neighbours('attribute', 'availability of owf')