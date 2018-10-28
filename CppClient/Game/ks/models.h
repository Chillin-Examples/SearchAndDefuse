#ifndef _KS_MODELS_H_
#define _KS_MODELS_H_

#include <string>
#include <vector>
#include <map>
#include <array>


namespace ks
{

#ifndef _KS_OBJECT_
#define _KS_OBJECT_

class KSObject
{
public:
	static inline const std::string nameStatic() { return ""; }
	virtual inline const std::string name() const = 0;
	virtual std::string serialize() const = 0;
	virtual unsigned int deserialize(const std::string &, unsigned int = 0) = 0;
};

#endif // _KS_OBJECT_


namespace models
{

enum class ECell
{
	Empty = 0,
	SmallBombSite = 1,
	MediumBombSite = 2,
	LargeBombSite = 3,
	VastBombSite = 4,
	Wall = 5,
};


enum class EDirection
{
	Up = 0,
	Right = 1,
	Down = 2,
	Left = 3,
};


enum class ESoundIntensity
{
	Weak = 0,
	Normal = 1,
	Strong = 2,
};


class Constants : public KSObject
{

protected:

	int __bomb_planting_time;
	int __bomb_defusion_time;
	int __bomb_explosion_time;
	int __bomb_planting_score;
	int __bomb_defusion_score;
	int __bomb_explosion_score;
	int __terrorist_vision_distance;
	int __terrorist_arrest_score;
	int __police_vision_distance;
	std::map<ESoundIntensity, int> __sound_ranges;
	int __max_cycles;

	bool __has_bomb_planting_time;
	bool __has_bomb_defusion_time;
	bool __has_bomb_explosion_time;
	bool __has_bomb_planting_score;
	bool __has_bomb_defusion_score;
	bool __has_bomb_explosion_score;
	bool __has_terrorist_vision_distance;
	bool __has_terrorist_arrest_score;
	bool __has_police_vision_distance;
	bool __has_sound_ranges;
	bool __has_max_cycles;


public: // getters

	inline int bomb_planting_time() const
	{
		return __bomb_planting_time;
	}
	
	inline int bomb_defusion_time() const
	{
		return __bomb_defusion_time;
	}
	
	inline int bomb_explosion_time() const
	{
		return __bomb_explosion_time;
	}
	
	inline int bomb_planting_score() const
	{
		return __bomb_planting_score;
	}
	
	inline int bomb_defusion_score() const
	{
		return __bomb_defusion_score;
	}
	
	inline int bomb_explosion_score() const
	{
		return __bomb_explosion_score;
	}
	
	inline int terrorist_vision_distance() const
	{
		return __terrorist_vision_distance;
	}
	
	inline int terrorist_arrest_score() const
	{
		return __terrorist_arrest_score;
	}
	
	inline int police_vision_distance() const
	{
		return __police_vision_distance;
	}
	
	inline std::map<ESoundIntensity, int> sound_ranges() const
	{
		return __sound_ranges;
	}
	
	inline int max_cycles() const
	{
		return __max_cycles;
	}
	

public: // reference getters

	inline int &ref_bomb_planting_time() const
	{
		return (int&) __bomb_planting_time;
	}
	
	inline int &ref_bomb_defusion_time() const
	{
		return (int&) __bomb_defusion_time;
	}
	
	inline int &ref_bomb_explosion_time() const
	{
		return (int&) __bomb_explosion_time;
	}
	
	inline int &ref_bomb_planting_score() const
	{
		return (int&) __bomb_planting_score;
	}
	
	inline int &ref_bomb_defusion_score() const
	{
		return (int&) __bomb_defusion_score;
	}
	
	inline int &ref_bomb_explosion_score() const
	{
		return (int&) __bomb_explosion_score;
	}
	
	inline int &ref_terrorist_vision_distance() const
	{
		return (int&) __terrorist_vision_distance;
	}
	
	inline int &ref_terrorist_arrest_score() const
	{
		return (int&) __terrorist_arrest_score;
	}
	
	inline int &ref_police_vision_distance() const
	{
		return (int&) __police_vision_distance;
	}
	
	inline std::map<ESoundIntensity, int> &ref_sound_ranges() const
	{
		return (std::map<ESoundIntensity, int>&) __sound_ranges;
	}
	
	inline int &ref_max_cycles() const
	{
		return (int&) __max_cycles;
	}
	

public: // setters

	inline void bomb_planting_time(const int &bomb_planting_time)
	{
		__bomb_planting_time = bomb_planting_time;
		has_bomb_planting_time(true);
	}
	
	inline void bomb_defusion_time(const int &bomb_defusion_time)
	{
		__bomb_defusion_time = bomb_defusion_time;
		has_bomb_defusion_time(true);
	}
	
	inline void bomb_explosion_time(const int &bomb_explosion_time)
	{
		__bomb_explosion_time = bomb_explosion_time;
		has_bomb_explosion_time(true);
	}
	
	inline void bomb_planting_score(const int &bomb_planting_score)
	{
		__bomb_planting_score = bomb_planting_score;
		has_bomb_planting_score(true);
	}
	
	inline void bomb_defusion_score(const int &bomb_defusion_score)
	{
		__bomb_defusion_score = bomb_defusion_score;
		has_bomb_defusion_score(true);
	}
	
	inline void bomb_explosion_score(const int &bomb_explosion_score)
	{
		__bomb_explosion_score = bomb_explosion_score;
		has_bomb_explosion_score(true);
	}
	
	inline void terrorist_vision_distance(const int &terrorist_vision_distance)
	{
		__terrorist_vision_distance = terrorist_vision_distance;
		has_terrorist_vision_distance(true);
	}
	
