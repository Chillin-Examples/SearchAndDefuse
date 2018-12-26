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


	def __init__(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, score_coefficient_small_bomb_site=None, score_coefficient_medium_bomb_site=None, score_coefficient_large_bomb_site=None, score_coefficient_vast_bomb_site=None, terrorist_vision_distance=None, terrorist_death_score=None, police_death_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
		self.initialize(bomb_planting_time, bomb_defusion_time, bomb_explosion_time, bomb_planting_score, bomb_defusion_score, bomb_explosion_score, score_coefficient_small_bomb_site, score_coefficient_medium_bomb_site, score_coefficient_large_bomb_site, score_coefficient_vast_bomb_site, terrorist_vision_distance, terrorist_death_score, police_death_score, police_vision_distance, sound_ranges, max_cycles)
	

	def initialize(self, bomb_planting_time=None, bomb_defusion_time=None, bomb_explosion_time=None, bomb_planting_score=None, bomb_defusion_score=None, bomb_explosion_score=None, score_coefficient_small_bomb_site=None, score_coefficient_medium_bomb_site=None, score_coefficient_large_bomb_site=None, score_coefficient_vast_bomb_site=None, terrorist_vision_distance=None, terrorist_death_score=None, police_death_score=None, police_vision_distance=None, sound_ranges=None, max_cycles=None):
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
		self.police_death_score = police_death_score
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
		
		# serialize self.police_death_score
		s += b'\x00' if self.police_death_score is None else b'\x01'
		if self.police_death_score is not None:
			s += struct.pack('i', self.police_death_score)
		
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
		
		# deserialize self.police_death_score
		tmp14 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp14:
			self.police_death_score = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.police_death_score = None
		
		# deserialize self.police_vision_distance
		tmp15 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp15:
			self.police_vision_distance = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.police_vision_distance = None
		
		# deserialize self.sound_ranges
		tmp16 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp16:
			tmp17 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp18 = s[offset:offset + tmp17]
			offset += tmp17
			tmp18 += b'\x00' * (4 - tmp17)
			tmp19 = struct.unpack('I', tmp18)[0]
			
			self.sound_ranges = {}
			for tmp20 in range(tmp19):
				tmp23 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp23:
					tmp24 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp21 = ESoundIntensity(tmp24)
				else:
					tmp21 = None
				tmp25 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp25:
					tmp22 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp22 = None
				self.sound_ranges[tmp21] = tmp22
		else:
			self.sound_ranges = None
		
		# deserialize self.max_cycles
		tmp26 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp26:
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
		tmp27 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp27:
			self.x = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.x = None
		
		# deserialize self.y
		tmp28 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp28:
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
		tmp29 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp29:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.explosion_remaining_time
		tmp30 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp30:
			self.explosion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.explosion_remaining_time = None
		
		# deserialize self.planter_id
		tmp31 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp31:
			self.planter_id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planter_id = None
		
		# deserialize self.defuser_id
		tmp32 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp32:
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
			tmp33 = b''
			tmp33 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp33) and tmp33[-1] == b'\x00'[0]:
				tmp33 = tmp33[:-1]
			s += struct.pack('B', len(tmp33))
			s += tmp33
			
			for tmp34 in self.footstep_sounds:
				s += b'\x00' if tmp34 is None else b'\x01'
				if tmp34 is not None:
					s += struct.pack('i', tmp34)
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp35 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp35:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp36 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp36:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.planting_remaining_time
		tmp37 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp37:
			self.planting_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.planting_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp38 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp38:
			tmp39 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp40 = s[offset:offset + tmp39]
			offset += tmp39
			tmp40 += b'\x00' * (4 - tmp39)
			tmp41 = struct.unpack('I', tmp40)[0]
			
			self.footstep_sounds = []
			for tmp42 in range(tmp41):
				tmp44 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp44:
					tmp43 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp43 = None
				self.footstep_sounds.append(tmp43)
		else:
			self.footstep_sounds = None
		
		# deserialize self.status
		tmp45 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp45:
			tmp46 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = AgentStatus(tmp46)
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
			tmp47 = b''
			tmp47 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp47) and tmp47[-1] == b'\x00'[0]:
				tmp47 = tmp47[:-1]
			s += struct.pack('B', len(tmp47))
			s += tmp47
			
			for tmp48 in self.footstep_sounds:
				s += b'\x00' if tmp48 is None else b'\x01'
				if tmp48 is not None:
					s += struct.pack('i', tmp48)
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp49 = b''
			tmp49 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp49) and tmp49[-1] == b'\x00'[0]:
				tmp49 = tmp49[:-1]
			s += struct.pack('B', len(tmp49))
			s += tmp49
			
			for tmp50 in self.bomb_sounds:
				s += b'\x00' if tmp50 is None else b'\x01'
				if tmp50 is not None:
					s += struct.pack('i', tmp50)
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp51 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp51:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp56 = s[offset:offset + tmp55]
			offset += tmp55
			tmp56 += b'\x00' * (4 - tmp55)
			tmp57 = struct.unpack('I', tmp56)[0]
			
			self.footstep_sounds = []
			for tmp58 in range(tmp57):
				tmp60 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp60:
					tmp59 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp59 = None
				self.footstep_sounds.append(tmp59)
		else:
			self.footstep_sounds = None
		
		# deserialize self.bomb_sounds
		tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp61:
			tmp62 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp63 = s[offset:offset + tmp62]
			offset += tmp62
			tmp63 += b'\x00' * (4 - tmp62)
			tmp64 = struct.unpack('I', tmp63)[0]
			
			self.bomb_sounds = []
			for tmp65 in range(tmp64):
				tmp67 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp67:
					tmp66 = struct.unpack('i', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp66 = None
				self.bomb_sounds.append(tmp66)
		else:
			self.bomb_sounds = None
		
		# deserialize self.status
		tmp68 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp68:
			tmp69 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = AgentStatus(tmp69)
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
			tmp70 = b''
			tmp70 += struct.pack('I', len(self.board))
			while len(tmp70) and tmp70[-1] == b'\x00'[0]:
				tmp70 = tmp70[:-1]
			s += struct.pack('B', len(tmp70))
			s += tmp70
			
			for tmp71 in self.board:
				s += b'\x00' if tmp71 is None else b'\x01'
				if tmp71 is not None:
					tmp72 = b''
					tmp72 += struct.pack('I', len(tmp71))
					while len(tmp72) and tmp72[-1] == b'\x00'[0]:
						tmp72 = tmp72[:-1]
					s += struct.pack('B', len(tmp72))
					s += tmp72
					
					for tmp73 in tmp71:
						s += b'\x00' if tmp73 is None else b'\x01'
						if tmp73 is not None:
							s += struct.pack('b', tmp73.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp74 = b''
			tmp74 += struct.pack('I', len(self.scores))
			while len(tmp74) and tmp74[-1] == b'\x00'[0]:
				tmp74 = tmp74[:-1]
			s += struct.pack('B', len(tmp74))
			s += tmp74
			
			for tmp75 in self.scores:
				s += b'\x00' if tmp75 is None else b'\x01'
				if tmp75 is not None:
					tmp76 = b''
					tmp76 += struct.pack('I', len(tmp75))
					while len(tmp76) and tmp76[-1] == b'\x00'[0]:
						tmp76 = tmp76[:-1]
					s += struct.pack('B', len(tmp76))
					s += tmp76
					
					s += tmp75.encode('ISO-8859-1') if PY3 else tmp75
				s += b'\x00' if self.scores[tmp75] is None else b'\x01'
				if self.scores[tmp75] is not None:
					s += struct.pack('f', self.scores[tmp75])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp77 = b''
			tmp77 += struct.pack('I', len(self.bombs))
			while len(tmp77) and tmp77[-1] == b'\x00'[0]:
				tmp77 = tmp77[:-1]
			s += struct.pack('B', len(tmp77))
			s += tmp77
			
			for tmp78 in self.bombs:
				s += b'\x00' if tmp78 is None else b'\x01'
				if tmp78 is not None:
					s += tmp78.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp79 = b''
			tmp79 += struct.pack('I', len(self.terrorists))
			while len(tmp79) and tmp79[-1] == b'\x00'[0]:
				tmp79 = tmp79[:-1]
			s += struct.pack('B', len(tmp79))
			s += tmp79
			
			for tmp80 in self.terrorists:
				s += b'\x00' if tmp80 is None else b'\x01'
				if tmp80 is not None:
					s += tmp80.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp81 = b''
			tmp81 += struct.pack('I', len(self.polices))
			while len(tmp81) and tmp81[-1] == b'\x00'[0]:
				tmp81 = tmp81[:-1]
			s += struct.pack('B', len(tmp81))
			s += tmp81
			
			for tmp82 in self.polices:
				s += b'\x00' if tmp82 is None else b'\x01'
				if tmp82 is not None:
					s += tmp82.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp83 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp83:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp84 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp84:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp85 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp85:
			tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp87 = s[offset:offset + tmp86]
			offset += tmp86
			tmp87 += b'\x00' * (4 - tmp86)
			tmp88 = struct.unpack('I', tmp87)[0]
			
			self.board = []
			for tmp89 in range(tmp88):
				tmp91 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp91:
					tmp92 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp93 = s[offset:offset + tmp92]
					offset += tmp92
					tmp93 += b'\x00' * (4 - tmp92)
					tmp94 = struct.unpack('I', tmp93)[0]
					
					tmp90 = []
					for tmp95 in range(tmp94):
						tmp97 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp97:
							tmp98 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp96 = ECell(tmp98)
						else:
							tmp96 = None
						tmp90.append(tmp96)
				else:
					tmp90 = None
				self.board.append(tmp90)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp99 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp99:
			tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp101 = s[offset:offset + tmp100]
			offset += tmp100
			tmp101 += b'\x00' * (4 - tmp100)
			tmp102 = struct.unpack('I', tmp101)[0]
			
			self.scores = {}
			for tmp103 in range(tmp102):
				tmp106 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp106:
					tmp107 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp108 = s[offset:offset + tmp107]
					offset += tmp107
					tmp108 += b'\x00' * (4 - tmp107)
					tmp109 = struct.unpack('I', tmp108)[0]
					
					tmp104 = s[offset:offset + tmp109].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp109]
					offset += tmp109
				else:
					tmp104 = None
				tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp110:
					tmp105 = struct.unpack('f', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp105 = None
				self.scores[tmp104] = tmp105
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp111 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp111:
			tmp112 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp113 = s[offset:offset + tmp112]
			offset += tmp112
			tmp113 += b'\x00' * (4 - tmp112)
			tmp114 = struct.unpack('I', tmp113)[0]
			
			self.bombs = []
			for tmp115 in range(tmp114):
				tmp117 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp117:
					tmp116 = Bomb()
					offset = tmp116.deserialize(s, offset)
				else:
					tmp116 = None
				self.bombs.append(tmp116)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp118 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp118:
			tmp119 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp120 = s[offset:offset + tmp119]
			offset += tmp119
			tmp120 += b'\x00' * (4 - tmp119)
			tmp121 = struct.unpack('I', tmp120)[0]
			
			self.terrorists = []
			for tmp122 in range(tmp121):
				tmp124 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp124:
					tmp123 = Terrorist()
					offset = tmp123.deserialize(s, offset)
				else:
					tmp123 = None
				self.terrorists.append(tmp123)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp125 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp125:
			tmp126 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp127 = s[offset:offset + tmp126]
			offset += tmp126
			tmp127 += b'\x00' * (4 - tmp126)
			tmp128 = struct.unpack('I', tmp127)[0]
			
			self.polices = []
			for tmp129 in range(tmp128):
				tmp131 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp131:
					tmp130 = Police()
					offset = tmp130.deserialize(s, offset)
				else:
					tmp130 = None
				self.polices.append(tmp130)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp132 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp132:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
