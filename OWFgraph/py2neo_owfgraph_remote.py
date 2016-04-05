__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'
from py2neo_functions import add_node, add_relationship, add_property, del_relationship, del_node, change_relationship
from py2neo import Graph
owfgraph = Graph("http://neo4j:kluyverwegwind@owfgraph.lr.tudelft.nl:7474/db/data/")
exe = owfgraph.cypher.execute

query = "match (m:)--(v) return v.name"

# print exe(query)

turbulence = {'label': 'attribute',

             'name': 'turbulence',

             'description': 'concept of turbulence in the atmosphere',

             'author': 'sebastian',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': '',

             'reference': '',

             'note': ''}

wind_direction = {'label': 'attribute',

             'name': 'wind direction',

             'description': 'concept of the direction of wind',

             'author': 'sebastian',

             'unit': '',

             'domain': '',

             'value': '',

             'expression': '',

             'reference': '',

             'note': ''}

# add_node(turbulence)
# add_node(wind_direction)

# change_relationship('attribute', 'ocean currents', 'describes', 'specifies', 'object', 'ocean')

# del_relationship('variable', 'turbulence intensity', 'describes', 'object', 'atmosphere')
# del_relationship('variable', 'wind direction', 'example', 'object', 'atmosphere')

# add_relationship('variable', 'turbulence intensity', 'describes', 'attribute', 'turbulence')
# add_relationship('attribute', 'wind direction', 'specifies', 'object', 'atmosphe

# del_node('attribute', 'wind direction')

