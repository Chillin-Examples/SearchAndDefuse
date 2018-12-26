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


class AgentStatus(Enum):
	Alive = 0
	Dead = 1


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


	def __init__(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, status=None):
		self.initialize(id, position, planting_remaining_time, footstep_sounds, status)
	

	def initialize(self, id=None, position=None, planting_remaining_time=None, footstep_sounds=None, status=None):
		self.id = id
		self.position = position
		self.planting_remaining_time = planting_remaining_time
		self.footstep_sounds = footstep_sounds
		self.status = status
	

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
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
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
		
		# deserialize self.status
		tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp44:
			tmp45 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = AgentStatus(tmp45)
		else:
			self.status = None
		
		return offset


class Police(object):

	@staticmethod
	def name():
		return 'Police'


	def __init__(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, bomb_sounds=None, status=None):
		self.initialize(id, position, defusion_remaining_time, footstep_sounds, bomb_sounds, status)
	

	def initialize(self, id=None, position=None, defusion_remaining_time=None, footstep_sounds=None, bomb_sounds=None, status=None):
		self.id = id
		self.position = position
		self.defusion_remaining_time = defusion_remaining_time
		self.footstep_sounds = footstep_sounds
		self.bomb_sounds = bomb_sounds
		self.status = status
	

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
			tmp46 = b''
			tmp46 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp46) and tmp46[-1] == b'\x00'[0]:
				tmp46 = tmp46[:-1]
			s += struct.pack('B', len(tmp46))
			s += tmp46
			
			for tmp47 in self.footstep_sounds:
				s += b'\x00' if tmp47 is None else b'\x01'
				if tmp47 is not None:
					s += struct.pack('i', tmp47)
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp48 = b''
			tmp48 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp48) and tmp48[-1] == b'\x00'[0]:
				tmp48 = tmp48[:-1]
			s += struct.pack('B', len(tmp48))
			s += tmp48
			
			for tmp49 in self.bomb_sounds:
				s += b'\x00' if tmp49 is None else b'\x01'
				if tmp49 is not None:
					s += struct.pack('i', tmp49)
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp50 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp50:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp55 = s[offset:offset + tmp54]
			offset += tmp54
			tmp55 += b'\x00' * (4 - tmp54)
			tmp56 = struct.unpack('I', tmp55)[0]
			
			self.footstep_sounds = []
			for tmp57 in range(tmp56):
				tmp59 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp59:
					tmp58 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp58 = None
				self.footstep_sounds.append(tmp58)
		else:
			self.footstep_sounds = None
		
		# deserialize self.bomb_sounds
		tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp60:
			tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp62 = s[offset:offset + tmp61]
			offset += tmp61
			tmp62 += b'\x00' * (4 - tmp61)
			tmp63 = struct.unpack('I', tmp62)[0]
			
			self.bomb_sounds = []
			for tmp64 in range(tmp63):
				tmp66 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp66:
					tmp65 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp65 = None
				self.bomb_sounds.append(tmp65)
		else:
			self.bomb_sounds = None
		
		# deserialize self.status
		tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp67:
			tmp68 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = AgentStatus(tmp68)
		else:
			self.status = None
		
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
			tmp69 = b''
			tmp69 += struct.pack('I', len(self.board))
			while len(tmp69) and tmp69[-1] == b'\x00'[0]:
				tmp69 = tmp69[:-1]
			s += struct.pack('B', len(tmp69))
			s += tmp69
			
			for tmp70 in self.board:
				s += b'\x00' if tmp70 is None else b'\x01'
				if tmp70 is not None:
					tmp71 = b''
					tmp71 += struct.pack('I', len(tmp70))
					while len(tmp71) and tmp71[-1] == b'\x00'[0]:
						tmp71 = tmp71[:-1]
					s += struct.pack('B', len(tmp71))
					s += tmp71
					
					for tmp72 in tmp70:
						s += b'\x00' if tmp72 is None else b'\x01'
						if tmp72 is not None:
							s += struct.pack('b', tmp72.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp73 = b''
			tmp73 += struct.pack('I', len(self.scores))
			while len(tmp73) and tmp73[-1] == b'\x00'[0]:
				tmp73 = tmp73[:-1]
			s += struct.pack('B', len(tmp73))
			s += tmp73
			
			for tmp74 in self.scores:
				s += b'\x00' if tmp74 is None else b'\x01'
				if tmp74 is not None:
					tmp75 = b''
					tmp75 += struct.pack('I', len(tmp74))
					while len(tmp75) and tmp75[-1] == b'\x00'[0]:
						tmp75 = tmp75[:-1]
					s += struct.pack('B', len(tmp75))
					s += tmp75
					
					s += tmp74.encode('ISO-8859-1') if PY3 else tmp74
				s += b'\x00' if self.scores[tmp74] is None else b'\x01'
				if self.scores[tmp74] is not None:
					s += struct.pack('f', self.scores[tmp74])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp76 = b''
			tmp76 += struct.pack('I', len(self.bombs))
			while len(tmp76) and tmp76[-1] == b'\x00'[0]:
				tmp76 = tmp76[:-1]
			s += struct.pack('B', len(tmp76))
			s += tmp76
			
			for tmp77 in self.bombs:
				s += b'\x00' if tmp77 is None else b'\x01'
				if tmp77 is not None:
					s += tmp77.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp78 = b''
			tmp78 += struct.pack('I', len(self.terrorists))
			while len(tmp78) and tmp78[-1] == b'\x00'[0]:
				tmp78 = tmp78[:-1]
			s += struct.pack('B', len(tmp78))
			s += tmp78
			
			for tmp79 in self.terrorists:
				s += b'\x00' if tmp79 is None else b'\x01'
				if tmp79 is not None:
					s += tmp79.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp80 = b''
			tmp80 += struct.pack('I', len(self.polices))
			while len(tmp80) and tmp80[-1] == b'\x00'[0]:
				tmp80 = tmp80[:-1]
			s += struct.pack('B', len(tmp80))
			s += tmp80
			
			for tmp81 in self.polices:
				s += b'\x00' if tmp81 is None else b'\x01'
				if tmp81 is not None:
					s += tmp81.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp82 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp82:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp83:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
			tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp86 = s[offset:offset + tmp85]
			offset += tmp85
			tmp86 += b'\x00' * (4 - tmp85)
			tmp87 = struct.unpack('I', tmp86)[0]
			
			self.board = []
			for tmp88 in range(tmp87):
				tmp90 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp90:
					tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp92 = s[offset:offset + tmp91]
					offset += tmp91
					tmp92 += b'\x00' * (4 - tmp91)
					tmp93 = struct.unpack('I', tmp92)[0]
					
					tmp89 = []
					for tmp94 in range(tmp93):
						tmp96 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp96:
							tmp97 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp95 = ECell(tmp97)
						else:
							tmp95 = None
						tmp89.append(tmp95)
				else:
					tmp89 = None
				self.board.append(tmp89)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp98 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp98:
			tmp99 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp100 = s[offset:offset + tmp99]
			offset += tmp99
			tmp100 += b'\x00' * (4 - tmp99)
			tmp101 = struct.unpack('I', tmp100)[0]
			
			self.scores = {}
			for tmp102 in range(tmp101):
				tmp105 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp105:
					tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp107 = s[offset:offset + tmp106]
					offset += tmp106
					tmp107 += b'\x00' * (4 - tmp106)
					tmp108 = struct.unpack('I', tmp107)[0]
					
					tmp103 = s[offset:offset + tmp108].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp108]
					offset += tmp108
				else:
					tmp103 = None
				tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp109:
					tmp104 = struct.unpack('f', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp104 = None
				self.scores[tmp103] = tmp104
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp110:
			tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp112 = s[offset:offset + tmp111]
			offset += tmp111
			tmp112 += b'\x00' * (4 - tmp111)
			tmp113 = struct.unpack('I', tmp112)[0]
			
			self.bombs = []
			for tmp114 in range(tmp113):
				tmp116 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp116:
					tmp115 = Bomb()
					offset = tmp115.deserialize(s, offset)
				else:
					tmp115 = None
				self.bombs.append(tmp115)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp117:
			tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp119 = s[offset:offset + tmp118]
			offset += tmp118
			tmp119 += b'\x00' * (4 - tmp118)
			tmp120 = struct.unpack('I', tmp119)[0]
			
			self.terrorists = []
			for tmp121 in range(tmp120):
				tmp123 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp123:
					tmp122 = Terrorist()
					offset = tmp122.deserialize(s, offset)
				else:
					tmp122 = None
				self.terrorists.append(tmp122)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp124:
			tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp126 = s[offset:offset + tmp125]
			offset += tmp125
			tmp126 += b'\x00' * (4 - tmp125)
			tmp127 = struct.unpack('I', tmp126)[0]
			
			self.polices = []
			for tmp128 in range(tmp127):
				tmp130 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp130:
					tmp129 = Police()
					offset = tmp129.deserialize(s, offset)
				else:
					tmp129 = None
				self.polices.append(tmp129)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp131 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp131:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
