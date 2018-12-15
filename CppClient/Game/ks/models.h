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
	float __score_coefficient_small_bomb_site;
	float __score_coefficient_medium_bomb_site;
	float __score_coefficient_large_bomb_site;
	float __score_coefficient_vast_bomb_site;
	int __terrorist_vision_distance;
	int __terrorist_death_score;
	int __police_vision_distance;
	std::map<ESoundIntensity, int> __sound_ranges;
	int __max_cycles;

	bool __has_bomb_planting_time;
	bool __has_bomb_defusion_time;
	bool __has_bomb_explosion_time;
	bool __has_bomb_planting_score;
	bool __has_bomb_defusion_score;
	bool __has_bomb_explosion_score;
	bool __has_score_coefficient_small_bomb_site;
	bool __has_score_coefficient_medium_bomb_site;
	bool __has_score_coefficient_large_bomb_site;
	bool __has_score_coefficient_vast_bomb_site;
	bool __has_terrorist_vision_distance;
	bool __has_terrorist_death_score;
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
	
	inline float score_coefficient_small_bomb_site() const
	{
		return __score_coefficient_small_bomb_site;
	}
	
	inline float score_coefficient_medium_bomb_site() const
	{
		return __score_coefficient_medium_bomb_site;
	}
	
	inline float score_coefficient_large_bomb_site() const
	{
		return __score_coefficient_large_bomb_site;
	}
	
	inline float score_coefficient_vast_bomb_site() const
	{
		return __score_coefficient_vast_bomb_site;
	}
	
	inline int terrorist_vision_distance() const
	{
		return __terrorist_vision_distance;
	}
	
	inline int terrorist_death_score() const
	{
		return __terrorist_death_score;
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
	
	inline float &ref_score_coefficient_small_bomb_site() const
	{
		return (float&) __score_coefficient_small_bomb_site;
	}
	
	inline float &ref_score_coefficient_medium_bomb_site() const
	{
		return (float&) __score_coefficient_medium_bomb_site;
	}
	
	inline float &ref_score_coefficient_large_bomb_site() const
	{
		return (float&) __score_coefficient_large_bomb_site;
	}
	
	inline float &ref_score_coefficient_vast_bomb_site() const
	{
		return (float&) __score_coefficient_vast_bomb_site;
	}
	
	inline int &ref_terrorist_vision_distance() const
	{
		return (int&) __terrorist_vision_distance;
	}
	
	inline int &ref_terrorist_death_score() const
	{
		return (int&) __terrorist_death_score;
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
	
	inline void score_coefficient_small_bomb_site(const float &score_coefficient_small_bomb_site)
	{
		__score_coefficient_small_bomb_site = score_coefficient_small_bomb_site;
		has_score_coefficient_small_bomb_site(true);
	}
	
	inline void score_coefficient_medium_bomb_site(const float &score_coefficient_medium_bomb_site)
	{
		__score_coefficient_medium_bomb_site = score_coefficient_medium_bomb_site;
		has_score_coefficient_medium_bomb_site(true);
	}
	
	inline void score_coefficient_large_bomb_site(const float &score_coefficient_large_bomb_site)
	{
		__score_coefficient_large_bomb_site = score_coefficient_large_bomb_site;
		has_score_coefficient_large_bomb_site(true);
	}
	
	inline void score_coefficient_vast_bomb_site(const float &score_coefficient_vast_bomb_site)
	{
		__score_coefficient_vast_bomb_site = score_coefficient_vast_bomb_site;
		has_score_coefficient_vast_bomb_site(true);
	}
	
	inline void terrorist_vision_distance(const int &terrorist_vision_distance)
	{
		__terrorist_vision_distance = terrorist_vision_distance;
		has_terrorist_vision_distance(true);
	}
	
	inline void terrorist_death_score(const int &terrorist_death_score)
	{
		__terrorist_death_score = terrorist_death_score;
		has_terrorist_death_score(true);
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
	
	inline bool has_score_coefficient_small_bomb_site() const
	{
		return __has_score_coefficient_small_bomb_site;
	}
	
	inline bool has_score_coefficient_medium_bomb_site() const
	{
		return __has_score_coefficient_medium_bomb_site;
	}
	
	inline bool has_score_coefficient_large_bomb_site() const
	{
		return __has_score_coefficient_large_bomb_site;
	}
	
	inline bool has_score_coefficient_vast_bomb_site() const
	{
		return __has_score_coefficient_vast_bomb_site;
	}
	
	inline bool has_terrorist_vision_distance() const
	{
		return __has_terrorist_vision_distance;
	}
	
	inline bool has_terrorist_death_score() const
	{
		return __has_terrorist_death_score;
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
	
	inline void has_score_coefficient_small_bomb_site(const bool &has_score_coefficient_small_bomb_site)
	{
		__has_score_coefficient_small_bomb_site = has_score_coefficient_small_bomb_site;
	}
	
	inline void has_score_coefficient_medium_bomb_site(const bool &has_score_coefficient_medium_bomb_site)
	{
		__has_score_coefficient_medium_bomb_site = has_score_coefficient_medium_bomb_site;
	}
	
	inline void has_score_coefficient_large_bomb_site(const bool &has_score_coefficient_large_bomb_site)
	{
		__has_score_coefficient_large_bomb_site = has_score_coefficient_large_bomb_site;
	}
	
	inline void has_score_coefficient_vast_bomb_site(const bool &has_score_coefficient_vast_bomb_site)
	{
		__has_score_coefficient_vast_bomb_site = has_score_coefficient_vast_bomb_site;
	}
	
	inline void has_terrorist_vision_distance(const bool &has_terrorist_vision_distance)
	{
		__has_terrorist_vision_distance = has_terrorist_vision_distance;
	}
	
	inline void has_terrorist_death_score(const bool &has_terrorist_death_score)
	{
		__has_terrorist_death_score = has_terrorist_death_score;
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
		has_score_coefficient_small_bomb_site(false);
		has_score_coefficient_medium_bomb_site(false);
		has_score_coefficient_large_bomb_site(false);
		has_score_coefficient_vast_bomb_site(false);
		has_terrorist_vision_distance(false);
		has_terrorist_death_score(false);
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
		
		// serialize score_coefficient_small_bomb_site
		s += __has_score_coefficient_small_bomb_site;
		if (__has_score_coefficient_small_bomb_site)
		{
			float tmp19 = __score_coefficient_small_bomb_site;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(float));
		}
		
		// serialize score_coefficient_medium_bomb_site
		s += __has_score_coefficient_medium_bomb_site;
		if (__has_score_coefficient_medium_bomb_site)
		{
			float tmp22 = __score_coefficient_medium_bomb_site;
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			s += std::string(tmp23, sizeof(float));
		}
		
		// serialize score_coefficient_large_bomb_site
		s += __has_score_coefficient_large_bomb_site;
		if (__has_score_coefficient_large_bomb_site)
		{
			float tmp25 = __score_coefficient_large_bomb_site;
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(float));
		}
		
		// serialize score_coefficient_vast_bomb_site
		s += __has_score_coefficient_vast_bomb_site;
		if (__has_score_coefficient_vast_bomb_site)
		{
			float tmp28 = __score_coefficient_vast_bomb_site;
			auto tmp29 = reinterpret_cast<char*>(&tmp28);
			s += std::string(tmp29, sizeof(float));
		}
		
		// serialize terrorist_vision_distance
		s += __has_terrorist_vision_distance;
		if (__has_terrorist_vision_distance)
		{
			int tmp31 = __terrorist_vision_distance;
			auto tmp32 = reinterpret_cast<char*>(&tmp31);
			s += std::string(tmp32, sizeof(int));
		}
		
		// serialize terrorist_death_score
		s += __has_terrorist_death_score;
		if (__has_terrorist_death_score)
		{
			int tmp34 = __terrorist_death_score;
			auto tmp35 = reinterpret_cast<char*>(&tmp34);
			s += std::string(tmp35, sizeof(int));
		}
		
		// serialize police_vision_distance
		s += __has_police_vision_distance;
		if (__has_police_vision_distance)
		{
			int tmp37 = __police_vision_distance;
			auto tmp38 = reinterpret_cast<char*>(&tmp37);
			s += std::string(tmp38, sizeof(int));
		}
		
		// serialize sound_ranges
		s += __has_sound_ranges;
		if (__has_sound_ranges)
		{
			std::string tmp39 = "";
			unsigned int tmp41 = __sound_ranges.size();
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			tmp39 += std::string(tmp42, sizeof(unsigned int));
			while (tmp39.size() && tmp39.back() == 0)
				tmp39.pop_back();
			unsigned char tmp44 = tmp39.size();
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(unsigned char));
			s += tmp39;
			
			for (auto &tmp46 : __sound_ranges)
			{
				s += '\x01';
				char tmp48 = (char) tmp46.first;
				auto tmp49 = reinterpret_cast<char*>(&tmp48);
				s += std::string(tmp49, sizeof(char));
				
				s += '\x01';
				int tmp51 = tmp46.second;
				auto tmp52 = reinterpret_cast<char*>(&tmp51);
				s += std::string(tmp52, sizeof(int));
			}
		}
		
		// serialize max_cycles
		s += __has_max_cycles;
		if (__has_max_cycles)
		{
			int tmp54 = __max_cycles;
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(int));
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
		
		// deserialize score_coefficient_small_bomb_site
		__has_score_coefficient_small_bomb_site = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_score_coefficient_small_bomb_site)
		{
			__score_coefficient_small_bomb_site = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize score_coefficient_medium_bomb_site
		__has_score_coefficient_medium_bomb_site = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_score_coefficient_medium_bomb_site)
		{
			__score_coefficient_medium_bomb_site = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize score_coefficient_large_bomb_site
		__has_score_coefficient_large_bomb_site = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_score_coefficient_large_bomb_site)
		{
			__score_coefficient_large_bomb_site = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize score_coefficient_vast_bomb_site
		__has_score_coefficient_vast_bomb_site = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_score_coefficient_vast_bomb_site)
		{
			__score_coefficient_vast_bomb_site = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize terrorist_vision_distance
		__has_terrorist_vision_distance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorist_vision_distance)
		{
			__terrorist_vision_distance = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize terrorist_death_score
		__has_terrorist_death_score = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorist_death_score)
		{
			__terrorist_death_score = *((int*) (&s[offset]));
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
			unsigned char tmp56;
			tmp56 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp57 = std::string(&s[offset], tmp56);
			offset += tmp56;
			while (tmp57.size() < sizeof(unsigned int))
				tmp57 += '\x00';
			unsigned int tmp58;
			tmp58 = *((unsigned int*) (&tmp57[0]));
			
			__sound_ranges.clear();
			for (unsigned int tmp59 = 0; tmp59 < tmp58; tmp59++)
			{
				ESoundIntensity tmp60;
				offset++;
				char tmp62;
				tmp62 = *((char*) (&s[offset]));
				offset += sizeof(char);
				tmp60 = (ESoundIntensity) tmp62;
				
				int tmp61;
				offset++;
				tmp61 = *((int*) (&s[offset]));
				offset += sizeof(int);
				
				__sound_ranges[tmp60] = tmp61;
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
			int tmp64 = __x;
			auto tmp65 = reinterpret_cast<char*>(&tmp64);
			s += std::string(tmp65, sizeof(int));
		}
		
		// serialize y
		s += __has_y;
		if (__has_y)
		{
			int tmp67 = __y;
			auto tmp68 = reinterpret_cast<char*>(&tmp67);
			s += std::string(tmp68, sizeof(int));
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
	int __planter_id;
	int __defuser_id;

	bool __has_position;
	bool __has_explosion_remaining_time;
	bool __has_planter_id;
	bool __has_defuser_id;


public: // getters

	inline Position position() const
	{
		return __position;
	}
	
	inline int explosion_remaining_time() const
	{
		return __explosion_remaining_time;
	}
	
	inline int planter_id() const
	{
		return __planter_id;
	}
	
	inline int defuser_id() const
	{
		return __defuser_id;
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
	
	inline int &ref_planter_id() const
	{
		return (int&) __planter_id;
	}
	
	inline int &ref_defuser_id() const
	{
		return (int&) __defuser_id;
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
	
	inline void planter_id(const int &planter_id)
	{
		__planter_id = planter_id;
		has_planter_id(true);
	}
	
	inline void defuser_id(const int &defuser_id)
	{
		__defuser_id = defuser_id;
		has_defuser_id(true);
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
	
	inline bool has_planter_id() const
	{
		return __has_planter_id;
	}
	
	inline bool has_defuser_id() const
	{
		return __has_defuser_id;
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
	
	inline void has_planter_id(const bool &has_planter_id)
	{
		__has_planter_id = has_planter_id;
	}
	
	inline void has_defuser_id(const bool &has_defuser_id)
	{
		__has_defuser_id = has_defuser_id;
	}
	

public:

	Bomb()
	{
		has_position(false);
		has_explosion_remaining_time(false);
		has_planter_id(false);
		has_defuser_id(false);
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
			int tmp70 = __explosion_remaining_time;
			auto tmp71 = reinterpret_cast<char*>(&tmp70);
			s += std::string(tmp71, sizeof(int));
		}
		
		// serialize planter_id
		s += __has_planter_id;
		if (__has_planter_id)
		{
			int tmp73 = __planter_id;
			auto tmp74 = reinterpret_cast<char*>(&tmp73);
			s += std::string(tmp74, sizeof(int));
		}
		
		// serialize defuser_id
		s += __has_defuser_id;
		if (__has_defuser_id)
		{
			int tmp76 = __defuser_id;
			auto tmp77 = reinterpret_cast<char*>(&tmp76);
			s += std::string(tmp77, sizeof(int));
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
		
		// deserialize planter_id
		__has_planter_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_planter_id)
		{
			__planter_id = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize defuser_id
		__has_defuser_id = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_defuser_id)
		{
			__defuser_id = *((int*) (&s[offset]));
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
	std::vector<Position> __vision;
	bool __is_dead;

	bool __has_id;
	bool __has_position;
	bool __has_planting_remaining_time;
	bool __has_footstep_sounds;
	bool __has_vision;
	bool __has_is_dead;


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
	
	inline std::vector<Position> vision() const
	{
		return __vision;
	}
	
	inline bool is_dead() const
	{
		return __is_dead;
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
	
	inline std::vector<Position> &ref_vision() const
	{
		return (std::vector<Position>&) __vision;
	}
	
	inline bool &ref_is_dead() const
	{
		return (bool&) __is_dead;
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
	
	inline void vision(const std::vector<Position> &vision)
	{
		__vision = vision;
		has_vision(true);
	}
	
	inline void is_dead(const bool &is_dead)
	{
		__is_dead = is_dead;
		has_is_dead(true);
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
	
	inline bool has_vision() const
	{
		return __has_vision;
	}
	
	inline bool has_is_dead() const
	{
		return __has_is_dead;
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
	
	inline void has_vision(const bool &has_vision)
	{
		__has_vision = has_vision;
	}
	
	inline void has_is_dead(const bool &has_is_dead)
	{
		__has_is_dead = has_is_dead;
	}
	

public:

	Terrorist()
	{
		has_id(false);
		has_position(false);
		has_planting_remaining_time(false);
		has_footstep_sounds(false);
		has_vision(false);
		has_is_dead(false);
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
			int tmp79 = __id;
			auto tmp80 = reinterpret_cast<char*>(&tmp79);
			s += std::string(tmp80, sizeof(int));
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
			int tmp82 = __planting_remaining_time;
			auto tmp83 = reinterpret_cast<char*>(&tmp82);
			s += std::string(tmp83, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp84 = "";
			unsigned int tmp86 = __footstep_sounds.size();
			auto tmp87 = reinterpret_cast<char*>(&tmp86);
			tmp84 += std::string(tmp87, sizeof(unsigned int));
			while (tmp84.size() && tmp84.back() == 0)
				tmp84.pop_back();
			unsigned char tmp89 = tmp84.size();
			auto tmp90 = reinterpret_cast<char*>(&tmp89);
			s += std::string(tmp90, sizeof(unsigned char));
			s += tmp84;
			
			for (auto &tmp91 : __footstep_sounds)
			{
				s += '\x01';
				int tmp93 = tmp91;
				auto tmp94 = reinterpret_cast<char*>(&tmp93);
				s += std::string(tmp94, sizeof(int));
			}
		}
		
		// serialize vision
		s += __has_vision;
		if (__has_vision)
		{
			std::string tmp95 = "";
			unsigned int tmp97 = __vision.size();
			auto tmp98 = reinterpret_cast<char*>(&tmp97);
			tmp95 += std::string(tmp98, sizeof(unsigned int));
			while (tmp95.size() && tmp95.back() == 0)
				tmp95.pop_back();
			unsigned char tmp100 = tmp95.size();
			auto tmp101 = reinterpret_cast<char*>(&tmp100);
			s += std::string(tmp101, sizeof(unsigned char));
			s += tmp95;
			
			for (auto &tmp102 : __vision)
			{
				s += '\x01';
				s += tmp102.serialize();
			}
		}
		
		// serialize is_dead
		s += __has_is_dead;
		if (__has_is_dead)
		{
			bool tmp104 = __is_dead;
			auto tmp105 = reinterpret_cast<char*>(&tmp104);
			s += std::string(tmp105, sizeof(bool));
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
			unsigned char tmp106;
			tmp106 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp107 = std::string(&s[offset], tmp106);
			offset += tmp106;
			while (tmp107.size() < sizeof(unsigned int))
				tmp107 += '\x00';
			unsigned int tmp108;
			tmp108 = *((unsigned int*) (&tmp107[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp109 = 0; tmp109 < tmp108; tmp109++)
			{
				int tmp110;
				offset++;
				tmp110 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp110);
			}
		}
		
		// deserialize vision
		__has_vision = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_vision)
		{
			unsigned char tmp111;
			tmp111 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp112 = std::string(&s[offset], tmp111);
			offset += tmp111;
			while (tmp112.size() < sizeof(unsigned int))
				tmp112 += '\x00';
			unsigned int tmp113;
			tmp113 = *((unsigned int*) (&tmp112[0]));
			
			__vision.clear();
			for (unsigned int tmp114 = 0; tmp114 < tmp113; tmp114++)
			{
				Position tmp115;
				offset++;
				offset = tmp115.deserialize(s, offset);
				__vision.push_back(tmp115);
			}
		}
		
		// deserialize is_dead
		__has_is_dead = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_is_dead)
		{
			__is_dead = *((bool*) (&s[offset]));
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
	std::vector<Position> __vision;
	std::vector<int> __bomb_sounds;
	bool __is_visible;

	bool __has_id;
	bool __has_position;
	bool __has_defusion_remaining_time;
	bool __has_footstep_sounds;
	bool __has_vision;
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
	
	inline std::vector<Position> vision() const
	{
		return __vision;
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
	
	inline std::vector<Position> &ref_vision() const
	{
		return (std::vector<Position>&) __vision;
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
	
	inline void vision(const std::vector<Position> &vision)
	{
		__vision = vision;
		has_vision(true);
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
	
	inline bool has_vision() const
	{
		return __has_vision;
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
	
	inline void has_vision(const bool &has_vision)
	{
		__has_vision = has_vision;
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
		has_vision(false);
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
			int tmp117 = __id;
			auto tmp118 = reinterpret_cast<char*>(&tmp117);
			s += std::string(tmp118, sizeof(int));
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
			int tmp120 = __defusion_remaining_time;
			auto tmp121 = reinterpret_cast<char*>(&tmp120);
			s += std::string(tmp121, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp122 = "";
			unsigned int tmp124 = __footstep_sounds.size();
			auto tmp125 = reinterpret_cast<char*>(&tmp124);
			tmp122 += std::string(tmp125, sizeof(unsigned int));
			while (tmp122.size() && tmp122.back() == 0)
				tmp122.pop_back();
			unsigned char tmp127 = tmp122.size();
			auto tmp128 = reinterpret_cast<char*>(&tmp127);
			s += std::string(tmp128, sizeof(unsigned char));
			s += tmp122;
			
			for (auto &tmp129 : __footstep_sounds)
			{
				s += '\x01';
				int tmp131 = tmp129;
				auto tmp132 = reinterpret_cast<char*>(&tmp131);
				s += std::string(tmp132, sizeof(int));
			}
		}
		
		// serialize vision
		s += __has_vision;
		if (__has_vision)
		{
			std::string tmp133 = "";
			unsigned int tmp135 = __vision.size();
			auto tmp136 = reinterpret_cast<char*>(&tmp135);
			tmp133 += std::string(tmp136, sizeof(unsigned int));
			while (tmp133.size() && tmp133.back() == 0)
				tmp133.pop_back();
			unsigned char tmp138 = tmp133.size();
			auto tmp139 = reinterpret_cast<char*>(&tmp138);
			s += std::string(tmp139, sizeof(unsigned char));
			s += tmp133;
			
			for (auto &tmp140 : __vision)
			{
				s += '\x01';
				s += tmp140.serialize();
			}
		}
		
		// serialize bomb_sounds
		s += __has_bomb_sounds;
		if (__has_bomb_sounds)
		{
			std::string tmp141 = "";
			unsigned int tmp143 = __bomb_sounds.size();
			auto tmp144 = reinterpret_cast<char*>(&tmp143);
			tmp141 += std::string(tmp144, sizeof(unsigned int));
			while (tmp141.size() && tmp141.back() == 0)
				tmp141.pop_back();
			unsigned char tmp146 = tmp141.size();
			auto tmp147 = reinterpret_cast<char*>(&tmp146);
			s += std::string(tmp147, sizeof(unsigned char));
			s += tmp141;
			
			for (auto &tmp148 : __bomb_sounds)
			{
				s += '\x01';
				int tmp150 = tmp148;
				auto tmp151 = reinterpret_cast<char*>(&tmp150);
				s += std::string(tmp151, sizeof(int));
			}
		}
		
		// serialize is_visible
		s += __has_is_visible;
		if (__has_is_visible)
		{
			bool tmp153 = __is_visible;
			auto tmp154 = reinterpret_cast<char*>(&tmp153);
			s += std::string(tmp154, sizeof(bool));
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
			unsigned char tmp155;
			tmp155 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp156 = std::string(&s[offset], tmp155);
			offset += tmp155;
			while (tmp156.size() < sizeof(unsigned int))
				tmp156 += '\x00';
			unsigned int tmp157;
			tmp157 = *((unsigned int*) (&tmp156[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp158 = 0; tmp158 < tmp157; tmp158++)
			{
				int tmp159;
				offset++;
				tmp159 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp159);
			}
		}
		
		// deserialize vision
		__has_vision = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_vision)
		{
			unsigned char tmp160;
			tmp160 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp161 = std::string(&s[offset], tmp160);
			offset += tmp160;
			while (tmp161.size() < sizeof(unsigned int))
				tmp161 += '\x00';
			unsigned int tmp162;
			tmp162 = *((unsigned int*) (&tmp161[0]));
			
			__vision.clear();
			for (unsigned int tmp163 = 0; tmp163 < tmp162; tmp163++)
			{
				Position tmp164;
				offset++;
				offset = tmp164.deserialize(s, offset);
				__vision.push_back(tmp164);
			}
		}
		
		// deserialize bomb_sounds
		__has_bomb_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_sounds)
		{
			unsigned char tmp165;
			tmp165 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp166 = std::string(&s[offset], tmp165);
			offset += tmp165;
			while (tmp166.size() < sizeof(unsigned int))
				tmp166 += '\x00';
			unsigned int tmp167;
			tmp167 = *((unsigned int*) (&tmp166[0]));
			
			__bomb_sounds.clear();
			for (unsigned int tmp168 = 0; tmp168 < tmp167; tmp168++)
			{
				int tmp169;
				offset++;
				tmp169 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bomb_sounds.push_back(tmp169);
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
	std::map<std::string, float> __scores;
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
	
	inline std::map<std::string, float> scores() const
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
	
	inline std::map<std::string, float> &ref_scores() const
	{
		return (std::map<std::string, float>&) __scores;
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
	
	inline void scores(const std::map<std::string, float> &scores)
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
			int tmp171 = __width;
			auto tmp172 = reinterpret_cast<char*>(&tmp171);
			s += std::string(tmp172, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp174 = __height;
			auto tmp175 = reinterpret_cast<char*>(&tmp174);
			s += std::string(tmp175, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp176 = "";
			unsigned int tmp178 = __board.size();
			auto tmp179 = reinterpret_cast<char*>(&tmp178);
			tmp176 += std::string(tmp179, sizeof(unsigned int));
			while (tmp176.size() && tmp176.back() == 0)
				tmp176.pop_back();
			unsigned char tmp181 = tmp176.size();
			auto tmp182 = reinterpret_cast<char*>(&tmp181);
			s += std::string(tmp182, sizeof(unsigned char));
			s += tmp176;
			
			for (auto &tmp183 : __board)
			{
				s += '\x01';
				std::string tmp184 = "";
				unsigned int tmp186 = tmp183.size();
				auto tmp187 = reinterpret_cast<char*>(&tmp186);
				tmp184 += std::string(tmp187, sizeof(unsigned int));
				while (tmp184.size() && tmp184.back() == 0)
					tmp184.pop_back();
				unsigned char tmp189 = tmp184.size();
				auto tmp190 = reinterpret_cast<char*>(&tmp189);
				s += std::string(tmp190, sizeof(unsigned char));
				s += tmp184;
				
				for (auto &tmp191 : tmp183)
				{
					s += '\x01';
					char tmp193 = (char) tmp191;
					auto tmp194 = reinterpret_cast<char*>(&tmp193);
					s += std::string(tmp194, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp195 = "";
			unsigned int tmp197 = __scores.size();
			auto tmp198 = reinterpret_cast<char*>(&tmp197);
			tmp195 += std::string(tmp198, sizeof(unsigned int));
			while (tmp195.size() && tmp195.back() == 0)
				tmp195.pop_back();
			unsigned char tmp200 = tmp195.size();
			auto tmp201 = reinterpret_cast<char*>(&tmp200);
			s += std::string(tmp201, sizeof(unsigned char));
			s += tmp195;
			
			for (auto &tmp202 : __scores)
			{
				s += '\x01';
				std::string tmp203 = "";
				unsigned int tmp205 = tmp202.first.size();
				auto tmp206 = reinterpret_cast<char*>(&tmp205);
				tmp203 += std::string(tmp206, sizeof(unsigned int));
				while (tmp203.size() && tmp203.back() == 0)
					tmp203.pop_back();
				unsigned char tmp208 = tmp203.size();
				auto tmp209 = reinterpret_cast<char*>(&tmp208);
				s += std::string(tmp209, sizeof(unsigned char));
				s += tmp203;
				
				s += tmp202.first;
				
				s += '\x01';
				float tmp211 = tmp202.second;
				auto tmp212 = reinterpret_cast<char*>(&tmp211);
				s += std::string(tmp212, sizeof(float));
			}
		}
		
		// serialize bombs
		s += __has_bombs;
		if (__has_bombs)
		{
			std::string tmp213 = "";
			unsigned int tmp215 = __bombs.size();
			auto tmp216 = reinterpret_cast<char*>(&tmp215);
			tmp213 += std::string(tmp216, sizeof(unsigned int));
			while (tmp213.size() && tmp213.back() == 0)
				tmp213.pop_back();
			unsigned char tmp218 = tmp213.size();
			auto tmp219 = reinterpret_cast<char*>(&tmp218);
			s += std::string(tmp219, sizeof(unsigned char));
			s += tmp213;
			
			for (auto &tmp220 : __bombs)
			{
				s += '\x01';
				s += tmp220.serialize();
			}
		}
		
		// serialize terrorists
		s += __has_terrorists;
		if (__has_terrorists)
		{
			std::string tmp221 = "";
			unsigned int tmp223 = __terrorists.size();
			auto tmp224 = reinterpret_cast<char*>(&tmp223);
			tmp221 += std::string(tmp224, sizeof(unsigned int));
			while (tmp221.size() && tmp221.back() == 0)
				tmp221.pop_back();
			unsigned char tmp226 = tmp221.size();
			auto tmp227 = reinterpret_cast<char*>(&tmp226);
			s += std::string(tmp227, sizeof(unsigned char));
			s += tmp221;
			
			for (auto &tmp228 : __terrorists)
			{
				s += '\x01';
				s += tmp228.serialize();
			}
		}
		
		// serialize polices
		s += __has_polices;
		if (__has_polices)
		{
			std::string tmp229 = "";
			unsigned int tmp231 = __polices.size();
			auto tmp232 = reinterpret_cast<char*>(&tmp231);
			tmp229 += std::string(tmp232, sizeof(unsigned int));
			while (tmp229.size() && tmp229.back() == 0)
				tmp229.pop_back();
			unsigned char tmp234 = tmp229.size();
			auto tmp235 = reinterpret_cast<char*>(&tmp234);
			s += std::string(tmp235, sizeof(unsigned char));
			s += tmp229;
			
			for (auto &tmp236 : __polices)
			{
				s += '\x01';
				s += tmp236.serialize();
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
			unsigned char tmp237;
			tmp237 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp238 = std::string(&s[offset], tmp237);
			offset += tmp237;
			while (tmp238.size() < sizeof(unsigned int))
				tmp238 += '\x00';
			unsigned int tmp239;
			tmp239 = *((unsigned int*) (&tmp238[0]));
			
			__board.clear();
			for (unsigned int tmp240 = 0; tmp240 < tmp239; tmp240++)
			{
				std::vector<ECell> tmp241;
				offset++;
				unsigned char tmp242;
				tmp242 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp243 = std::string(&s[offset], tmp242);
				offset += tmp242;
				while (tmp243.size() < sizeof(unsigned int))
					tmp243 += '\x00';
				unsigned int tmp244;
				tmp244 = *((unsigned int*) (&tmp243[0]));
				
				tmp241.clear();
				for (unsigned int tmp245 = 0; tmp245 < tmp244; tmp245++)
				{
					ECell tmp246;
					offset++;
					char tmp247;
					tmp247 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp246 = (ECell) tmp247;
					tmp241.push_back(tmp246);
				}
				__board.push_back(tmp241);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp248;
			tmp248 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp249 = std::string(&s[offset], tmp248);
			offset += tmp248;
			while (tmp249.size() < sizeof(unsigned int))
				tmp249 += '\x00';
			unsigned int tmp250;
			tmp250 = *((unsigned int*) (&tmp249[0]));
			
			__scores.clear();
			for (unsigned int tmp251 = 0; tmp251 < tmp250; tmp251++)
			{
				std::string tmp252;
				offset++;
				unsigned char tmp254;
				tmp254 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp255 = std::string(&s[offset], tmp254);
				offset += tmp254;
				while (tmp255.size() < sizeof(unsigned int))
					tmp255 += '\x00';
				unsigned int tmp256;
				tmp256 = *((unsigned int*) (&tmp255[0]));
				
				tmp252 = s.substr(offset, tmp256);
				offset += tmp256;
				
				float tmp253;
				offset++;
				tmp253 = *((float*) (&s[offset]));
				offset += sizeof(float);
				
				__scores[tmp252] = tmp253;
			}
		}
		
		// deserialize bombs
		__has_bombs = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombs)
		{
			unsigned char tmp257;
			tmp257 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp258 = std::string(&s[offset], tmp257);
			offset += tmp257;
			while (tmp258.size() < sizeof(unsigned int))
				tmp258 += '\x00';
			unsigned int tmp259;
			tmp259 = *((unsigned int*) (&tmp258[0]));
			
			__bombs.clear();
			for (unsigned int tmp260 = 0; tmp260 < tmp259; tmp260++)
			{
				Bomb tmp261;
				offset++;
				offset = tmp261.deserialize(s, offset);
				__bombs.push_back(tmp261);
			}
		}
		
		// deserialize terrorists
		__has_terrorists = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorists)
		{
			unsigned char tmp262;
			tmp262 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp263 = std::string(&s[offset], tmp262);
			offset += tmp262;
			while (tmp263.size() < sizeof(unsigned int))
				tmp263 += '\x00';
			unsigned int tmp264;
			tmp264 = *((unsigned int*) (&tmp263[0]));
			
			__terrorists.clear();
			for (unsigned int tmp265 = 0; tmp265 < tmp264; tmp265++)
			{
				Terrorist tmp266;
				offset++;
				offset = tmp266.deserialize(s, offset);
				__terrorists.push_back(tmp266);
			}
		}
		
		// deserialize polices
		__has_polices = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_polices)
		{
			unsigned char tmp267;
			tmp267 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp268 = std::string(&s[offset], tmp267);
			offset += tmp267;
			while (tmp268.size() < sizeof(unsigned int))
				tmp268 += '\x00';
			unsigned int tmp269;
			tmp269 = *((unsigned int*) (&tmp268[0]));
			
			__polices.clear();
			for (unsigned int tmp270 = 0; tmp270 < tmp269; tmp270++)
			{
				Police tmp271;
				offset++;
				offset = tmp271.deserialize(s, offset);
				__polices.push_back(tmp271);
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
