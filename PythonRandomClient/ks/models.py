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


	def __init__(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, score_coefficient_small_bomb_site=None, score_coefficient_medium_bomb_site=None, score_coefficient_large_bomb_site=None, score_coefficient_vast_bomb_site=None, terrorist_vision_distance=None, terrorist_death_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
		self.initialize(bomb_planting_time, bomb_defusion_time, bomb_explosion_time, bomb_planting_score, bomb_defusion_score, bomb_explosion_score, score_coefficient_small_bomb_site, score_coefficient_medium_bomb_site, score_coefficient_large_bomb_site, score_coefficient_vast_bomb_site, terrorist_vision_distance, terrorist_death_score, police_vision_distance, sound_ranges, max_cycles)
	

	def initialize(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, score_coefficient_small_bomb_site=None, score_coefficient_medium_bomb_site=None, score_coefficient_large_bomb_site=None, score_coefficient_vast_bomb_site=None, terrorist_vision_distance=None, terrorist_death_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
		self.bomb_planting_time = bomb_planting_time
		self.bomb_defusion_time = bomb_defusion_time
		self.bomb_explosion_time = bomb_explosion_time
		self.bomb_planting_score = bomb_planting_score
		self.bomb_defusion_score = bomb_defusion_score
		self.bomb_explosion_score = bomb_explosion_score
		self.score_coefficient_small_bomb_site = score_coefficient_small_bomb_site
		self.score_coefficient_medium_bomb_site = score_coefficient_medium_bomb_site
		self.score_coefficient_large_bomb_site = score_coefficient_large_bomb_site
		self.score_coefficient_vast_bomb_site = score_coefficient_vast_bomb_site
		self.terrorist_vision_distance = terrorist_vision_distance
		self.terrorist_death_score = terrorist_death_score
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
		
		# serialize self.score_coefficient_small_bomb_site
		s += b'\x00' if self.score_coefficient_small_bomb_site is None else b'\x01'
		if self.score_coefficient_small_bomb_site is not None:
			s += struct.pack('f', self.score_coefficient_small_bomb_site)
		
		# serialize self.score_coefficient_medium_bomb_site
		s += b'\x00' if self.score_coefficient_medium_bomb_site is None else b'\x01'
		if self.score_coefficient_medium_bomb_site is not None:
			s += struct.pack('f', self.score_coefficient_medium_bomb_site)
		
		# serialize self.score_coefficient_large_bomb_site
		s += b'\x00' if self.score_coefficient_large_bomb_site is None else b'\x01'
		if self.score_coefficient_large_bomb_site is not None:
			s += struct.pack('f', self.score_coefficient_large_bomb_site)
		
		# serialize self.score_coefficient_vast_bomb_site
		s += b'\x00' if self.score_coefficient_vast_bomb_site is None else b'\x01'
		if self.score_coefficient_vast_bomb_site is not None:
			s += struct.pack('f', self.score_coefficient_vast_bomb_site)
		
		# serialize self.terrorist_vision_distance
		s += b'\x00' if self.terrorist_vision_distance is None else b'\x01'
		if self.terrorist_vision_distance is not None:
			s += struct.pack('i', self.terrorist_vision_distance)
		
		# serialize self.terrorist_death_score
		s += b'\x00' if self.terrorist_death_score is None else b'\x01'
		if self.terrorist_death_score is not None:
			s += struct.pack('i', self.terrorist_death_score)
		
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
		
		# deserialize self.score_coefficient_small_bomb_site
		tmp8 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp8:
			self.score_coefficient_small_bomb_site = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.score_coefficient_small_bomb_site = None
		
		# deserialize self.score_coefficient_medium_bomb_site
		tmp9 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp9:
			self.score_coefficient_medium_bomb_site = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.score_coefficient_medium_bomb_site = None
		
		# deserialize self.score_coefficient_large_bomb_site
		tmp10 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp10:
			self.score_coefficient_large_bomb_site = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.score_coefficient_large_bomb_site = None
		
		# deserialize self.score_coefficient_vast_bomb_site
		tmp11 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp11:
			self.score_coefficient_vast_bomb_site = struct.unpack('f', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.score_coefficient_vast_bomb_site = None
		
		# deserialize self.terrorist_vision_distance
		tmp12 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp12:
			self.terrorist_vision_distance = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.terrorist_vision_distance = None
		
		# deserialize self.terrorist_death_score
		tmp13 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp13:
			self.terrorist_death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.terrorist_death_score = None
		
		# deserialize self.police_vision_distance
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.police_vision_distance = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.police_vision_distance = None
		
		# deserialize self.sound_ranges
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp17 = s[offset:offset + tmp16]
			offset += tmp16
			tmp17 += b'\x00' * (4 - tmp16)
			tmp18 = struct.unpack('I', tmp17)[0]
			
			self.sound_ranges = {}
			for tmp19 in range(tmp18):
				tmp22 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp22:
					tmp23 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp20 = ESoundIntensity(tmp23)
				else:
					tmp20 = None
				tmp24 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp24:
					tmp21 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp21 = None
				self.sound_ranges[tmp20] = tmp21
		else:
			self.sound_ranges = None
		
		# deserialize self.max_cycles
		tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp25:
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
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.y = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.y = None
		
		return offset


class Bomb(object):

	@staticmethod
	def name():
		return 'Bomb'


	def __init__(self, position=None, explosion_remaining_time=None, planter_id=None, defuser_id=None):
		self.initialize(position, explosion_remaining_time, planter_id, defuser_id)
	

	def initialize(self, position=None, explosion_remaining_time=None, planter_id=None, defuser_id=None):
		self.position = position
		self.explosion_remaining_time = explosion_remaining_time
		self.planter_id = planter_id
		self.defuser_id = defuser_id
	

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
		
		# serialize self.planter_id
		s += b'\x00' if self.planter_id is None else b'\x01'
		if self.planter_id is not None:
			s += struct.pack('i', self.planter_id)
		
		# serialize self.defuser_id
		s += b'\x00' if self.defuser_id is None else b'\x01'
		if self.defuser_id is not None:
			s += struct.pack('i', self.defuser_id)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.position
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.explosion_remaining_time
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.explosion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.explosion_remaining_time = None
		
		# deserialize self.planter_id
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.planter_id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planter_id = None
		
		# deserialize self.defuser_id
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.defuser_id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defuser_id = None
		
		return offset


class Terrorist(object):

	@staticmethod
	def name():
		return 'Terrorist'


	def __init__(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, vision=None, is_dead=None):
		self.initialize(id, position, planting_remaining_time, footstep_sounds, vision, is_dead)
	

	def initialize(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, vision=None, is_dead=None):
		self.id = id
		self.position = position
		self.planting_remaining_time = planting_remaining_time
		self.footstep_sounds = footstep_sounds
		self.vision = vision
		self.is_dead = is_dead
	

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
			tmp32 = b''
			tmp32 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp32) and tmp32[-1] == b'\x00'[0]:
				tmp32 = tmp32[:-1]
			s += struct.pack('B', len(tmp32))
			s += tmp32
			
			for tmp33 in self.footstep_sounds:
				s += b'\x00' if tmp33 is None else b'\x01'
				if tmp33 is not None:
					s += struct.pack('i', tmp33)
		
		# serialize self.vision
		s += b'\x00' if self.vision is None else b'\x01'
		if self.vision is not None:
			tmp34 = b''
			tmp34 += struct.pack('I', len(self.vision))
			while len(tmp34) and tmp34[-1] == b'\x00'[0]:
				tmp34 = tmp34[:-1]
			s += struct.pack('B', len(tmp34))
			s += tmp34
			
			for tmp35 in self.vision:
				s += b'\x00' if tmp35 is None else b'\x01'
				if tmp35 is not None:
					s += tmp35.serialize()
		
		# serialize self.is_dead
		s += b'\x00' if self.is_dead is None else b'\x01'
		if self.is_dead is not None:
			s += struct.pack('?', self.is_dead)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.planting_remaining_time
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			self.planting_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planting_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp39:
			tmp40 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp41 = s[offset:offset + tmp40]
			offset += tmp40
			tmp41 += b'\x00' * (4 - tmp40)
			tmp42 = struct.unpack('I', tmp41)[0]
			
			self.footstep_sounds = []
			for tmp43 in range(tmp42):
				tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp45:
					tmp44 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp44 = None
				self.footstep_sounds.append(tmp44)
		else:
			self.footstep_sounds = None
		
		# deserialize self.vision
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			tmp47 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp48 = s[offset:offset + tmp47]
			offset += tmp47
			tmp48 += b'\x00' * (4 - tmp47)
			tmp49 = struct.unpack('I', tmp48)[0]
			
			self.vision = []
			for tmp50 in range(tmp49):
				tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp52:
					tmp51 = Position()
					offset = tmp51.deserialize(s, offset)
				else:
					tmp51 = None
				self.vision.append(tmp51)
		else:
			self.vision = None
		
		# deserialize self.is_dead
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			self.is_dead = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_dead = None
		
		return offset


class Police(object):

	@staticmethod
	def name():
		return 'Police'


	def __init__(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, vision=None, bomb_sounds=None, is_visible=None):
		self.initialize(id, position, defusion_remaining_time, footstep_sounds, vision, bomb_sounds, is_visible)
	

	def initialize(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, vision=None, bomb_sounds=None, is_visible=None):
		self.id = id
		self.position = position
		self.defusion_remaining_time = defusion_remaining_time
		self.footstep_sounds = footstep_sounds
		self.vision = vision
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
			tmp54 = b''
			tmp54 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp54) and tmp54[-1] == b'\x00'[0]:
				tmp54 = tmp54[:-1]
			s += struct.pack('B', len(tmp54))
			s += tmp54
			
			for tmp55 in self.footstep_sounds:
				s += b'\x00' if tmp55 is None else b'\x01'
				if tmp55 is not None:
					s += struct.pack('i', tmp55)
		
		# serialize self.vision
		s += b'\x00' if self.vision is None else b'\x01'
		if self.vision is not None:
			tmp56 = b''
			tmp56 += struct.pack('I', len(self.vision))
			while len(tmp56) and tmp56[-1] == b'\x00'[0]:
				tmp56 = tmp56[:-1]
			s += struct.pack('B', len(tmp56))
			s += tmp56
			
			for tmp57 in self.vision:
				s += b'\x00' if tmp57 is None else b'\x01'
				if tmp57 is not None:
					s += tmp57.serialize()
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp58 = b''
			tmp58 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp58) and tmp58[-1] == b'\x00'[0]:
				tmp58 = tmp58[:-1]
			s += struct.pack('B', len(tmp58))
			s += tmp58
			
			for tmp59 in self.bomb_sounds:
				s += b'\x00' if tmp59 is None else b'\x01'
				if tmp59 is not None:
					s += struct.pack('i', tmp59)
		
		# serialize self.is_visible
		s += b'\x00' if self.is_visible is None else b'\x01'
		if self.is_visible is not None:
			s += struct.pack('?', self.is_visible)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp62:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp65 = s[offset:offset + tmp64]
			offset += tmp64
			tmp65 += b'\x00' * (4 - tmp64)
			tmp66 = struct.unpack('I', tmp65)[0]
			
			self.footstep_sounds = []
			for tmp67 in range(tmp66):
				tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp69:
					tmp68 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp68 = None
				self.footstep_sounds.append(tmp68)
		else:
			self.footstep_sounds = None
		
		# deserialize self.vision
		tmp70 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp70:
			tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp72 = s[offset:offset + tmp71]
			offset += tmp71
			tmp72 += b'\x00' * (4 - tmp71)
			tmp73 = struct.unpack('I', tmp72)[0]
			
			self.vision = []
			for tmp74 in range(tmp73):
				tmp76 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp76:
					tmp75 = Position()
					offset = tmp75.deserialize(s, offset)
				else:
					tmp75 = None
				self.vision.append(tmp75)
		else:
			self.vision = None
		
		# deserialize self.bomb_sounds
		tmp77 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp77:
			tmp78 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp79 = s[offset:offset + tmp78]
			offset += tmp78
			tmp79 += b'\x00' * (4 - tmp78)
			tmp80 = struct.unpack('I', tmp79)[0]
			
			self.bomb_sounds = []
			for tmp81 in range(tmp80):
				tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp83:
					tmp82 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp82 = None
				self.bomb_sounds.append(tmp82)
		else:
			self.bomb_sounds = None
		
		# deserialize self.is_visible
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
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
			tmp85 = b''
			tmp85 += struct.pack('I', len(self.board))
			while len(tmp85) and tmp85[-1] == b'\x00'[0]:
				tmp85 = tmp85[:-1]
			s += struct.pack('B', len(tmp85))
			s += tmp85
			
			for tmp86 in self.board:
				s += b'\x00' if tmp86 is None else b'\x01'
				if tmp86 is not None:
					tmp87 = b''
					tmp87 += struct.pack('I', len(tmp86))
					while len(tmp87) and tmp87[-1] == b'\x00'[0]:
						tmp87 = tmp87[:-1]
					s += struct.pack('B', len(tmp87))
					s += tmp87
					
					for tmp88 in tmp86:
						s += b'\x00' if tmp88 is None else b'\x01'
						if tmp88 is not None:
							s += struct.pack('b', tmp88.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp89 = b''
			tmp89 += struct.pack('I', len(self.scores))
			while len(tmp89) and tmp89[-1] == b'\x00'[0]:
				tmp89 = tmp89[:-1]
			s += struct.pack('B', len(tmp89))
			s += tmp89
			
			for tmp90 in self.scores:
				s += b'\x00' if tmp90 is None else b'\x01'
				if tmp90 is not None:
					tmp91 = b''
					tmp91 += struct.pack('I', len(tmp90))
					while len(tmp91) and tmp91[-1] == b'\x00'[0]:
						tmp91 = tmp91[:-1]
					s += struct.pack('B', len(tmp91))
					s += tmp91
					
					s += tmp90.encode('ISO-8859-1') if PY3 else tmp90
				s += b'\x00' if self.scores[tmp90] is None else b'\x01'
				if self.scores[tmp90] is not None:
					s += struct.pack('f', self.scores[tmp90])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp92 = b''
			tmp92 += struct.pack('I', len(self.bombs))
			while len(tmp92) and tmp92[-1] == b'\x00'[0]:
				tmp92 = tmp92[:-1]
			s += struct.pack('B', len(tmp92))
			s += tmp92
			
			for tmp93 in self.bombs:
				s += b'\x00' if tmp93 is None else b'\x01'
				if tmp93 is not None:
					s += tmp93.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp94 = b''
			tmp94 += struct.pack('I', len(self.terrorists))
			while len(tmp94) and tmp94[-1] == b'\x00'[0]:
				tmp94 = tmp94[:-1]
			s += struct.pack('B', len(tmp94))
			s += tmp94
			
			for tmp95 in self.terrorists:
				s += b'\x00' if tmp95 is None else b'\x01'
				if tmp95 is not None:
					s += tmp95.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp96 = b''
			tmp96 += struct.pack('I', len(self.polices))
			while len(tmp96) and tmp96[-1] == b'\x00'[0]:
				tmp96 = tmp96[:-1]
			s += struct.pack('B', len(tmp96))
			s += tmp96
			
			for tmp97 in self.polices:
				s += b'\x00' if tmp97 is None else b'\x01'
				if tmp97 is not None:
					s += tmp97.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp98:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp99 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp99:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp100:
			tmp101 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp102 = s[offset:offset + tmp101]
			offset += tmp101
			tmp102 += b'\x00' * (4 - tmp101)
			tmp103 = struct.unpack('I', tmp102)[0]
			
			self.board = []
			for tmp104 in range(tmp103):
				tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp106:
					tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp108 = s[offset:offset + tmp107]
					offset += tmp107
					tmp108 += b'\x00' * (4 - tmp107)
					tmp109 = struct.unpack('I', tmp108)[0]
					
					tmp105 = []
					for tmp110 in range(tmp109):
						tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp112:
							tmp113 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp111 = ECell(tmp113)
						else:
							tmp111 = None
						tmp105.append(tmp111)
				else:
					tmp105 = None
				self.board.append(tmp105)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp116 = s[offset:offset + tmp115]
			offset += tmp115
			tmp116 += b'\x00' * (4 - tmp115)
			tmp117 = struct.unpack('I', tmp116)[0]
			
			self.scores = {}
			for tmp118 in range(tmp117):
				tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp121:
					tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp123 = s[offset:offset + tmp122]
					offset += tmp122
					tmp123 += b'\x00' * (4 - tmp122)
					tmp124 = struct.unpack('I', tmp123)[0]
					
					tmp119 = s[offset:offset + tmp124].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp124]
					offset += tmp124
				else:
					tmp119 = None
				tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp125:
					tmp120 = struct.unpack('f', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp120 = None
				self.scores[tmp119] = tmp120
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp126:
			tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp128 = s[offset:offset + tmp127]
			offset += tmp127
			tmp128 += b'\x00' * (4 - tmp127)
			tmp129 = struct.unpack('I', tmp128)[0]
			
			self.bombs = []
			for tmp130 in range(tmp129):
				tmp132 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp132:
					tmp131 = Bomb()
					offset = tmp131.deserialize(s, offset)
				else:
					tmp131 = None
				self.bombs.append(tmp131)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp133 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp133:
			tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp135 = s[offset:offset + tmp134]
			offset += tmp134
			tmp135 += b'\x00' * (4 - tmp134)
			tmp136 = struct.unpack('I', tmp135)[0]
			
			self.terrorists = []
			for tmp137 in range(tmp136):
				tmp139 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp139:
					tmp138 = Terrorist()
					offset = tmp138.deserialize(s, offset)
				else:
					tmp138 = None
				self.terrorists.append(tmp138)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp140 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp140:
			tmp141 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp142 = s[offset:offset + tmp141]
			offset += tmp141
			tmp142 += b'\x00' * (4 - tmp141)
			tmp143 = struct.unpack('I', tmp142)[0]
			
			self.polices = []
			for tmp144 in range(tmp143):
				tmp146 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp146:
					tmp145 = Police()
					offset = tmp145.deserialize(s, offset)
				else:
					tmp145 = None
				self.polices.append(tmp145)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp147 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp147:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
