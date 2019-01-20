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


class ESoundIntensity(Enum):
	Weak = 0
	Normal = 1
	Strong = 2


class EAgentStatus(Enum):
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
					s += struct.pack('b', tmp34.value)
		
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
					tmp45 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp43 = ESoundIntensity(tmp45)
				else:
					tmp43 = None
				self.footstep_sounds.append(tmp43)
		else:
			self.footstep_sounds = None
		
		# deserialize self.status
		tmp46 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp46:
			tmp47 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = EAgentStatus(tmp47)
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
			tmp48 = b''
			tmp48 += struct.pack('I', len(self.footstep_sounds))
			while len(tmp48) and tmp48[-1] == b'\x00'[0]:
				tmp48 = tmp48[:-1]
			s += struct.pack('B', len(tmp48))
			s += tmp48
			
			for tmp49 in self.footstep_sounds:
				s += b'\x00' if tmp49 is None else b'\x01'
				if tmp49 is not None:
					s += struct.pack('b', tmp49.value)
		
		# serialize self.bomb_sounds
		s += b'\x00' if self.bomb_sounds is None else b'\x01'
		if self.bomb_sounds is not None:
			tmp50 = b''
			tmp50 += struct.pack('I', len(self.bomb_sounds))
			while len(tmp50) and tmp50[-1] == b'\x00'[0]:
				tmp50 = tmp50[:-1]
			s += struct.pack('B', len(tmp50))
			s += tmp50
			
			for tmp51 in self.bomb_sounds:
				s += b'\x00' if tmp51 is None else b'\x01'
				if tmp51 is not None:
					s += struct.pack('b', tmp51.value)
		
		# serialize self.status
		s += b'\x00' if self.status is None else b'\x01'
		if self.status is not None:
			s += struct.pack('b', self.status.value)
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.id
		tmp52 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp52:
			self.id = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.id = None
		
		# deserialize self.position
		tmp53 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp53:
			self.position = Position()
			offset = self.position.deserialize(s, offset)
		else:
			self.position = None
		
		# deserialize self.defusion_remaining_time
		tmp54 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp54:
			self.defusion_remaining_time = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.defusion_remaining_time = None
		
		# deserialize self.footstep_sounds
		tmp55 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp55:
			tmp56 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp57 = s[offset:offset + tmp56]
			offset += tmp56
			tmp57 += b'\x00' * (4 - tmp56)
			tmp58 = struct.unpack('I', tmp57)[0]
			
			self.footstep_sounds = []
			for tmp59 in range(tmp58):
				tmp61 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp61:
					tmp62 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp60 = ESoundIntensity(tmp62)
				else:
					tmp60 = None
				self.footstep_sounds.append(tmp60)
		else:
			self.footstep_sounds = None
		
		# deserialize self.bomb_sounds
		tmp63 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp63:
			tmp64 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp65 = s[offset:offset + tmp64]
			offset += tmp64
			tmp65 += b'\x00' * (4 - tmp64)
			tmp66 = struct.unpack('I', tmp65)[0]
			
			self.bomb_sounds = []
			for tmp67 in range(tmp66):
				tmp69 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp69:
					tmp70 = struct.unpack('b', s[offset:offset + 1])[0]
					offset += 1
					tmp68 = ESoundIntensity(tmp70)
				else:
					tmp68 = None
				self.bomb_sounds.append(tmp68)
		else:
			self.bomb_sounds = None
		
		# deserialize self.status
		tmp71 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp71:
			tmp72 = struct.unpack('b', s[offset:offset + 1])[0]
			offset += 1
			self.status = EAgentStatus(tmp72)
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
			tmp73 = b''
			tmp73 += struct.pack('I', len(self.board))
			while len(tmp73) and tmp73[-1] == b'\x00'[0]:
				tmp73 = tmp73[:-1]
			s += struct.pack('B', len(tmp73))
			s += tmp73
			
			for tmp74 in self.board:
				s += b'\x00' if tmp74 is None else b'\x01'
				if tmp74 is not None:
					tmp75 = b''
					tmp75 += struct.pack('I', len(tmp74))
					while len(tmp75) and tmp75[-1] == b'\x00'[0]:
						tmp75 = tmp75[:-1]
					s += struct.pack('B', len(tmp75))
					s += tmp75
					
					for tmp76 in tmp74:
						s += b'\x00' if tmp76 is None else b'\x01'
						if tmp76 is not None:
							s += struct.pack('b', tmp76.value)
		
		# serialize self.scores
		s += b'\x00' if self.scores is None else b'\x01'
		if self.scores is not None:
			tmp77 = b''
			tmp77 += struct.pack('I', len(self.scores))
			while len(tmp77) and tmp77[-1] == b'\x00'[0]:
				tmp77 = tmp77[:-1]
			s += struct.pack('B', len(tmp77))
			s += tmp77
			
			for tmp78 in self.scores:
				s += b'\x00' if tmp78 is None else b'\x01'
				if tmp78 is not None:
					tmp79 = b''
					tmp79 += struct.pack('I', len(tmp78))
					while len(tmp79) and tmp79[-1] == b'\x00'[0]:
						tmp79 = tmp79[:-1]
					s += struct.pack('B', len(tmp79))
					s += tmp79
					
					s += tmp78.encode('ISO-8859-1') if PY3 else tmp78
				s += b'\x00' if self.scores[tmp78] is None else b'\x01'
				if self.scores[tmp78] is not None:
					s += struct.pack('f', self.scores[tmp78])
		
		# serialize self.bombs
		s += b'\x00' if self.bombs is None else b'\x01'
		if self.bombs is not None:
			tmp80 = b''
			tmp80 += struct.pack('I', len(self.bombs))
			while len(tmp80) and tmp80[-1] == b'\x00'[0]:
				tmp80 = tmp80[:-1]
			s += struct.pack('B', len(tmp80))
			s += tmp80
			
			for tmp81 in self.bombs:
				s += b'\x00' if tmp81 is None else b'\x01'
				if tmp81 is not None:
					s += tmp81.serialize()
		
		# serialize self.terrorists
		s += b'\x00' if self.terrorists is None else b'\x01'
		if self.terrorists is not None:
			tmp82 = b''
			tmp82 += struct.pack('I', len(self.terrorists))
			while len(tmp82) and tmp82[-1] == b'\x00'[0]:
				tmp82 = tmp82[:-1]
			s += struct.pack('B', len(tmp82))
			s += tmp82
			
			for tmp83 in self.terrorists:
				s += b'\x00' if tmp83 is None else b'\x01'
				if tmp83 is not None:
					s += tmp83.serialize()
		
		# serialize self.polices
		s += b'\x00' if self.polices is None else b'\x01'
		if self.polices is not None:
			tmp84 = b''
			tmp84 += struct.pack('I', len(self.polices))
			while len(tmp84) and tmp84[-1] == b'\x00'[0]:
				tmp84 = tmp84[:-1]
			s += struct.pack('B', len(tmp84))
			s += tmp84
			
			for tmp85 in self.polices:
				s += b'\x00' if tmp85 is None else b'\x01'
				if tmp85 is not None:
					s += tmp85.serialize()
		
		# serialize self.constants
		s += b'\x00' if self.constants is None else b'\x01'
		if self.constants is not None:
			s += self.constants.serialize()
		
		return s
	

	def deserialize(self, s, offset=0):
		# deserialize self.width
		tmp86 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp86:
			self.width = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.width = None
		
		# deserialize self.height
		tmp87 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp87:
			self.height = struct.unpack('i', s[offset:offset + 4])[0]
			offset += 4
		else:
			self.height = None
		
		# deserialize self.board
		tmp88 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp88:
			tmp89 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp90 = s[offset:offset + tmp89]
			offset += tmp89
			tmp90 += b'\x00' * (4 - tmp89)
			tmp91 = struct.unpack('I', tmp90)[0]
			
			self.board = []
			for tmp92 in range(tmp91):
				tmp94 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp94:
					tmp95 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp96 = s[offset:offset + tmp95]
					offset += tmp95
					tmp96 += b'\x00' * (4 - tmp95)
					tmp97 = struct.unpack('I', tmp96)[0]
					
					tmp93 = []
					for tmp98 in range(tmp97):
						tmp100 = struct.unpack('B', s[offset:offset + 1])[0]
						offset += 1
						if tmp100:
							tmp101 = struct.unpack('b', s[offset:offset + 1])[0]
							offset += 1
							tmp99 = ECell(tmp101)
						else:
							tmp99 = None
						tmp93.append(tmp99)
				else:
					tmp93 = None
				self.board.append(tmp93)
		else:
			self.board = None
		
		# deserialize self.scores
		tmp102 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp102:
			tmp103 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp104 = s[offset:offset + tmp103]
			offset += tmp103
			tmp104 += b'\x00' * (4 - tmp103)
			tmp105 = struct.unpack('I', tmp104)[0]
			
			self.scores = {}
			for tmp106 in range(tmp105):
				tmp109 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp109:
					tmp110 = struct.unpack('B', s[offset:offset + 1])[0]
					offset += 1
					tmp111 = s[offset:offset + tmp110]
					offset += tmp110
					tmp111 += b'\x00' * (4 - tmp110)
					tmp112 = struct.unpack('I', tmp111)[0]
					
					tmp107 = s[offset:offset + tmp112].decode('ISO-8859-1') if PY3 else s[offset:offset + tmp112]
					offset += tmp112
				else:
					tmp107 = None
				tmp113 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp113:
					tmp108 = struct.unpack('f', s[offset:offset + 4])[0]
					offset += 4
				else:
					tmp108 = None
				self.scores[tmp107] = tmp108
		else:
			self.scores = None
		
		# deserialize self.bombs
		tmp114 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp114:
			tmp115 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp116 = s[offset:offset + tmp115]
			offset += tmp115
			tmp116 += b'\x00' * (4 - tmp115)
			tmp117 = struct.unpack('I', tmp116)[0]
			
			self.bombs = []
			for tmp118 in range(tmp117):
				tmp120 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp120:
					tmp119 = Bomb()
					offset = tmp119.deserialize(s, offset)
				else:
					tmp119 = None
				self.bombs.append(tmp119)
		else:
			self.bombs = None
		
		# deserialize self.terrorists
		tmp121 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp121:
			tmp122 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp123 = s[offset:offset + tmp122]
			offset += tmp122
			tmp123 += b'\x00' * (4 - tmp122)
			tmp124 = struct.unpack('I', tmp123)[0]
			
			self.terrorists = []
			for tmp125 in range(tmp124):
				tmp127 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp127:
					tmp126 = Terrorist()
					offset = tmp126.deserialize(s, offset)
				else:
					tmp126 = None
				self.terrorists.append(tmp126)
		else:
			self.terrorists = None
		
		# deserialize self.polices
		tmp128 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp128:
			tmp129 = struct.unpack('B', s[offset:offset + 1])[0]
			offset += 1
			tmp130 = s[offset:offset + tmp129]
			offset += tmp129
			tmp130 += b'\x00' * (4 - tmp129)
			tmp131 = struct.unpack('I', tmp130)[0]
			
			self.polices = []
			for tmp132 in range(tmp131):
				tmp134 = struct.unpack('B', s[offset:offset + 1])[0]
				offset += 1
				if tmp134:
					tmp133 = Police()
					offset = tmp133.deserialize(s, offset)
				else:
					tmp133 = None
				self.polices.append(tmp133)
		else:
			self.polices = None
		
		# deserialize self.constants
		tmp135 = struct.unpack('B', s[offset:offset + 1])[0]
		offset += 1
		if tmp135:
			self.constants = Constants()
			offset = self.constants.deserialize(s, offset)
		else:
			self.constants = None
		
		return offset
