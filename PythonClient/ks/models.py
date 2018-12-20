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
	ExplodedBombSite = 5
	Wall = 6


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


	def __init__(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, is_dead=None):
		self.initialize(id, position, planting_remaining_time, footstep_sounds, is_dead)
	

	def initialize(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, is_dead=None):
		self.id = id
		self.position = position
		self.planting_remaining_time = planting_remaining_time
		self.footstep_sounds = footstep_sounds
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
		
		# serialize self.is_dead
		s += b'\x00' if self.is_dead is None else b'\x01'
		if self.is_dead is not None:
			s += struct.pack('?', self.is_dead)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp34 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp34:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.planting_remaining_time
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.planting_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planting_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp39 = s[offset:offset + tmp38]
			offset += tmp38
			tmp39 += b'\x00' * (4 - tmp38)
			tmp40 = struct.unpack('I', tmp39)[0]
			
			self.footstep_sounds = []
			for tmp41 in range(tmp40):
				tmp43 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp43:
					tmp42 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp42 = None
				self.footstep_sounds.append(tmp42)
		else:
			self.footstep_sounds = None
		
		# deserialize self.is_dead
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			self.is_dead = struct.unpack('?', s[offset:offset + 1])[0]
			offset += 1
		else:
			self.is_dead = None
		
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
			tmp45 = b''
			tmp45 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp45) and tmp45[-1] == b'\x00'[0]:
				tmp45 = tmp45[:-1]
			s += struct.pack('B', len(tmp45))
			s += tmp45
			
			for tmp46 in self.footstep_sounds:
				s += b'\x00' if tmp46 is None else b'\x01'
				if tmp46 is not None:
					s += struct.pack('i', tmp46)
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp47 = b''
			tmp47 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp47) and tmp47[-1] == b'\x00'[0]:
				tmp47 = tmp47[:-1]
			s += struct.pack('B', len(tmp47))
			s += tmp47
			
			for tmp48 in self.bomb_sounds:
				s += b'\x00' if tmp48 is None else b'\x01'
				if tmp48 is not None:
					s += struct.pack('i', tmp48)
		
		# serialize self.is_visible
		s += b'\x00' if self.is_visible is None else b'\x01'
		if self.is_visible is not None:
			s += struct.pack('?', self.is_visible)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp49 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp49:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp54 = s[offset:offset + tmp53]
			offset += tmp53
			tmp54 += b'\x00' * (4 - tmp53)
			tmp55 = struct.unpack('I', tmp54)[0]
			
			self.footstep_sounds = []
			for tmp56 in range(tmp55):
				tmp58 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp58:
					tmp57 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp57 = None
				self.footstep_sounds.append(tmp57)
		else:
			self.footstep_sounds = None
		
		# deserialize self.bomb_sounds
		tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp59:
			tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp61 = s[offset:offset + tmp60]
			offset += tmp60
			tmp61 += b'\x00' * (4 - tmp60)
			tmp62 = struct.unpack('I', tmp61)[0]
			
			self.bomb_sounds = []
			for tmp63 in range(tmp62):
				tmp65 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp65:
					tmp64 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp64 = None
				self.bomb_sounds.append(tmp64)
		else:
			self.bomb_sounds = None
		
		# deserialize self.is_visible
		tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp66:
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
			tmp67 = b''
			tmp67 += struct.pack('I', len(self.board))
			while len(tmp67) and tmp67[-1] == b'\x00'[0]:
				tmp67 = tmp67[:-1]
			s += struct.pack('B', len(tmp67))
			s += tmp67
			
			for tmp68 in self.board:
				s += b'\x00' if tmp68 is None else b'\x01'
				if tmp68 is not None:
					tmp69 = b''
					tmp69 += struct.pack('I', len(tmp68))
					while len(tmp69) and tmp69[-1] == b'\x00'[0]:
						tmp69 = tmp69[:-1]
					s += struct.pack('B', len(tmp69))
					s += tmp69
					
					for tmp70 in tmp68:
						s += b'\x00' if tmp70 is None else b'\x01'
						if tmp70 is not None:
							s += struct.pack('b', tmp70.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp71 = b''
			tmp71 += struct.pack('I', len(self.scores))
			while len(tmp71) and tmp71[-1] == b'\x00'[0]:
				tmp71 = tmp71[:-1]
			s += struct.pack('B', len(tmp71))
			s += tmp71
			
			for tmp72 in self.scores:
				s += b'\x00' if tmp72 is None else b'\x01'
				if tmp72 is not None:
					tmp73 = b''
					tmp73 += struct.pack('I', len(tmp72))
					while len(tmp73) and tmp73[-1] == b'\x00'[0]:
						tmp73 = tmp73[:-1]
					s += struct.pack('B', len(tmp73))
					s += tmp73
					
					s += tmp72.encode('ISO-8859-1') if PY3 else tmp72
				s += b'\x00' if self.scores[tmp72] is None else b'\x01'
				if self.scores[tmp72] is not None:
					s += struct.pack('f', self.scores[tmp72])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp74 = b''
			tmp74 += struct.pack('I', len(self.bombs))
			while len(tmp74) and tmp74[-1] == b'\x00'[0]:
				tmp74 = tmp74[:-1]
			s += struct.pack('B', len(tmp74))
			s += tmp74
			
			for tmp75 in self.bombs:
				s += b'\x00' if tmp75 is None else b'\x01'
				if tmp75 is not None:
					s += tmp75.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp76 = b''
			tmp76 += struct.pack('I', len(self.terrorists))
			while len(tmp76) and tmp76[-1] == b'\x00'[0]:
				tmp76 = tmp76[:-1]
			s += struct.pack('B', len(tmp76))
			s += tmp76
			
			for tmp77 in self.terrorists:
				s += b'\x00' if tmp77 is None else b'\x01'
				if tmp77 is not None:
					s += tmp77.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp78 = b''
			tmp78 += struct.pack('I', len(self.polices))
			while len(tmp78) and tmp78[-1] == b'\x00'[0]:
				tmp78 = tmp78[:-1]
			s += struct.pack('B', len(tmp78))
			s += tmp78
			
			for tmp79 in self.polices:
				s += b'\x00' if tmp79 is None else b'\x01'
				if tmp79 is not None:
					s += tmp79.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp80 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp80:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp81 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp81:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp84 = s[offset:offset + tmp83]
			offset += tmp83
			tmp84 += b'\x00' * (4 - tmp83)
			tmp85 = struct.unpack('I', tmp84)[0]
			
			self.board = []
			for tmp86 in range(tmp85):
				tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp88:
					tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp90 = s[offset:offset + tmp89]
					offset += tmp89
					tmp90 += b'\x00' * (4 - tmp89)
					tmp91 = struct.unpack('I', tmp90)[0]
					
					tmp87 = []
					for tmp92 in range(tmp91):
						tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp94:
							tmp95 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp93 = ECell(tmp95)
						else:
							tmp93 = None
						tmp87.append(tmp93)
				else:
					tmp87 = None
				self.board.append(tmp87)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp96:
			tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp98 = s[offset:offset + tmp97]
			offset += tmp97
			tmp98 += b'\x00' * (4 - tmp97)
			tmp99 = struct.unpack('I', tmp98)[0]
			
			self.scores = {}
			for tmp100 in range(tmp99):
				tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp103:
					tmp104 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp105 = s[offset:offset + tmp104]
					offset += tmp104
					tmp105 += b'\x00' * (4 - tmp104)
					tmp106 = struct.unpack('I', tmp105)[0]
					
					tmp101 = s[offset:offset + tmp106].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp106]
					offset += tmp106
				else:
					tmp101 = None
				tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp107:
					tmp102 = struct.unpack('f', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp102 = None
				self.scores[tmp101] = tmp102
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp108 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp108:
			tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp110 = s[offset:offset + tmp109]
			offset += tmp109
			tmp110 += b'\x00' * (4 - tmp109)
			tmp111 = struct.unpack('I', tmp110)[0]
			
			self.bombs = []
			for tmp112 in range(tmp111):
				tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp114:
					tmp113 = Bomb()
					offset = tmp113.deserialize(s, offset)
				else:
					tmp113 = None
				self.bombs.append(tmp113)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp115:
			tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp117 = s[offset:offset + tmp116]
			offset += tmp116
			tmp117 += b'\x00' * (4 - tmp116)
			tmp118 = struct.unpack('I', tmp117)[0]
			
			self.terrorists = []
			for tmp119 in range(tmp118):
				tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp121:
					tmp120 = Terrorist()
					offset = tmp120.deserialize(s, offset)
				else:
					tmp120 = None
				self.terrorists.append(tmp120)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp122:
			tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp124 = s[offset:offset + tmp123]
			offset += tmp123
			tmp124 += b'\x00' * (4 - tmp123)
			tmp125 = struct.unpack('I', tmp124)[0]
			
			self.polices = []
			for tmp126 in range(tmp125):
				tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp128:
					tmp127 = Police()
					offset = tmp127.deserialize(s, offset)
				else:
					tmp127 = None
				self.polices.append(tmp127)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp129:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
