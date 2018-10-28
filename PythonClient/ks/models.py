# -*- coding: utf-8 -*-

# python imports
import sys
import struct
from enum import Enum

PY3 = sys.version_info > (3,)


class ECell(Enum):
	Empty = 0
	SmallBombSite = 1
	MediumBombSite = 2
	LargeBombSite = 3
	VastBombSite = 4
	Wall = 5


class EDirection(Enum):
	Up = 0
	Right = 1
	Down = 2
	Left = 3


class ESoundIntensity(Enum):
	Weak = 0
	Normal = 1
	Strong = 2


class Constants(object):

	@staticmethod
	def name():
		return 'Constants'


	def __init__(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, terrorist_vision_distance=None, terrorist_arrest_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
		self.initialize(bomb_planting_time, bomb_defusion_time, bomb_explosion_time, bomb_planting_score, bomb_defusion_score, bomb_explosion_score, terrorist_vision_distance, terrorist_arrest_score, police_vision_distance, sound_ranges, max_cycles)
	

	def initialize(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, terrorist_vision_distance=None, terrorist_arrest_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
		self.bomb_planting_time = bomb_planting_time
		self.bomb_defusion_time = bomb_defusion_time
		self.bomb_explosion_time = bomb_explosion_time
		self.bomb_planting_score = bomb_planting_score
		self.bomb_defusion_score = bomb_defusion_score
		self.bomb_explosion_score = bomb_explosion_score
		self.terrorist_vision_distance = terrorist_vision_distance
		self.terrorist_arrest_score = terrorist_arrest_score
		self.police_vision_distance = police_vision_distance
		self.sound_ranges = sound_ranges
		self.max_cycles = max_cycles
	

	def serialize(self):
		s = b''
		
		# serialize self.bomb_planting_time
		s += b'\x00' if self.bomb_planting_time is None else b'\x01'
		if self.bomb_planting_time is not None:
			s += struct.pack('i', self.bomb_planting_time)
		
		# serialize self.bomb_defusion_time
		s += b'\x00' if self.bomb_defusion_time is None else b'\x01'
		if self.bomb_defusion_time is not None:
			s += struct.pack('i', self.bomb_defusion_time)
		
		# serialize self.bomb_explosion_time
		s += b'\x00' if self.bomb_explosion_time is None else b'\x01'
		if self.bomb_explosion_time is not None:
			s += struct.pack('i', self.bomb_explosion_time)
		
		# serialize self.bomb_planting_score
		s += b'\x00' if self.bomb_planting_score is None else b'\x01'
		if self.bomb_planting_score is not None:
			s += struct.pack('i', self.bomb_planting_score)
		
		# serialize self.bomb_defusion_score
		s += b'\x00' if self.bomb_defusion_score is None else b'\x01'
		if self.bomb_defusion_score is not None:
			s += struct.pack('i', self.bomb_defusion_score)
		
		# serialize self.bomb_explosion_score
		s += b'\x00' if self.bomb_explosion_score is None else b'\x01'
		if self.bomb_explosion_score is not None:
			s += struct.pack('i', self.bomb_explosion_score)
		
		# serialize self.terrorist_vision_distance
		s += b'\x00' if self.terrorist_vision_distance is None else b'\x01'
		if self.terrorist_vision_distance is not None:
			s += struct.pack('i', self.terrorist_vision_distance)
		
		# serialize self.terrorist_arrest_score
		s += b'\x00' if self.terrorist_arrest_score is None else b'\x01'
		if self.terrorist_arrest_score is not None:
			s += struct.pack('i', self.terrorist_arrest_score)
		
		# serialize self.police_vision_distance
		s += b'\x00' if self.police_vision_distance is None else b'\x01'
		if self.police_vision_distance is not None:
			s += struct.pack('i', self.police_vision_distance)
		
		# serialize self.sound_ranges
		s += b'\x00' if self.sound_ranges is None else b'\x01'
		if self.sound_ranges is not None:
			tmp0 = b''
			tmp0 += struct.pack('I', len(self.sound_ranges))
			while len(tmp0) and tmp0[-1] == b'\x00'[0]:
				tmp0 = tmp0[:-1]
			s += struct.pack('B', len(tmp0))
			s += tmp0
			
			for tmp1 in self.sound_ranges:
				s += b'\x00' if tmp1 is None else b'\x01'
				if tmp1 is not None:
					s += struct.pack('b', tmp1.value)
				s += b'\x00' if self.sound_ranges[tmp1] is None else b'\x01'
				if self.sound_ranges[tmp1] is not None:
					s += struct.pack('i', self.sound_ranges[tmp1])
		
		# serialize self.max_cycles
		s += b'\x00' if self.max_cycles is None else b'\x01'
		if self.max_cycles is not None:
			s += struct.pack('i', self.max_cycles)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.bomb_planting_time
		tmp2 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp2:
			self.bomb_planting_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_planting_time = None
		
		# deserialize self.bomb_defusion_time
		tmp3 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp3:
			self.bomb_defusion_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_defusion_time = None
		
		# deserialize self.bomb_explosion_time
		tmp4 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp4:
			self.bomb_explosion_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_explosion_time = None
		
		# deserialize self.bomb_planting_score
		tmp5 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp5:
			self.bomb_planting_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_planting_score = None
		
		# deserialize self.bomb_defusion_score
		tmp6 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp6:
			self.bomb_defusion_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_defusion_score = None
		
		# deserialize self.bomb_explosion_score
		tmp7 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp7:
			self.bomb_explosion_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.bomb_explosion_score = None
		
		# deserialize self.terrorist_vision_distance
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.terrorist_vision_distance = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.terrorist_vision_distance = None
		
		# deserialize self.terrorist_arrest_score
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.terrorist_arrest_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.terrorist_arrest_score = None
		
		# deserialize self.police_vision_distance
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.police_vision_distance = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.police_vision_distance = None
		
		# deserialize self.sound_ranges
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp13 = s[offset:offset + tmp12]
			offset += tmp12
			tmp13 += b'\x00' * (4 - tmp12)
			tmp14 = struct.unpack('I', tmp13)[0]
			
			self.sound_ranges = {}
			for tmp15 in range(tmp14):
				tmp18 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp18:
					tmp19 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp16 = ESoundIntensity(tmp19)
				else:
					tmp16 = None
				tmp20 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp20:
					tmp17 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp17 = None
				self.sound_ranges[tmp16] = tmp17
		else:
			self.sound_ranges = None
		
		# deserialize self.max_cycles
		tmp21 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp21:
			self.max_cycles = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.max_cycles = None
		
		return offset


class Position(object):

	@staticmethod
	def name():
		return 'Position'


	def __init__(self, x=None, y=None):
		self.initialize(x, y)
	

	def initialize(self, x=None, y=None):
		self.x = x
		self.y = y
	

	def serialize(self):
		s = b''
		
		# serialize self.x
		s += b'\x00' if self.x is None else b'\x01'
		if self.x is not None:
			s += struct.pack('i', self.x)
		
		# serialize self.y
		s += b'\x00' if self.y is None else b'\x01'
		if self.y is not None:
			s += struct.pack('i', self.y)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.x
		tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp22:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp23:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset


class Bomb(object):

	@staticmethod
	def name():
		return 'Bomb'


	def __init__(self, position=None, explosion_remaining_time=None):
		self.initialize(position, explosion_remaining_time)
	

	def initialize(self, position=None, explosion_remaining_time=None):
		self.position = position
		self.explosion_remaining_time = explosion_remaining_time
	

	def serialize(self):
		s = b''
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.explosion_remaining_time
		s += b'\x00' if self.explosion_remaining_time is None else b'\x01'
		if self.explosion_remaining_time is not None:
			s += struct.pack('i', self.explosion_remaining_time)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.position
		tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp24:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.explosion_remaining_time
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
			self.explosion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.explosion_remaining_time = None
		
		return offset


class Terrorist(object):

	@staticmethod
	def name():
		return 'Terrorist'


	def __init__(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, is_arrested=None):
		self.initialize(id, position, planting_remaining_time, footstep_sounds, is_arrested)
	

	def initialize(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, is_arrested=None):
		self.id = id
		self.position = position
		self.planting_remaining_time = planting_remaining_time
		self.footstep_sounds = footstep_sounds
		self.is_arrested = is_arrested
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.planting_remaining_time
		s += b'\x00' if self.planting_remaining_time is None else b'\x01'
		if self.planting_remaining_time is not None:
			s += struct.pack('i', self.planting_remaining_time)
		
		# serialize self.footstep_sounds
		s += b'\x00' if self.footstep_sounds is None else b'\x01'
		if self.footstep_sounds is not None:
			tmp26 = b''
			tmp26 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp26) and tmp26[-1] == b'\x00'[0]:
				tmp26 = tmp26[:-1]
			s += struct.pack('B', len(tmp26))
			s += tmp26
			
			for tmp27 in self.footstep_sounds:
				s += b'\x00' if tmp27 is None else b'\x01'
				if tmp27 is not None:
					s += struct.pack('i', tmp27)
		
		# serialize self.is_arrested
		s += b'\x00' if self.is_arrested is None else b'\x01'
		if self.is_arrested is not None:
			s += struct.pack('?', self.is_arrested)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.planting_remaining_time
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.planting_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planting_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp33 = s[offset:offset + tmp32]
			offset += tmp32
			tmp33 += b'\x00' * (4 - tmp32)
			tmp34 = struct.unpack('I', tmp33)[0]
			
			self.footstep_sounds = []
			for tmp35 in range(tmp34):
				tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp37:
					tmp36 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp36 = None
				self.footstep_sounds.append(tmp36)
		else:
			self.footstep_sounds = None
		
		# deserialize self.is_arrested
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.is_arrested = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_arrested = None
		
		return offset


class Police(object):

	@staticmethod
	def name():
		return 'Police'


	def __init__(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, bomb_sounds=None, is_visible=None):
		self.initialize(id, position, defusion_remaining_time, footstep_sounds, bomb_sounds, is_visible)
	

	def initialize(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, bomb_sounds=None, is_visible=None):
		self.id = id
		self.position = position
		self.defusion_remaining_time = defusion_remaining_time
		self.footstep_sounds = footstep_sounds
		self.bomb_sounds = bomb_sounds
		self.is_visible = is_visible
	

	def serialize(self):
		s = b''
		
		# serialize self.id
		s += b'\x00' if self.id is None else b'\x01'
		if self.id is not None:
			s += struct.pack('i', self.id)
		
		# serialize self.position
		s += b'\x00' if self.position is None else b'\x01'
		if self.position is not None:
			s += self.position.serialize()
		
		# serialize self.defusion_remaining_time
		s += b'\x00' if self.defusion_remaining_time is None else b'\x01'
		if self.defusion_remaining_time is not None:
			s += struct.pack('i', self.defusion_remaining_time)
		
		# serialize self.footstep_sounds
		s += b'\x00' if self.footstep_sounds is None else b'\x01'
		if self.footstep_sounds is not None:
			tmp39 = b''
			tmp39 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp39) and tmp39[-1] == b'\x00'[0]:
				tmp39 = tmp39[:-1]
			s += struct.pack('B', len(tmp39))
			s += tmp39
			
			for tmp40 in self.footstep_sounds:
				s += b'\x00' if tmp40 is None else b'\x01'
				if tmp40 is not None:
					s += struct.pack('i', tmp40)
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp41 = b''
			tmp41 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp41) and tmp41[-1] == b'\x00'[0]:
				tmp41 = tmp41[:-1]
			s += struct.pack('B', len(tmp41))
			s += tmp41
			
			for tmp42 in self.bomb_sounds:
				s += b'\x00' if tmp42 is None else b'\x01'
				if tmp42 is not None:
					s += struct.pack('i', tmp42)
		
		# serialize self.is_visible
		s += b'\x00' if self.is_visible is None else b'\x01'
		if self.is_visible is not None:
			s += struct.pack('?', self.is_visible)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp43:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp48 = s[offset:offset + tmp47]
			offset += tmp47
			tmp48 += b'\x00' * (4 - tmp47)
			tmp49 = struct.unpack('I', tmp48)[0]
			
			self.footstep_sounds = []
			for tmp50 in range(tmp49):
				tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp52:
					tmp51 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp51 = None
				self.footstep_sounds.append(tmp51)
		else:
			self.footstep_sounds = None
		
		# deserialize self.bomb_sounds
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp55 = s[offset:offset + tmp54]
			offset += tmp54
			tmp55 += b'\x00' * (4 - tmp54)
			tmp56 = struct.unpack('I', tmp55)[0]
			
			self.bomb_sounds = []
			for tmp57 in range(tmp56):
				tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp59:
					tmp58 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp58 = None
				self.bomb_sounds.append(tmp58)
		else:
			self.bomb_sounds = None
		
		# deserialize self.is_visible
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			self.is_visible = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_visible = None
		
		return offset