	inline void terrorist_arrest_score(const int &terrorist_arrest_score)
	{
		__terrorist_arrest_score = terrorist_arrest_score;
		has_terrorist_arrest_score(true);
	}
	
	inline void police_vision_distance(const int &police_vision_distance)
	{
		__police_vision_distance = police_vision_distance;
		has_police_vision_distance(true);
	}
	
	inline void sound_ranges(const std::map<ESoundIntensity, int> &sound_ranges)
	{
		__sound_ranges = sound_ranges;
		has_sound_ranges(true);
	}
	
	inline void max_cycles(const int &max_cycles)
	{
		__max_cycles = max_cycles;
		has_max_cycles(true);
	}
	

public: // has_attribute getters

	inline bool has_bomb_planting_time() const
	{
		return __has_bomb_planting_time;
	}
	
	inline bool has_bomb_defusion_time() const
	{
		return __has_bomb_defusion_time;
	}
	
	inline bool has_bomb_explosion_time() const
	{
		return __has_bomb_explosion_time;
	}
	
	inline bool has_bomb_planting_score() const
	{
		return __has_bomb_planting_score;
	}
	
	inline bool has_bomb_defusion_score() const
	{
		return __has_bomb_defusion_score;
	}
	
	inline bool has_bomb_explosion_score() const
	{
		return __has_bomb_explosion_score;
	}
	
	inline bool has_terrorist_vision_distance() const
	{
		return __has_terrorist_vision_distance;
	}
	
	inline bool has_terrorist_arrest_score() const
	{
		return __has_terrorist_arrest_score;
	}
	
	inline bool has_police_vision_distance() const
	{
		return __has_police_vision_distance;
	}
	
	inline bool has_sound_ranges() const
	{
		return __has_sound_ranges;
	}
	
	inline bool has_max_cycles() const
	{
		return __has_max_cycles;
	}
	

public: // has_attribute setters

	inline void has_bomb_planting_time(const bool &has_bomb_planting_time)
	{
		__has_bomb_planting_time = has_bomb_planting_time;
	}
	
	inline void has_bomb_defusion_time(const bool &has_bomb_defusion_time)
	{
		__has_bomb_defusion_time = has_bomb_defusion_time;
	}
	
	inline void has_bomb_explosion_time(const bool &has_bomb_explosion_time)
	{
		__has_bomb_explosion_time = has_bomb_explosion_time;
	}
	
	inline void has_bomb_planting_score(const bool &has_bomb_planting_score)
	{
		__has_bomb_planting_score = has_bomb_planting_score;
	}
	
	inline void has_bomb_defusion_score(const bool &has_bomb_defusion_score)
	{
		__has_bomb_defusion_score = has_bomb_defusion_score;
	}
	
	inline void has_bomb_explosion_score(const bool &has_bomb_explosion_score)
	{
		__has_bomb_explosion_score = has_bomb_explosion_score;
	}
	
	inline void has_terrorist_vision_distance(const bool &has_terrorist_vision_distance)
	{
		__has_terrorist_vision_distance = has_terrorist_vision_distance;
	}
	
	inline void has_terrorist_arrest_score(const bool &has_terrorist_arrest_score)
	{
		__has_terrorist_arrest_score = has_terrorist_arrest_score;
	}
	
	inline void has_police_vision_distance(const bool &has_police_vision_distance)
	{
		__has_police_vision_distance = has_police_vision_distance;
	}
	
	inline void has_sound_ranges(const bool &has_sound_ranges)
	{
		__has_sound_ranges = has_sound_ranges;
	}
	
	inline void has_max_cycles(const bool &has_max_cycles)
	{
		__has_max_cycles = has_max_cycles;
	}
	

public:

