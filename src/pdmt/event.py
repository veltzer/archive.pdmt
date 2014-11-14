'''
These are events which a user of the core can register
to
'''

import enum # for Enum

class Event(enum.Enum):
	nodepreadd=1
	nodepostadd=2
	nodepredel=3
	nodepostdel=4
	edgepreadd=5
	edgepostadd=6
	edgepredel=7
	edgepostdel=8
	nodeprebuild=9
	nodepostbuild=10