class World(object):

	@staticmethod
	def name():
		return 'World'


	def __init__(self, width=None, height=None, board=None, scores=None, bombs=None, terrorists=None, polices=None, constants=None):
		self.initialize(width, height, board, scores, bombs, terrorists, polices, constants)
	

	def initialize(self, width=None, height=None, board=None, scores=None, bombs=None, terrorists=None, polices=None, constants=None):
		self.width = width
		self.height = height
		self.board = board
		self.scores = scores
		self.bombs = bombs
		self.terrorists = terrorists
		self.polices = polices
		self.constants = constants
	

	def serialize(self):
		s = b''
		
		# serialize self.width
		s += b'\x00' if self.width is None else b'\x01'
		if self.width is not None:
			s += struct.pack('i', self.width)
		
		# serialize self.height
		s += b'\x00' if self.height is None else b'\x01'
		if self.height is not None:
			s += struct.pack('i', self.height)
		
		# serialize self.board
		s += b'\x00' if self.board is None else b'\x01'
		if self.board is not None:
			tmp61 = b''
			tmp61 += struct.pack('I', len(self.board))
			while len(tmp61) and tmp61[-1] == b'\x00'[0]:
				tmp61 = tmp61[:-1]
			s += struct.pack('B', len(tmp61))
			s += tmp61
			
			for tmp62 in self.board:
				s += b'\x00' if tmp62 is None else b'\x01'
				if tmp62 is not None:
					tmp63 = b''
					tmp63 += struct.pack('I', len(tmp62))
					while len(tmp63) and tmp63[-1] == b'\x00'[0]:
						tmp63 = tmp63[:-1]
					s += struct.pack('B', len(tmp63))
					s += tmp63
					
					for tmp64 in tmp62:
						s += b'\x00' if tmp64 is None else b'\x01'
						if tmp64 is not None:
							s += struct.pack('b', tmp64.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp65 = b''
			tmp65 += struct.pack('I', len(self.scores))
			while len(tmp65) and tmp65[-1] == b'\x00'[0]:
				tmp65 = tmp65[:-1]
			s += struct.pack('B', len(tmp65))
			s += tmp65
			
			for tmp66 in self.scores:
				s += b'\x00' if tmp66 is None else b'\x01'
				if tmp66 is not None:
					tmp67 = b''
					tmp67 += struct.pack('I', len(tmp66))
					while len(tmp67) and tmp67[-1] == b'\x00'[0]:
						tmp67 = tmp67[:-1]
					s += struct.pack('B', len(tmp67))
					s += tmp67
					
					s += tmp66.encode('ISO-8859-1') if PY3 else tmp66
				s += b'\x00' if self.scores[tmp66] is None else b'\x01'
				if self.scores[tmp66] is not None:
					s += struct.pack('i', self.scores[tmp66])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp68 = b''
			tmp68 += struct.pack('I', len(self.bombs))
			while len(tmp68) and tmp68[-1] == b'\x00'[0]:
				tmp68 = tmp68[:-1]
			s += struct.pack('B', len(tmp68))
			s += tmp68
			
			for tmp69 in self.bombs:
				s += b'\x00' if tmp69 is None else b'\x01'
				if tmp69 is not None:
					s += tmp69.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp70 = b''
			tmp70 += struct.pack('I', len(self.terrorists))
			while len(tmp70) and tmp70[-1] == b'\x00'[0]:
				tmp70 = tmp70[:-1]
			s += struct.pack('B', len(tmp70))
			s += tmp70
			
			for tmp71 in self.terrorists:
				s += b'\x00' if tmp71 is None else b'\x01'
				if tmp71 is not None:
					s += tmp71.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp72 = b''
			tmp72 += struct.pack('I', len(self.polices))
			while len(tmp72) and tmp72[-1] == b'\x00'[0]:
				tmp72 = tmp72[:-1]
			s += struct.pack('B', len(tmp72))
			s += tmp72
			
			for tmp73 in self.polices:
				s += b'\x00' if tmp73 is None else b'\x01'
				if tmp73 is not None:
					s += tmp73.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp74 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp74:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp75 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp75:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp76:
			tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp78 = s[offset:offset + tmp77]
			offset += tmp77
			tmp78 += b'\x00' * (4 - tmp77)
			tmp79 = struct.unpack('I', tmp78)[0]
			
			self.board = []
			for tmp80 in range(tmp79):
				tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp82:
					tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp84 = s[offset:offset + tmp83]
					offset += tmp83
					tmp84 += b'\x00' * (4 - tmp83)
					tmp85 = struct.unpack('I', tmp84)[0]
					
					tmp81 = []
					for tmp86 in range(tmp85):
						tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp88:
							tmp89 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp87 = ECell(tmp89)
						else:
							tmp87 = None
						tmp81.append(tmp87)
				else:
					tmp81 = None
				self.board.append(tmp81)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp90:
			tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp92 = s[offset:offset + tmp91]
			offset += tmp91
			tmp92 += b'\x00' * (4 - tmp91)
			tmp93 = struct.unpack('I', tmp92)[0]
			
			self.scores = {}
			for tmp94 in range(tmp93):
				tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp97:
					tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp99 = s[offset:offset + tmp98]
					offset += tmp98
					tmp99 += b'\x00' * (4 - tmp98)
					tmp100 = struct.unpack('I', tmp99)[0]
					
					tmp95 = s[offset:offset + tmp100].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp100]
					offset += tmp100
				else:
					tmp95 = None
				tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp101:
					tmp96 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp96 = None
				self.scores[tmp95] = tmp96
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp102:
			tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp104 = s[offset:offset + tmp103]
			offset += tmp103
			tmp104 += b'\x00' * (4 - tmp103)
			tmp105 = struct.unpack('I', tmp104)[0]
			
			self.bombs = []
			for tmp106 in range(tmp105):
				tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp108:
					tmp107 = Bomb()
					offset = tmp107.deserialize(s, offset)
				else:
					tmp107 = None
				self.bombs.append(tmp107)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp109:
			tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp111 = s[offset:offset + tmp110]
			offset += tmp110
			tmp111 += b'\x00' * (4 - tmp110)
			tmp112 = struct.unpack('I', tmp111)[0]
			
			self.terrorists = []
			for tmp113 in range(tmp112):
				tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp115:
					tmp114 = Terrorist()
					offset = tmp114.deserialize(s, offset)
				else:
					tmp114 = None
				self.terrorists.append(tmp114)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp116:
			tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp118 = s[offset:offset + tmp117]
			offset += tmp117
			tmp118 += b'\x00' * (4 - tmp117)
			tmp119 = struct.unpack('I', tmp118)[0]
			
			self.polices = []
			for tmp120 in range(tmp119):
				tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp122:
					tmp121 = Police()
					offset = tmp121.deserialize(s, offset)
				else:
					tmp121 = None
				self.polices.append(tmp121)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp123:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
