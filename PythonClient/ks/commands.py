# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECommandDirection(Enum):
	Up = 0
	Right = 1
	Down = 2
	Left = 3


class Move(object):

	@staticmethod
	def name():
		return 'Move'


	def __init__(self, id=None, direction=None):
		self.initialize(id, direction)
	

	def initialize(self, id=None, direction=None):
		self.id = id
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp0 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp0:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp1 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp1:
			tmp2 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = ECommandDirection(tmp2)
		else:
			self.direction = None
		
		return offset


class PlantBomb(object):

	@staticmethod
	def name():
		return 'PlantBomb'


	def __init__(self, id=None, direction=None):
		self.initialize(id, direction)
	

	def initialize(self, id=None, direction=None):
		self.id = id
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			tmp5 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = ECommandDirection(tmp5)
		else:
			self.direction = None
		
		return offset


class DefuseBomb(object):

	@staticmethod
	def name():
		return 'DefuseBomb'


	def __init__(self, id=None, direction=None):
		self.initialize(id, direction)
	

	def initialize(self, id=None, direction=None):
		self.id = id
		self.direction = direction
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.direction
		s += b'\x00' if self.direction is None else b'\x01'
		if self.direction is not None:
			s += struct.pack('b', self.direction.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.direction
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			tmp8 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.direction = ECommandDirection(tmp8)
		else:
			self.direction = None
		
		return offset
