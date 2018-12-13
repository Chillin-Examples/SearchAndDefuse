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
		
		// serialize is_dead
		s += __has_is_dead;
		if (__has_is_dead)
		{
			bool tmp96 = __is_dead;
			auto tmp97 = reinterpret_cast<char*>(&tmp96);
			s += std::string(tmp97, sizeof(bool));
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
			unsigned char tmp98;
			tmp98 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp99 = std::string(&s[offset], tmp98);
			offset += tmp98;
			while (tmp99.size() < sizeof(unsigned int))
				tmp99 += '\x00';
			unsigned int tmp100;
			tmp100 = *((unsigned int*) (&tmp99[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp101 = 0; tmp101 < tmp100; tmp101++)
			{
				int tmp102;
				offset++;
				tmp102 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp102);
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
			int tmp104 = __id;
			auto tmp105 = reinterpret_cast<char*>(&tmp104);
			s += std::string(tmp105, sizeof(int));
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
			int tmp107 = __defusion_remaining_time;
			auto tmp108 = reinterpret_cast<char*>(&tmp107);
			s += std::string(tmp108, sizeof(int));
		}
		
		// serialize footstep_sounds
		s += __has_footstep_sounds;
		if (__has_footstep_sounds)
		{
			std::string tmp109 = "";
			unsigned int tmp111 = __footstep_sounds.size();
			auto tmp112 = reinterpret_cast<char*>(&tmp111);
			tmp109 += std::string(tmp112, sizeof(unsigned int));
			while (tmp109.size() && tmp109.back() == 0)
				tmp109.pop_back();
			unsigned char tmp114 = tmp109.size();
			auto tmp115 = reinterpret_cast<char*>(&tmp114);
			s += std::string(tmp115, sizeof(unsigned char));
			s += tmp109;
			
			for (auto &tmp116 : __footstep_sounds)
			{
				s += '\x01';
				int tmp118 = tmp116;
				auto tmp119 = reinterpret_cast<char*>(&tmp118);
				s += std::string(tmp119, sizeof(int));
			}
		}
		
		// serialize bomb_sounds
		s += __has_bomb_sounds;
		if (__has_bomb_sounds)
		{
			std::string tmp120 = "";
			unsigned int tmp122 = __bomb_sounds.size();
			auto tmp123 = reinterpret_cast<char*>(&tmp122);
			tmp120 += std::string(tmp123, sizeof(unsigned int));
			while (tmp120.size() && tmp120.back() == 0)
				tmp120.pop_back();
			unsigned char tmp125 = tmp120.size();
			auto tmp126 = reinterpret_cast<char*>(&tmp125);
			s += std::string(tmp126, sizeof(unsigned char));
			s += tmp120;
			
			for (auto &tmp127 : __bomb_sounds)
			{
				s += '\x01';
				int tmp129 = tmp127;
				auto tmp130 = reinterpret_cast<char*>(&tmp129);
				s += std::string(tmp130, sizeof(int));
			}
		}
		
		// serialize is_visible
		s += __has_is_visible;
		if (__has_is_visible)
		{
			bool tmp132 = __is_visible;
			auto tmp133 = reinterpret_cast<char*>(&tmp132);
			s += std::string(tmp133, sizeof(bool));
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
			unsigned char tmp134;
			tmp134 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp135 = std::string(&s[offset], tmp134);
			offset += tmp134;
			while (tmp135.size() < sizeof(unsigned int))
				tmp135 += '\x00';
			unsigned int tmp136;
			tmp136 = *((unsigned int*) (&tmp135[0]));
			
			__footstep_sounds.clear();
			for (unsigned int tmp137 = 0; tmp137 < tmp136; tmp137++)
			{
				int tmp138;
				offset++;
				tmp138 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstep_sounds.push_back(tmp138);
			}
		}
		
		// deserialize bomb_sounds
		__has_bomb_sounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bomb_sounds)
		{
			unsigned char tmp139;
			tmp139 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp140 = std::string(&s[offset], tmp139);
			offset += tmp139;
			while (tmp140.size() < sizeof(unsigned int))
				tmp140 += '\x00';
			unsigned int tmp141;
			tmp141 = *((unsigned int*) (&tmp140[0]));
			
			__bomb_sounds.clear();
			for (unsigned int tmp142 = 0; tmp142 < tmp141; tmp142++)
			{
				int tmp143;
				offset++;
				tmp143 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bomb_sounds.push_back(tmp143);
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
			int tmp145 = __width;
			auto tmp146 = reinterpret_cast<char*>(&tmp145);
			s += std::string(tmp146, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp148 = __height;
			auto tmp149 = reinterpret_cast<char*>(&tmp148);
			s += std::string(tmp149, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp150 = "";
			unsigned int tmp152 = __board.size();
			auto tmp153 = reinterpret_cast<char*>(&tmp152);
			tmp150 += std::string(tmp153, sizeof(unsigned int));
			while (tmp150.size() && tmp150.back() == 0)
				tmp150.pop_back();
			unsigned char tmp155 = tmp150.size();
			auto tmp156 = reinterpret_cast<char*>(&tmp155);
			s += std::string(tmp156, sizeof(unsigned char));
			s += tmp150;
			
			for (auto &tmp157 : __board)
			{
				s += '\x01';
				std::string tmp158 = "";
				unsigned int tmp160 = tmp157.size();
				auto tmp161 = reinterpret_cast<char*>(&tmp160);
				tmp158 += std::string(tmp161, sizeof(unsigned int));
				while (tmp158.size() && tmp158.back() == 0)
					tmp158.pop_back();
				unsigned char tmp163 = tmp158.size();
				auto tmp164 = reinterpret_cast<char*>(&tmp163);
				s += std::string(tmp164, sizeof(unsigned char));
				s += tmp158;
				
				for (auto &tmp165 : tmp157)
				{
					s += '\x01';
					char tmp167 = (char) tmp165;
					auto tmp168 = reinterpret_cast<char*>(&tmp167);
					s += std::string(tmp168, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp169 = "";
			unsigned int tmp171 = __scores.size();
			auto tmp172 = reinterpret_cast<char*>(&tmp171);
			tmp169 += std::string(tmp172, sizeof(unsigned int));
			while (tmp169.size() && tmp169.back() == 0)
				tmp169.pop_back();
			unsigned char tmp174 = tmp169.size();
			auto tmp175 = reinterpret_cast<char*>(&tmp174);
			s += std::string(tmp175, sizeof(unsigned char));
			s += tmp169;
			
			for (auto &tmp176 : __scores)
			{
				s += '\x01';
				std::string tmp177 = "";
				unsigned int tmp179 = tmp176.first.size();
				auto tmp180 = reinterpret_cast<char*>(&tmp179);
				tmp177 += std::string(tmp180, sizeof(unsigned int));
				while (tmp177.size() && tmp177.back() == 0)
					tmp177.pop_back();
				unsigned char tmp182 = tmp177.size();
				auto tmp183 = reinterpret_cast<char*>(&tmp182);
				s += std::string(tmp183, sizeof(unsigned char));
				s += tmp177;
				
				s += tmp176.first;
				
				s += '\x01';
				float tmp185 = tmp176.second;
				auto tmp186 = reinterpret_cast<char*>(&tmp185);
				s += std::string(tmp186, sizeof(float));
			}
		}
		
		// serialize bombs
		s += __has_bombs;
		if (__has_bombs)
		{
			std::string tmp187 = "";
			unsigned int tmp189 = __bombs.size();
			auto tmp190 = reinterpret_cast<char*>(&tmp189);
			tmp187 += std::string(tmp190, sizeof(unsigned int));
			while (tmp187.size() && tmp187.back() == 0)
				tmp187.pop_back();
			unsigned char tmp192 = tmp187.size();
			auto tmp193 = reinterpret_cast<char*>(&tmp192);
			s += std::string(tmp193, sizeof(unsigned char));
			s += tmp187;
			
			for (auto &tmp194 : __bombs)
			{
				s += '\x01';
				s += tmp194.serialize();
			}
		}
		
		// serialize terrorists
		s += __has_terrorists;
		if (__has_terrorists)
		{
			std::string tmp195 = "";
			unsigned int tmp197 = __terrorists.size();
			auto tmp198 = reinterpret_cast<char*>(&tmp197);
			tmp195 += std::string(tmp198, sizeof(unsigned int));
			while (tmp195.size() && tmp195.back() == 0)
				tmp195.pop_back();
			unsigned char tmp200 = tmp195.size();
			auto tmp201 = reinterpret_cast<char*>(&tmp200);
			s += std::string(tmp201, sizeof(unsigned char));
			s += tmp195;
			
			for (auto &tmp202 : __terrorists)
			{
				s += '\x01';
				s += tmp202.serialize();
			}
		}
		
		// serialize polices
		s += __has_polices;
		if (__has_polices)
		{
			std::string tmp203 = "";
			unsigned int tmp205 = __polices.size();
			auto tmp206 = reinterpret_cast<char*>(&tmp205);
			tmp203 += std::string(tmp206, sizeof(unsigned int));
			while (tmp203.size() && tmp203.back() == 0)
				tmp203.pop_back();
			unsigned char tmp208 = tmp203.size();
			auto tmp209 = reinterpret_cast<char*>(&tmp208);
			s += std::string(tmp209, sizeof(unsigned char));
			s += tmp203;
			
			for (auto &tmp210 : __polices)
			{
				s += '\x01';
				s += tmp210.serialize();
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
			unsigned char tmp211;
			tmp211 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp212 = std::string(&s[offset], tmp211);
			offset += tmp211;
			while (tmp212.size() < sizeof(unsigned int))
				tmp212 += '\x00';
			unsigned int tmp213;
			tmp213 = *((unsigned int*) (&tmp212[0]));
			
			__board.clear();
			for (unsigned int tmp214 = 0; tmp214 < tmp213; tmp214++)
			{
				std::vector<ECell> tmp215;
				offset++;
				unsigned char tmp216;
				tmp216 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp217 = std::string(&s[offset], tmp216);
				offset += tmp216;
				while (tmp217.size() < sizeof(unsigned int))
					tmp217 += '\x00';
				unsigned int tmp218;
				tmp218 = *((unsigned int*) (&tmp217[0]));
				
				tmp215.clear();
				for (unsigned int tmp219 = 0; tmp219 < tmp218; tmp219++)
				{
					ECell tmp220;
					offset++;
					char tmp221;
					tmp221 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp220 = (ECell) tmp221;
					tmp215.push_back(tmp220);
				}
				__board.push_back(tmp215);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp222;
			tmp222 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp223 = std::string(&s[offset], tmp222);
			offset += tmp222;
			while (tmp223.size() < sizeof(unsigned int))
				tmp223 += '\x00';
			unsigned int tmp224;
			tmp224 = *((unsigned int*) (&tmp223[0]));
			
			__scores.clear();
			for (unsigned int tmp225 = 0; tmp225 < tmp224; tmp225++)
			{
				std::string tmp226;
				offset++;
				unsigned char tmp228;
				tmp228 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp229 = std::string(&s[offset], tmp228);
				offset += tmp228;
				while (tmp229.size() < sizeof(unsigned int))
					tmp229 += '\x00';
				unsigned int tmp230;
				tmp230 = *((unsigned int*) (&tmp229[0]));
				
				tmp226 = s.substr(offset, tmp230);
				offset += tmp230;
				
				float tmp227;
				offset++;
				tmp227 = *((float*) (&s[offset]));
				offset += sizeof(float);
				
				__scores[tmp226] = tmp227;
			}
		}
		
		// deserialize bombs
		__has_bombs = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombs)
		{
			unsigned char tmp231;
			tmp231 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp232 = std::string(&s[offset], tmp231);
			offset += tmp231;
			while (tmp232.size() < sizeof(unsigned int))
				tmp232 += '\x00';
			unsigned int tmp233;
			tmp233 = *((unsigned int*) (&tmp232[0]));
			
			__bombs.clear();
			for (unsigned int tmp234 = 0; tmp234 < tmp233; tmp234++)
			{
				Bomb tmp235;
				offset++;
				offset = tmp235.deserialize(s, offset);
				__bombs.push_back(tmp235);
			}
		}
		
		// deserialize terrorists
		__has_terrorists = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorists)
		{
			unsigned char tmp236;
			tmp236 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp237 = std::string(&s[offset], tmp236);
			offset += tmp236;
			while (tmp237.size() < sizeof(unsigned int))
				tmp237 += '\x00';
			unsigned int tmp238;
			tmp238 = *((unsigned int*) (&tmp237[0]));
			
			__terrorists.clear();
			for (unsigned int tmp239 = 0; tmp239 < tmp238; tmp239++)
			{
				Terrorist tmp240;
				offset++;
				offset = tmp240.deserialize(s, offset);
				__terrorists.push_back(tmp240);
			}
		}
		
		// deserialize polices
		__has_polices = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_polices)
		{
			unsigned char tmp241;
			tmp241 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp242 = std::string(&s[offset], tmp241);
			offset += tmp241;
			while (tmp242.size() < sizeof(unsigned int))
				tmp242 += '\x00';
			unsigned int tmp243;
			tmp243 = *((unsigned int*) (&tmp242[0]));
			
			__polices.clear();
			for (unsigned int tmp244 = 0; tmp244 < tmp243; tmp244++)
			{
				Police tmp245;
				offset++;
				offset = tmp245.deserialize(s, offset);
				__polices.push_back(tmp245);
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