	Constants()
	{
		has_bomb_planting_time(false);
		has_bomb_defusion_time(false);
		has_bomb_explosion_time(false);
		has_bomb_planting_score(false);
		has_bomb_defusion_score(false);
		has_bomb_explosion_score(false);
		has_terrorist_vision_distance(false);
		has_terrorist_arrest_score(false);
		has_police_vision_distance(false);
		has_sound_ranges(false);
		has_max_cycles(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Constants";
	}
	
	virtual inline const std::string name() const
	{
		return "Constants";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize bomb_planting_time
		s += __has_bomb_planting_time;
		if (__has_bomb_planting_time)
		{
			int tmp1 = __bomb_planting_time;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize bomb_defusion_time
		s += __has_bomb_defusion_time;
		if (__has_bomb_defusion_time)
		{
			int tmp4 = __bomb_defusion_time;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(int));
		}
		
		// serialize bomb_explosion_time
		s += __has_bomb_explosion_time;
		if (__has_bomb_explosion_time)
		{
			int tmp7 = __bomb_explosion_time;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize bomb_planting_score
		s += __has_bomb_planting_score;
		if (__has_bomb_planting_score)
		{
			int tmp10 = __bomb_planting_score;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		// serialize bomb_defusion_score
		s += __has_bomb_defusion_score;
		if (__has_bomb_defusion_score)
		{
			int tmp13 = __bomb_defusion_score;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(int));
		}
		
		// serialize bomb_explosion_score
		s += __has_bomb_explosion_score;
		if (__has_bomb_explosion_score)
		{
			int tmp16 = __bomb_explosion_score;
			auto tmp17 = reinterpret_cast<char*>(&tmp16);
			s += std::string(tmp17, sizeof(int));
		}
		
		// serialize terrorist_vision_distance
		s += __has_terrorist_vision_distance;
		if (__has_terrorist_vision_distance)
		{
			int tmp19 = __terrorist_vision_distance;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(int));
		}
		
		// serialize terrorist_arrest_score
		s += __has_terrorist_arrest_score;
		if (__has_terrorist_arrest_score)
		{
			int tmp22 = __terrorist_arrest_score;
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			s += std::string(tmp23, sizeof(int));
		}
		
		// serialize police_vision_distance
		s += __has_police_vision_distance;
		if (__has_police_vision_distance)
		{
			int tmp25 = __police_vision_distance;
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(int));
		}
		
		// serialize sound_ranges
		s += __has_sound_ranges;
		if (__has_sound_ranges)
		{
			std::string tmp27 = "";
			unsigned int tmp29 = __sound_ranges.size();
			auto tmp30 = reinterpret_cast<char*>(&tmp29);
			tmp27 += std::string(tmp30, sizeof(unsigned int));
			while (tmp27.size() && tmp27.back() == 0)
				tmp27.pop_back();
			unsigned char tmp32 = tmp27.size();
			auto tmp33 = reinterpret_cast<char*>(&tmp32);
			s += std::string(tmp33, sizeof(unsigned char));
			s += tmp27;
			
			for (auto &tmp34 : __sound_ranges)
			{
				s += '\x01';
				char tmp36 = (char) tmp34.first;
				auto tmp37 = reinterpret_cast<char*>(&tmp36);
				s += std::string(tmp37, sizeof(char));
				
				s += '\x01';
				int tmp39 = tmp34.second;
				auto tmp40 = reinterpret_cast<char*>(&tmp39);
				s += std::string(tmp40, sizeof(int));
			}
		}
		
		// serialize max_cycles
		s += __has_max_cycles;
		if (__has_max_cycles)
		{
			int tmp42 = __max_cycles;
			auto tmp43 = reinterpret_cast<char*>(&tmp42);
			s += std::string(tmp43, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize bomb_planting_time
		__has_bomb_planting_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_planting_time)
		{
			__bomb_planting_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bomb_defusion_time
		__has_bomb_defusion_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_defusion_time)
		{
			__bomb_defusion_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bomb_explosion_time
		__has_bomb_explosion_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_explosion_time)
		{
			__bomb_explosion_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bomb_planting_score
		__has_bomb_planting_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_planting_score)
		{
			__bomb_planting_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bomb_defusion_score
		__has_bomb_defusion_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_defusion_score)
		{
			__bomb_defusion_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bomb_explosion_score
		__has_bomb_explosion_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_explosion_score)
		{
			__bomb_explosion_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize terrorist_vision_distance
		__has_terrorist_vision_distance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorist_vision_distance)
		{
			__terrorist_vision_distance = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize terrorist_arrest_score
		__has_terrorist_arrest_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorist_arrest_score)
		{
			__terrorist_arrest_score = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize police_vision_distance
		__has_police_vision_distance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_police_vision_distance)
		{
			__police_vision_distance = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize sound_ranges
		__has_sound_ranges = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_sound_ranges)
		{
			unsigned char tmp44;
			tmp44 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp45 = std::string(&s[offset], tmp44);
			offset += tmp44;
			while (tmp45.size() < sizeof(unsigned int))
				tmp45 += '\x00';
			unsigned int tmp46;
			tmp46 = *((unsigned int*) (&tmp45[0]));
			
			__sound_ranges.clear();
			for (unsigned int tmp47 = 0; tmp47 < tmp46; tmp47++)
			{
				ESoundIntensity tmp48;
				offset++;
				char tmp50;
				tmp50 = *((char*) (&s[offset]));
				offset += sizeof(char);
				tmp48 = (ESoundIntensity) tmp50;
				
				int tmp49;
				offset++;
				tmp49 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__sound_ranges[tmp48] = tmp49;
			}
		}
		
		// deserialize max_cycles
		__has_max_cycles = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_max_cycles)
		{
			__max_cycles = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Position : public KSObject
{

protected:

	int __x;
	int __y;

	bool __has_x;
	bool __has_y;


public: // getters

	inline int x() const
	{
		return __x;
	}
	
	inline int y() const
	{
		return __y;
	}
	

public: // reference getters

	inline int &ref_x() const
	{
		return (int&) __x;
	}
	
	inline int &ref_y() const
	{
		return (int&) __y;
	}
	

public: // setters

	inline void x(const int &x)
	{
		__x = x;
		has_x(true);
	}
	
	inline void y(const int &y)
	{
		__y = y;
		has_y(true);
	}
	

public: // has_attribute getters

	inline bool has_x() const
	{
		return __has_x;
	}
	
	inline bool has_y() const
	{
		return __has_y;
	}
	

public: // has_attribute setters

	inline void has_x(const bool &has_x)
	{
		__has_x = has_x;
	}
	
	inline void has_y(const bool &has_y)
	{
		__has_y = has_y;
	}
	

public:

	Position()
	{
		has_x(false);
		has_y(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Position";
	}
	
	virtual inline const std::string name() const
	{
		return "Position";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize x
		s += __has_x;
		if (__has_x)
		{
			int tmp52 = __x;
			auto tmp53 = reinterpret_cast<char*>(&tmp52);
			s += std::string(tmp53, sizeof(int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			int tmp55 = __y;
			auto tmp56 = reinterpret_cast<char*>(&tmp55);
			s += std::string(tmp56, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize x
		__has_x = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_x)
		{
			__x = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize y
		__has_y = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_y)
		{
			__y = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Bomb : public KSObject
{

protected:

	Position __position;
	int __explosion_remaining_time;

	bool __has_position;
	bool __has_explosion_remaining_time;


public: // getters

	inline Position position() const
	{
		return __position;
	}
	
	inline int explosion_remaining_time() const
	{
		return __explosion_remaining_time;
	}
	

public: // reference getters

	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline int &ref_explosion_remaining_time() const
	{
		return (int&) __explosion_remaining_time;
	}
	

public: // setters

	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void explosion_remaining_time(const int &explosion_remaining_time)
	{
		__explosion_remaining_time = explosion_remaining_time;
		has_explosion_remaining_time(true);
	}
	

public: // has_attribute getters

	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_explosion_remaining_time() const
	{
		return __has_explosion_remaining_time;
	}
	

public: // has_attribute setters

	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_explosion_remaining_time(const bool &has_explosion_remaining_time)
	{
		__has_explosion_remaining_time = has_explosion_remaining_time;
	}
	

public:

	Bomb()
	{
		has_position(false);
		has_explosion_remaining_time(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Bomb";
	}
	
	virtual inline const std::string name() const
	{
		return "Bomb";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize explosion_remaining_time
		s += __has_explosion_remaining_time;
		if (__has_explosion_remaining_time)
		{
			int tmp58 = __explosion_remaining_time;
			auto tmp59 = reinterpret_cast<char*>(&tmp58);
			s += std::string(tmp59, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize explosion_remaining_time
		__has_explosion_remaining_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_explosion_remaining_time)
		{
			__explosion_remaining_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		return offset;
	}
};


class Terrorist : public KSObject
{

protected:

	int __id;
	Position __position;
	int __planting_remaining_time;
	std::vector<int> __footstep_sounds;
	bool __is_arrested;

	bool __has_id;
	bool __has_position;
	bool __has_planting_remaining_time;
	bool __has_footstep_sounds;
	bool __has_is_arrested;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline int planting_remaining_time() const
	{
		return __planting_remaining_time;
	}
	
	inline std::vector<int> footstep_sounds() const
	{
		return __footstep_sounds;
	}
	
	inline bool is_arrested() const
	{
		return __is_arrested;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline int &ref_planting_remaining_time() const
	{
		return (int&) __planting_remaining_time;
	}
	
	inline std::vector<int> &ref_footstep_sounds() const
	{
		return (std::vector<int>&) __footstep_sounds;
	}
	
	inline bool &ref_is_arrested() const
	{
		return (bool&) __is_arrested;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void planting_remaining_time(const int &planting_remaining_time)
	{
		__planting_remaining_time = planting_remaining_time;
		has_planting_remaining_time(true);
	}
	
	inline void footstep_sounds(const std::vector<int> &footstep_sounds)
	{
		__footstep_sounds = footstep_sounds;
		has_footstep_sounds(true);
	}
	
	inline void is_arrested(const bool &is_arrested)
	{
		__is_arrested = is_arrested;
		has_is_arrested(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_planting_remaining_time() const
	{
		return __has_planting_remaining_time;
	}
	
	inline bool has_footstep_sounds() const
	{
		return __has_footstep_sounds;
	}
	
	inline bool has_is_arrested() const
	{
		return __has_is_arrested;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_planting_remaining_time(const bool &has_planting_remaining_time)
	{
		__has_planting_remaining_time = has_planting_remaining_time;
	}
	
	inline void has_footstep_sounds(const bool &has_footstep_sounds)
	{
		__has_footstep_sounds = has_footstep_sounds;
	}
	
	inline void has_is_arrested(const bool &has_is_arrested)
	{
		__has_is_arrested = has_is_arrested;
	}
	

public:

	Terrorist()
	{
		has_id(false);
		has_position(false);
		has_planting_remaining_time(false);
		has_footstep_sounds(false);
		has_is_arrested(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Terrorist";
	}
	
	virtual inline const std::string name() const
	{
		return "Terrorist";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp61 = __id;
			auto tmp62 = reinterpret_cast<char*>(&tmp61);
			s += std::string(tmp62, sizeof(int));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize planting_remaining_time
		s += __has_planting_remaining_time;
		if (__has_planting_remaining_time)
		{
			int tmp64 = __planting_remaining_time;
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			s += std::string(tmp65, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp66 = "";
			unsigned int tmp68 = __footstep_sounds.size();
			auto tmp69 = reinterpret_cast<char*>(&tmp68);
			tmp66 += std::string(tmp69, sizeof(unsigned int));
			while (tmp66.size() && tmp66.back() == 0)
				tmp66.pop_back();
			unsigned char tmp71 = tmp66.size();
			auto tmp72 = reinterpret_cast<char*>(&tmp71);
			s += std::string(tmp72, sizeof(unsigned char));
			s += tmp66;
			
			for (auto &tmp73 : __footstep_sounds)
			{
				s += '\x01';
				int tmp75 = tmp73;
				auto tmp76 = reinterpret_cast<char*>(&tmp75);
				s += std::string(tmp76, sizeof(int));
			}
		}
		
		// serialize is_arrested
		s += __has_is_arrested;
		if (__has_is_arrested)
		{
			bool tmp78 = __is_arrested;
			auto tmp79 = reinterpret_cast<char*>(&tmp78);
			s += std::string(tmp79, sizeof(bool));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize planting_remaining_time
		__has_planting_remaining_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_planting_remaining_time)
		{
			__planting_remaining_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize footstep_sounds
		__has_footstep_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_footstep_sounds)
		{
			unsigned char tmp80;
			tmp80 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp81 = std::string(&s[offset], tmp80);
			offset += tmp80;
			while (tmp81.size() < sizeof(unsigned int))
				tmp81 += '\x00';
			unsigned int tmp82;
			tmp82 = *((unsigned int*) (&tmp81[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp83 = 0; tmp83 < tmp82; tmp83++)
			{
				int tmp84;
				offset++;
				tmp84 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp84);
			}
		}
		
		// deserialize is_arrested
		__has_is_arrested = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_is_arrested)
		{
			__is_arrested = *((bool*) (&s[offset]));
			offset += sizeof(bool);
		}
		
		return offset;
	}
};


class Police : public KSObject
{

protected:

	int __id;
	Position __position;
	int __defusion_remaining_time;
	std::vector<int> __footstep_sounds;
	std::vector<int> __bomb_sounds;
	bool __is_visible;

	bool __has_id;
	bool __has_position;
	bool __has_defusion_remaining_time;
	bool __has_footstep_sounds;
	bool __has_bomb_sounds;
	bool __has_is_visible;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline int defusion_remaining_time() const
	{
		return __defusion_remaining_time;
	}
	
	inline std::vector<int> footstep_sounds() const
	{
		return __footstep_sounds;
	}
	
	inline std::vector<int> bomb_sounds() const
	{
		return __bomb_sounds;
	}
	
	inline bool is_visible() const
	{
		return __is_visible;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline int &ref_defusion_remaining_time() const
	{
		return (int&) __defusion_remaining_time;
	}
	
	inline std::vector<int> &ref_footstep_sounds() const
	{
		return (std::vector<int>&) __footstep_sounds;
	}
	
	inline std::vector<int> &ref_bomb_sounds() const
	{
		return (std::vector<int>&) __bomb_sounds;
	}
	
	inline bool &ref_is_visible() const
	{
		return (bool&) __is_visible;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void defusion_remaining_time(const int &defusion_remaining_time)
	{
		__defusion_remaining_time = defusion_remaining_time;
		has_defusion_remaining_time(true);
	}
	
	inline void footstep_sounds(const std::vector<int> &footstep_sounds)
	{
		__footstep_sounds = footstep_sounds;
		has_footstep_sounds(true);
	}
	
	inline void bomb_sounds(const std::vector<int> &bomb_sounds)
	{
		__bomb_sounds = bomb_sounds;
		has_bomb_sounds(true);
	}
	
	inline void is_visible(const bool &is_visible)
	{
		__is_visible = is_visible;
		has_is_visible(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_defusion_remaining_time() const
	{
		return __has_defusion_remaining_time;
	}
	
	inline bool has_footstep_sounds() const
	{
		return __has_footstep_sounds;
	}
	
	inline bool has_bomb_sounds() const
	{
		return __has_bomb_sounds;
	}
	
	inline bool has_is_visible() const
	{
		return __has_is_visible;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_defusion_remaining_time(const bool &has_defusion_remaining_time)
	{
		__has_defusion_remaining_time = has_defusion_remaining_time;
	}
	
	inline void has_footstep_sounds(const bool &has_footstep_sounds)
	{
		__has_footstep_sounds = has_footstep_sounds;
	}
	
	inline void has_bomb_sounds(const bool &has_bomb_sounds)
	{
		__has_bomb_sounds = has_bomb_sounds;
	}
	
	inline void has_is_visible(const bool &has_is_visible)
	{
		__has_is_visible = has_is_visible;
	}
	

public:

	Police()
	{
		has_id(false);
		has_position(false);
		has_defusion_remaining_time(false);
		has_footstep_sounds(false);
		has_bomb_sounds(false);
		has_is_visible(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Police";
	}
	
	virtual inline const std::string name() const
	{
		return "Police";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp86 = __id;
			auto tmp87 = reinterpret_cast<char*>(&tmp86);
			s += std::string(tmp87, sizeof(int));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize defusion_remaining_time
		s += __has_defusion_remaining_time;
		if (__has_defusion_remaining_time)
		{
			int tmp89 = __defusion_remaining_time;
			auto tmp90 = reinterpret_cast<char*>(&tmp89);
			s += std::string(tmp90, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp91 = "";
			unsigned int tmp93 = __footstep_sounds.size();
			auto tmp94 = reinterpret_cast<char*>(&tmp93);
			tmp91 += std::string(tmp94, sizeof(unsigned int));
			while (tmp91.size() && tmp91.back() == 0)
				tmp91.pop_back();
			unsigned char tmp96 = tmp91.size();
			auto tmp97 = reinterpret_cast<char*>(&tmp96);
			s += std::string(tmp97, sizeof(unsigned char));
			s += tmp91;
			
			for (auto &tmp98 : __footstep_sounds)
			{
				s += '\x01';
				int tmp100 = tmp98;
				auto tmp101 = reinterpret_cast<char*>(&tmp100);
				s += std::string(tmp101, sizeof(int));
			}
		}
		
		// serialize bomb_sounds
		s += __has_bomb_sounds;
		if (__has_bomb_sounds)
		{
			std::string tmp102 = "";
			unsigned int tmp104 = __bomb_sounds.size();
			auto tmp105 = reinterpret_cast<char*>(&tmp104);
			tmp102 += std::string(tmp105, sizeof(unsigned int));
			while (tmp102.size() && tmp102.back() == 0)
				tmp102.pop_back();
			unsigned char tmp107 = tmp102.size();
			auto tmp108 = reinterpret_cast<char*>(&tmp107);
			s += std::string(tmp108, sizeof(unsigned char));
			s += tmp102;
			
			for (auto &tmp109 : __bomb_sounds)
			{
				s += '\x01';
				int tmp111 = tmp109;
				auto tmp112 = reinterpret_cast<char*>(&tmp111);
				s += std::string(tmp112, sizeof(int));
			}
		}
		
		// serialize is_visible
		s += __has_is_visible;
		if (__has_is_visible)
		{
			bool tmp114 = __is_visible;
			auto tmp115 = reinterpret_cast<char*>(&tmp114);
			s += std::string(tmp115, sizeof(bool));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize id
		__has_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_id)
		{
			__id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize position
		__has_position = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_position)
		{
			offset = __position.deserialize(s, offset);
		}
		
		// deserialize defusion_remaining_time
		__has_defusion_remaining_time = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_defusion_remaining_time)
		{
			__defusion_remaining_time = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize footstep_sounds
		__has_footstep_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_footstep_sounds)
		{
			unsigned char tmp116;
			tmp116 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp117 = std::string(&s[offset], tmp116);
			offset += tmp116;
			while (tmp117.size() < sizeof(unsigned int))
				tmp117 += '\x00';
			unsigned int tmp118;
			tmp118 = *((unsigned int*) (&tmp117[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp119 = 0; tmp119 < tmp118; tmp119++)
			{
				int tmp120;
				offset++;
				tmp120 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp120);
			}
		}
		
		// deserialize bomb_sounds
		__has_bomb_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_sounds)
		{
			unsigned char tmp121;
			tmp121 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp122 = std::string(&s[offset], tmp121);
			offset += tmp121;
			while (tmp122.size() < sizeof(unsigned int))
				tmp122 += '\x00';
			unsigned int tmp123;
			tmp123 = *((unsigned int*) (&tmp122[0]));
			
			__bomb_sounds.clear();
			for (unsigned int tmp124 = 0; tmp124 < tmp123; tmp124++)
			{
				int tmp125;
				offset++;
				tmp125 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bomb_sounds.push_back(tmp125);
			}
		}
		
		// deserialize is_visible
		__has_is_visible = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_is_visible)
		{
			__is_visible = *((bool*) (&s[offset]));
			offset += sizeof(bool);
		}
		
		return offset;
	}
};


class World : public KSObject
{

protected:

	int __width;
	int __height;
	std::vector<std::vector<ECell>> __board;
	std::map<std::string, int> __scores;
	std::vector<Bomb> __bombs;
	std::vector<Terrorist> __terrorists;
	std::vector<Police> __polices;
	Constants __constants;

	bool __has_width;
	bool __has_height;
	bool __has_board;
	bool __has_scores;
	bool __has_bombs;
	bool __has_terrorists;
	bool __has_polices;
	bool __has_constants;


public: // getters

	inline int width() const
	{
		return __width;
	}
	
	inline int height() const
	{
		return __height;
	}
	
	inline std::vector<std::vector<ECell>> board() const
	{
		return __board;
	}
	
	inline std::map<std::string, int> scores() const
	{
		return __scores;
	}
	
	inline std::vector<Bomb> bombs() const
	{
		return __bombs;
	}
	
	inline std::vector<Terrorist> terrorists() const
	{
		return __terrorists;
	}
	
	inline std::vector<Police> polices() const
	{
		return __polices;
	}
	
	inline Constants constants() const
	{
		return __constants;
	}
	

public: // reference getters

	inline int &ref_width() const
	{
		return (int&) __width;
	}
	
	inline int &ref_height() const
	{
		return (int&) __height;
	}
	
	inline std::vector<std::vector<ECell>> &ref_board() const
	{
		return (std::vector<std::vector<ECell>>&) __board;
	}
	
	inline std::map<std::string, int> &ref_scores() const
	{
		return (std::map<std::string, int>&) __scores;
	}
	
	inline std::vector<Bomb> &ref_bombs() const
	{
		return (std::vector<Bomb>&) __bombs;
	}
	
	inline std::vector<Terrorist> &ref_terrorists() const
	{
		return (std::vector<Terrorist>&) __terrorists;
	}
	
	inline std::vector<Police> &ref_polices() const
	{
		return (std::vector<Police>&) __polices;
	}
	
	inline Constants &ref_constants() const
	{
		return (Constants&) __constants;
	}
	

public: // setters

	inline void width(const int &width)
	{
		__width = width;
		has_width(true);
	}
	
	inline void height(const int &height)
	{
		__height = height;
		has_height(true);
	}
	
	inline void board(const std::vector<std::vector<ECell>> &board)
	{
		__board = board;
		has_board(true);
	}
	
	inline void scores(const std::map<std::string, int> &scores)
	{
		__scores = scores;
		has_scores(true);
	}
	
	inline void bombs(const std::vector<Bomb> &bombs)
	{
		__bombs = bombs;
		has_bombs(true);
	}
	
	inline void terrorists(const std::vector<Terrorist> &terrorists)
	{
		__terrorists = terrorists;
		has_terrorists(true);
	}
	
	inline void polices(const std::vector<Police> &polices)
	{
		__polices = polices;
		has_polices(true);
	}
	
	inline void constants(const Constants &constants)
	{
		__constants = constants;
		has_constants(true);
	}
	

public: // has_attribute getters

	inline bool has_width() const
	{
		return __has_width;
	}
	
	inline bool has_height() const
	{
		return __has_height;
	}
	
	inline bool has_board() const
	{
		return __has_board;
	}
	
	inline bool has_scores() const
	{
		return __has_scores;
	}
	
	inline bool has_bombs() const
	{
		return __has_bombs;
	}
	
	inline bool has_terrorists() const
	{
		return __has_terrorists;
	}
	
	inline bool has_polices() const
	{
		return __has_polices;
	}
	
	inline bool has_constants() const
	{
		return __has_constants;
	}
	

public: // has_attribute setters

	inline void has_width(const bool &has_width)
	{
		__has_width = has_width;
	}
	
	inline void has_height(const bool &has_height)
	{
		__has_height = has_height;
	}
	
	inline void has_board(const bool &has_board)
	{
		__has_board = has_board;
	}
	
	inline void has_scores(const bool &has_scores)
	{
		__has_scores = has_scores;
	}
	
	inline void has_bombs(const bool &has_bombs)
	{
		__has_bombs = has_bombs;
	}
	
	inline void has_terrorists(const bool &has_terrorists)
	{
		__has_terrorists = has_terrorists;
	}
	
	inline void has_polices(const bool &has_polices)
	{
		__has_polices = has_polices;
	}
	
	inline void has_constants(const bool &has_constants)
	{
		__has_constants = has_constants;
	}
	

public:

	World()
	{
		has_width(false);
		has_height(false);
		has_board(false);
		has_scores(false);
		has_bombs(false);
		has_terrorists(false);
		has_polices(false);
		has_constants(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "World";
	}
	
	virtual inline const std::string name() const
	{
		return "World";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize width
		s += __has_width;
		if (__has_width)
		{
			int tmp127 = __width;
			auto tmp128 = reinterpret_cast<char*>(&tmp127);
			s += std::string(tmp128, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp130 = __height;
			auto tmp131 = reinterpret_cast<char*>(&tmp130);
			s += std::string(tmp131, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp132 = "";
			unsigned int tmp134 = __board.size();
			auto tmp135 = reinterpret_cast<char*>(&tmp134);
			tmp132 += std::string(tmp135, sizeof(unsigned int));
			while (tmp132.size() && tmp132.back() == 0)
				tmp132.pop_back();
			unsigned char tmp137 = tmp132.size();
			auto tmp138 = reinterpret_cast<char*>(&tmp137);
			s += std::string(tmp138, sizeof(unsigned char));
			s += tmp132;
			
			for (auto &tmp139 : __board)
			{
				s += '\x01';
				std::string tmp140 = "";
				unsigned int tmp142 = tmp139.size();
				auto tmp143 = reinterpret_cast<char*>(&tmp142);
				tmp140 += std::string(tmp143, sizeof(unsigned int));
				while (tmp140.size() && tmp140.back() == 0)
					tmp140.pop_back();
				unsigned char tmp145 = tmp140.size();
				auto tmp146 = reinterpret_cast<char*>(&tmp145);
				s += std::string(tmp146, sizeof(unsigned char));
				s += tmp140;
				
				for (auto &tmp147 : tmp139)
				{
					s += '\x01';
					char tmp149 = (char) tmp147;
					auto tmp150 = reinterpret_cast<char*>(&tmp149);
					s += std::string(tmp150, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp151 = "";
			unsigned int tmp153 = __scores.size();
			auto tmp154 = reinterpret_cast<char*>(&tmp153);
			tmp151 += std::string(tmp154, sizeof(unsigned int));
			while (tmp151.size() && tmp151.back() == 0)
				tmp151.pop_back();
			unsigned char tmp156 = tmp151.size();
			auto tmp157 = reinterpret_cast<char*>(&tmp156);
			s += std::string(tmp157, sizeof(unsigned char));
			s += tmp151;
			
			for (auto &tmp158 : __scores)
			{
				s += '\x01';
				std::string tmp159 = "";
				unsigned int tmp161 = tmp158.first.size();
				auto tmp162 = reinterpret_cast<char*>(&tmp161);
				tmp159 += std::string(tmp162, sizeof(unsigned int));
				while (tmp159.size() && tmp159.back() == 0)
					tmp159.pop_back();
				unsigned char tmp164 = tmp159.size();
				auto tmp165 = reinterpret_cast<char*>(&tmp164);
				s += std::string(tmp165, sizeof(unsigned char));
				s += tmp159;
				
				s += tmp158.first;
				
				s += '\x01';
				int tmp167 = tmp158.second;
				auto tmp168 = reinterpret_cast<char*>(&tmp167);
				s += std::string(tmp168, sizeof(int));
			}
		}
		
		// serialize bombs
		s += __has_bombs;
		if (__has_bombs)
		{
			std::string tmp169 = "";
			unsigned int tmp171 = __bombs.size();
			auto tmp172 = reinterpret_cast<char*>(&tmp171);
			tmp169 += std::string(tmp172, sizeof(unsigned int));
			while (tmp169.size() && tmp169.back() == 0)
				tmp169.pop_back();
			unsigned char tmp174 = tmp169.size();
			auto tmp175 = reinterpret_cast<char*>(&tmp174);
			s += std::string(tmp175, sizeof(unsigned char));
			s += tmp169;
			
			for (auto &tmp176 : __bombs)
			{
				s += '\x01';
				s += tmp176.serialize();
			}
		}
		
		// serialize terrorists
		s += __has_terrorists;
		if (__has_terrorists)
		{
			std::string tmp177 = "";
			unsigned int tmp179 = __terrorists.size();
			auto tmp180 = reinterpret_cast<char*>(&tmp179);
			tmp177 += std::string(tmp180, sizeof(unsigned int));
			while (tmp177.size() && tmp177.back() == 0)
				tmp177.pop_back();
			unsigned char tmp182 = tmp177.size();
			auto tmp183 = reinterpret_cast<char*>(&tmp182);
			s += std::string(tmp183, sizeof(unsigned char));
			s += tmp177;
			
			for (auto &tmp184 : __terrorists)
			{
				s += '\x01';
				s += tmp184.serialize();
			}
		}
		
		// serialize polices
		s += __has_polices;
		if (__has_polices)
		{
			std::string tmp185 = "";
			unsigned int tmp187 = __polices.size();
			auto tmp188 = reinterpret_cast<char*>(&tmp187);
			tmp185 += std::string(tmp188, sizeof(unsigned int));
			while (tmp185.size() && tmp185.back() == 0)
				tmp185.pop_back();
			unsigned char tmp190 = tmp185.size();
			auto tmp191 = reinterpret_cast<char*>(&tmp190);
			s += std::string(tmp191, sizeof(unsigned char));
			s += tmp185;
			
			for (auto &tmp192 : __polices)
			{
				s += '\x01';
				s += tmp192.serialize();
			}
		}
		
		// serialize constants
		s += __has_constants;
		if (__has_constants)
		{
			s += __constants.serialize();
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize width
		__has_width = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_width)
		{
			__width = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize height
		__has_height = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_height)
		{
			__height = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize board
		__has_board = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_board)
		{
			unsigned char tmp193;
			tmp193 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp194 = std::string(&s[offset], tmp193);
			offset += tmp193;
			while (tmp194.size() < sizeof(unsigned int))
				tmp194 += '\x00';
			unsigned int tmp195;
			tmp195 = *((unsigned int*) (&tmp194[0]));
			
			__board.clear();
			for (unsigned int tmp196 = 0; tmp196 < tmp195; tmp196++)
			{
				std::vector<ECell> tmp197;
				offset++;
				unsigned char tmp198;
				tmp198 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp199 = std::string(&s[offset], tmp198);
				offset += tmp198;
				while (tmp199.size() < sizeof(unsigned int))
					tmp199 += '\x00';
				unsigned int tmp200;
				tmp200 = *((unsigned int*) (&tmp199[0]));
				
				tmp197.clear();
				for (unsigned int tmp201 = 0; tmp201 < tmp200; tmp201++)
				{
					ECell tmp202;
					offset++;
					char tmp203;
					tmp203 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp202 = (ECell) tmp203;
					tmp197.push_back(tmp202);
				}
				__board.push_back(tmp197);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp204;
			tmp204 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp205 = std::string(&s[offset], tmp204);
			offset += tmp204;
			while (tmp205.size() < sizeof(unsigned int))
				tmp205 += '\x00';
			unsigned int tmp206;
			tmp206 = *((unsigned int*) (&tmp205[0]));
			
			__scores.clear();
			for (unsigned int tmp207 = 0; tmp207 < tmp206; tmp207++)
			{
				std::string tmp208;
				offset++;
				unsigned char tmp210;
				tmp210 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp211 = std::string(&s[offset], tmp210);
				offset += tmp210;
				while (tmp211.size() < sizeof(unsigned int))
					tmp211 += '\x00';
				unsigned int tmp212;
				tmp212 = *((unsigned int*) (&tmp211[0]));
				
				tmp208 = s.substr(offset, tmp212);
				offset += tmp212;
				
				int tmp209;
				offset++;
				tmp209 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__scores[tmp208] = tmp209;
			}
		}
		
		// deserialize bombs
		__has_bombs = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombs)
		{
			unsigned char tmp213;
			tmp213 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp214 = std::string(&s[offset], tmp213);
			offset += tmp213;
			while (tmp214.size() < sizeof(unsigned int))
				tmp214 += '\x00';
			unsigned int tmp215;
			tmp215 = *((unsigned int*) (&tmp214[0]));
			
			__bombs.clear();
			for (unsigned int tmp216 = 0; tmp216 < tmp215; tmp216++)
			{
				Bomb tmp217;
				offset++;
				offset = tmp217.deserialize(s, offset);
				__bombs.push_back(tmp217);
			}
		}
		
		// deserialize terrorists
		__has_terrorists = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorists)
		{
			unsigned char tmp218;
			tmp218 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp219 = std::string(&s[offset], tmp218);
			offset += tmp218;
			while (tmp219.size() < sizeof(unsigned int))
				tmp219 += '\x00';
			unsigned int tmp220;
			tmp220 = *((unsigned int*) (&tmp219[0]));
			
			__terrorists.clear();
			for (unsigned int tmp221 = 0; tmp221 < tmp220; tmp221++)
			{
				Terrorist tmp222;
				offset++;
				offset = tmp222.deserialize(s, offset);
				__terrorists.push_back(tmp222);
			}
		}
		
		// deserialize polices
		__has_polices = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_polices)
		{
			unsigned char tmp223;
			tmp223 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp224 = std::string(&s[offset], tmp223);
			offset += tmp223;
			while (tmp224.size() < sizeof(unsigned int))
				tmp224 += '\x00';
			unsigned int tmp225;
			tmp225 = *((unsigned int*) (&tmp224[0]));
			
			__polices.clear();
			for (unsigned int tmp226 = 0; tmp226 < tmp225; tmp226++)
			{
				Police tmp227;
				offset++;
				offset = tmp227.deserialize(s, offset);
				__polices.push_back(tmp227);
			}
		}
		
		// deserialize constants
		__has_constants = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_constants)
		{
			offset = __constants.deserialize(s, offset);
		}
		
		return offset;
	}
};

} // namespace models

} // namespace ks

#endif // _KS_MODELS_H_
