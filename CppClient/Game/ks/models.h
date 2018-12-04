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
			int tmp70 = __explosion_remaining_time;
			auto tmp71 = reinterpret_cast<char*>(&tmp70);
			s += std::string(tmp71, sizeof(int));
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
	bool __is_dead;

	bool __has_id;
	bool __has_position;
	bool __has_planting_remaining_time;
	bool __has_footstep_sounds;
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
			int tmp73 = __id;
			auto tmp74 = reinterpret_cast<char*>(&tmp73);
			s += std::string(tmp74, sizeof(int));
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
			int tmp76 = __planting_remaining_time;
			auto tmp77 = reinterpret_cast<char*>(&tmp76);
			s += std::string(tmp77, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp78 = "";
			unsigned int tmp80 = __footstep_sounds.size();
			auto tmp81 = reinterpret_cast<char*>(&tmp80);
			tmp78 += std::string(tmp81, sizeof(unsigned int));
			while (tmp78.size() && tmp78.back() == 0)
				tmp78.pop_back();
			unsigned char tmp83 = tmp78.size();
			auto tmp84 = reinterpret_cast<char*>(&tmp83);
			s += std::string(tmp84, sizeof(unsigned char));
			s += tmp78;
			
			for (auto &tmp85 : __footstep_sounds)
			{
				s += '\x01';
				int tmp87 = tmp85;
				auto tmp88 = reinterpret_cast<char*>(&tmp87);
				s += std::string(tmp88, sizeof(int));
			}
		}
		
		// serialize is_dead
		s += __has_is_dead;
		if (__has_is_dead)
		{
			bool tmp90 = __is_dead;
			auto tmp91 = reinterpret_cast<char*>(&tmp90);
			s += std::string(tmp91, sizeof(bool));
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
			unsigned char tmp92;
			tmp92 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp93 = std::string(&s[offset], tmp92);
			offset += tmp92;
			while (tmp93.size() < sizeof(unsigned int))
				tmp93 += '\x00';
			unsigned int tmp94;
			tmp94 = *((unsigned int*) (&tmp93[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp95 = 0; tmp95 < tmp94; tmp95++)
			{
				int tmp96;
				offset++;
				tmp96 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp96);
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
			int tmp98 = __id;
			auto tmp99 = reinterpret_cast<char*>(&tmp98);
			s += std::string(tmp99, sizeof(int));
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
			int tmp101 = __defusion_remaining_time;
			auto tmp102 = reinterpret_cast<char*>(&tmp101);
			s += std::string(tmp102, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp103 = "";
			unsigned int tmp105 = __footstep_sounds.size();
			auto tmp106 = reinterpret_cast<char*>(&tmp105);
			tmp103 += std::string(tmp106, sizeof(unsigned int));
			while (tmp103.size() && tmp103.back() == 0)
				tmp103.pop_back();
			unsigned char tmp108 = tmp103.size();
			auto tmp109 = reinterpret_cast<char*>(&tmp108);
			s += std::string(tmp109, sizeof(unsigned char));
			s += tmp103;
			
			for (auto &tmp110 : __footstep_sounds)
			{
				s += '\x01';
				int tmp112 = tmp110;
				auto tmp113 = reinterpret_cast<char*>(&tmp112);
				s += std::string(tmp113, sizeof(int));
			}
		}
		
		// serialize bomb_sounds
		s += __has_bomb_sounds;
		if (__has_bomb_sounds)
		{
			std::string tmp114 = "";
			unsigned int tmp116 = __bomb_sounds.size();
			auto tmp117 = reinterpret_cast<char*>(&tmp116);
			tmp114 += std::string(tmp117, sizeof(unsigned int));
			while (tmp114.size() && tmp114.back() == 0)
				tmp114.pop_back();
			unsigned char tmp119 = tmp114.size();
			auto tmp120 = reinterpret_cast<char*>(&tmp119);
			s += std::string(tmp120, sizeof(unsigned char));
			s += tmp114;
			
			for (auto &tmp121 : __bomb_sounds)
			{
				s += '\x01';
				int tmp123 = tmp121;
				auto tmp124 = reinterpret_cast<char*>(&tmp123);
				s += std::string(tmp124, sizeof(int));
			}
		}
		
		// serialize is_visible
		s += __has_is_visible;
		if (__has_is_visible)
		{
			bool tmp126 = __is_visible;
			auto tmp127 = reinterpret_cast<char*>(&tmp126);
			s += std::string(tmp127, sizeof(bool));
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
			unsigned char tmp128;
			tmp128 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp129 = std::string(&s[offset], tmp128);
			offset += tmp128;
			while (tmp129.size() < sizeof(unsigned int))
				tmp129 += '\x00';
			unsigned int tmp130;
			tmp130 = *((unsigned int*) (&tmp129[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp131 = 0; tmp131 < tmp130; tmp131++)
			{
				int tmp132;
				offset++;
				tmp132 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp132);
			}
		}
		
		// deserialize bomb_sounds
		__has_bomb_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_sounds)
		{
			unsigned char tmp133;
			tmp133 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp134 = std::string(&s[offset], tmp133);
			offset += tmp133;
			while (tmp134.size() < sizeof(unsigned int))
				tmp134 += '\x00';
			unsigned int tmp135;
			tmp135 = *((unsigned int*) (&tmp134[0]));
			
			__bomb_sounds.clear();
			for (unsigned int tmp136 = 0; tmp136 < tmp135; tmp136++)
			{
				int tmp137;
				offset++;
				tmp137 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bomb_sounds.push_back(tmp137);
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
			int tmp139 = __width;
			auto tmp140 = reinterpret_cast<char*>(&tmp139);
			s += std::string(tmp140, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp142 = __height;
			auto tmp143 = reinterpret_cast<char*>(&tmp142);
			s += std::string(tmp143, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp144 = "";
			unsigned int tmp146 = __board.size();
			auto tmp147 = reinterpret_cast<char*>(&tmp146);
			tmp144 += std::string(tmp147, sizeof(unsigned int));
			while (tmp144.size() && tmp144.back() == 0)
				tmp144.pop_back();
			unsigned char tmp149 = tmp144.size();
			auto tmp150 = reinterpret_cast<char*>(&tmp149);
			s += std::string(tmp150, sizeof(unsigned char));
			s += tmp144;
			
			for (auto &tmp151 : __board)
			{
				s += '\x01';
				std::string tmp152 = "";
				unsigned int tmp154 = tmp151.size();
				auto tmp155 = reinterpret_cast<char*>(&tmp154);
				tmp152 += std::string(tmp155, sizeof(unsigned int));
				while (tmp152.size() && tmp152.back() == 0)
					tmp152.pop_back();
				unsigned char tmp157 = tmp152.size();
				auto tmp158 = reinterpret_cast<char*>(&tmp157);
				s += std::string(tmp158, sizeof(unsigned char));
				s += tmp152;
				
				for (auto &tmp159 : tmp151)
				{
					s += '\x01';
					char tmp161 = (char) tmp159;
					auto tmp162 = reinterpret_cast<char*>(&tmp161);
					s += std::string(tmp162, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp163 = "";
			unsigned int tmp165 = __scores.size();
			auto tmp166 = reinterpret_cast<char*>(&tmp165);
			tmp163 += std::string(tmp166, sizeof(unsigned int));
			while (tmp163.size() && tmp163.back() == 0)
				tmp163.pop_back();
			unsigned char tmp168 = tmp163.size();
			auto tmp169 = reinterpret_cast<char*>(&tmp168);
			s += std::string(tmp169, sizeof(unsigned char));
			s += tmp163;
			
			for (auto &tmp170 : __scores)
			{
				s += '\x01';
				std::string tmp171 = "";
				unsigned int tmp173 = tmp170.first.size();
				auto tmp174 = reinterpret_cast<char*>(&tmp173);
				tmp171 += std::string(tmp174, sizeof(unsigned int));
				while (tmp171.size() && tmp171.back() == 0)
					tmp171.pop_back();
				unsigned char tmp176 = tmp171.size();
				auto tmp177 = reinterpret_cast<char*>(&tmp176);
				s += std::string(tmp177, sizeof(unsigned char));
				s += tmp171;
				
				s += tmp170.first;
				
				s += '\x01';
				float tmp179 = tmp170.second;
				auto tmp180 = reinterpret_cast<char*>(&tmp179);
				s += std::string(tmp180, sizeof(float));
			}
		}
		
		// serialize bombs
		s += __has_bombs;
		if (__has_bombs)
		{
			std::string tmp181 = "";
			unsigned int tmp183 = __bombs.size();
			auto tmp184 = reinterpret_cast<char*>(&tmp183);
			tmp181 += std::string(tmp184, sizeof(unsigned int));
			while (tmp181.size() && tmp181.back() == 0)
				tmp181.pop_back();
			unsigned char tmp186 = tmp181.size();
			auto tmp187 = reinterpret_cast<char*>(&tmp186);
			s += std::string(tmp187, sizeof(unsigned char));
			s += tmp181;
			
			for (auto &tmp188 : __bombs)
			{
				s += '\x01';
				s += tmp188.serialize();
			}
		}
		
		// serialize terrorists
		s += __has_terrorists;
		if (__has_terrorists)
		{
			std::string tmp189 = "";
			unsigned int tmp191 = __terrorists.size();
			auto tmp192 = reinterpret_cast<char*>(&tmp191);
			tmp189 += std::string(tmp192, sizeof(unsigned int));
			while (tmp189.size() && tmp189.back() == 0)
				tmp189.pop_back();
			unsigned char tmp194 = tmp189.size();
			auto tmp195 = reinterpret_cast<char*>(&tmp194);
			s += std::string(tmp195, sizeof(unsigned char));
			s += tmp189;
			
			for (auto &tmp196 : __terrorists)
			{
				s += '\x01';
				s += tmp196.serialize();
			}
		}
		
		// serialize polices
		s += __has_polices;
		if (__has_polices)
		{
			std::string tmp197 = "";
			unsigned int tmp199 = __polices.size();
			auto tmp200 = reinterpret_cast<char*>(&tmp199);
			tmp197 += std::string(tmp200, sizeof(unsigned int));
			while (tmp197.size() && tmp197.back() == 0)
				tmp197.pop_back();
			unsigned char tmp202 = tmp197.size();
			auto tmp203 = reinterpret_cast<char*>(&tmp202);
			s += std::string(tmp203, sizeof(unsigned char));
			s += tmp197;
			
			for (auto &tmp204 : __polices)
			{
				s += '\x01';
				s += tmp204.serialize();
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
			unsigned char tmp205;
			tmp205 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp206 = std::string(&s[offset], tmp205);
			offset += tmp205;
			while (tmp206.size() < sizeof(unsigned int))
				tmp206 += '\x00';
			unsigned int tmp207;
			tmp207 = *((unsigned int*) (&tmp206[0]));
			
			__board.clear();
			for (unsigned int tmp208 = 0; tmp208 < tmp207; tmp208++)
			{
				std::vector<ECell> tmp209;
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
				
				tmp209.clear();
				for (unsigned int tmp213 = 0; tmp213 < tmp212; tmp213++)
				{
					ECell tmp214;
					offset++;
					char tmp215;
					tmp215 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp214 = (ECell) tmp215;
					tmp209.push_back(tmp214);
				}
				__board.push_back(tmp209);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp216;
			tmp216 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp217 = std::string(&s[offset], tmp216);
			offset += tmp216;
			while (tmp217.size() < sizeof(unsigned int))
				tmp217 += '\x00';
			unsigned int tmp218;
			tmp218 = *((unsigned int*) (&tmp217[0]));
			
			__scores.clear();
			for (unsigned int tmp219 = 0; tmp219 < tmp218; tmp219++)
			{
				std::string tmp220;
				offset++;
				unsigned char tmp222;
				tmp222 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp223 = std::string(&s[offset], tmp222);
				offset += tmp222;
				while (tmp223.size() < sizeof(unsigned int))
					tmp223 += '\x00';
				unsigned int tmp224;
				tmp224 = *((unsigned int*) (&tmp223[0]));
				
				tmp220 = s.substr(offset, tmp224);
				offset += tmp224;
				
				float tmp221;
				offset++;
				tmp221 = *((float*) (&s[offset]));
				offset += sizeof(float);
				
				__scores[tmp220] = tmp221;
			}
		}
		
		// deserialize bombs
		__has_bombs = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombs)
		{
			unsigned char tmp225;
			tmp225 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp226 = std::string(&s[offset], tmp225);
			offset += tmp225;
			while (tmp226.size() < sizeof(unsigned int))
				tmp226 += '\x00';
			unsigned int tmp227;
			tmp227 = *((unsigned int*) (&tmp226[0]));
			
			__bombs.clear();
			for (unsigned int tmp228 = 0; tmp228 < tmp227; tmp228++)
			{
				Bomb tmp229;
				offset++;
				offset = tmp229.deserialize(s, offset);
				__bombs.push_back(tmp229);
			}
		}
		
		// deserialize terrorists
		__has_terrorists = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorists)
		{
			unsigned char tmp230;
			tmp230 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp231 = std::string(&s[offset], tmp230);
			offset += tmp230;
			while (tmp231.size() < sizeof(unsigned int))
				tmp231 += '\x00';
			unsigned int tmp232;
			tmp232 = *((unsigned int*) (&tmp231[0]));
			
			__terrorists.clear();
			for (unsigned int tmp233 = 0; tmp233 < tmp232; tmp233++)
			{
				Terrorist tmp234;
				offset++;
				offset = tmp234.deserialize(s, offset);
				__terrorists.push_back(tmp234);
			}
		}
		
		// deserialize polices
		__has_polices = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_polices)
		{
			unsigned char tmp235;
			tmp235 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp236 = std::string(&s[offset], tmp235);
			offset += tmp235;
			while (tmp236.size() < sizeof(unsigned int))
				tmp236 += '\x00';
			unsigned int tmp237;
			tmp237 = *((unsigned int*) (&tmp236[0]));
			
			__polices.clear();
			for (unsigned int tmp238 = 0; tmp238 < tmp237; tmp238++)
			{
				Police tmp239;
				offset++;
				offset = tmp239.deserialize(s, offset);
				__polices.push_back(tmp239);
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
