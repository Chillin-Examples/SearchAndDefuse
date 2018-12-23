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
	ExplodedBombSite = 5,
	Wall = 6,
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


enum class Status
{
	Alive = 0,
	Dead = 1,
};


class Constants : public KSObject
{

protected:

	int __bombPlantingTime;
	int __bombDefusionTime;
	int __bombExplosionTime;
	int __bombPlantingScore;
	int __bombDefusionScore;
	int __bombExplosionScore;
	float __scoreCoefficientSmallBombSite;
	float __scoreCoefficientMediumBombSite;
	float __scoreCoefficientLargeBombSite;
	float __scoreCoefficientVastBombSite;
	int __terroristVisionDistance;
	int __terroristDeathScore;
	int __policeVisionDistance;
	std::map<ESoundIntensity, int> __soundRanges;
	int __maxCycles;

	bool __has_bombPlantingTime;
	bool __has_bombDefusionTime;
	bool __has_bombExplosionTime;
	bool __has_bombPlantingScore;
	bool __has_bombDefusionScore;
	bool __has_bombExplosionScore;
	bool __has_scoreCoefficientSmallBombSite;
	bool __has_scoreCoefficientMediumBombSite;
	bool __has_scoreCoefficientLargeBombSite;
	bool __has_scoreCoefficientVastBombSite;
	bool __has_terroristVisionDistance;
	bool __has_terroristDeathScore;
	bool __has_policeVisionDistance;
	bool __has_soundRanges;
	bool __has_maxCycles;


public: // getters

	inline int bombPlantingTime() const
	{
		return __bombPlantingTime;
	}
	
	inline int bombDefusionTime() const
	{
		return __bombDefusionTime;
	}
	
	inline int bombExplosionTime() const
	{
		return __bombExplosionTime;
	}
	
	inline int bombPlantingScore() const
	{
		return __bombPlantingScore;
	}
	
	inline int bombDefusionScore() const
	{
		return __bombDefusionScore;
	}
	
	inline int bombExplosionScore() const
	{
		return __bombExplosionScore;
	}
	
	inline float scoreCoefficientSmallBombSite() const
	{
		return __scoreCoefficientSmallBombSite;
	}
	
	inline float scoreCoefficientMediumBombSite() const
	{
		return __scoreCoefficientMediumBombSite;
	}
	
	inline float scoreCoefficientLargeBombSite() const
	{
		return __scoreCoefficientLargeBombSite;
	}
	
	inline float scoreCoefficientVastBombSite() const
	{
		return __scoreCoefficientVastBombSite;
	}
	
	inline int terroristVisionDistance() const
	{
		return __terroristVisionDistance;
	}
	
	inline int terroristDeathScore() const
	{
		return __terroristDeathScore;
	}
	
	inline int policeVisionDistance() const
	{
		return __policeVisionDistance;
	}
	
	inline std::map<ESoundIntensity, int> soundRanges() const
	{
		return __soundRanges;
	}
	
	inline int maxCycles() const
	{
		return __maxCycles;
	}
	

public: // reference getters

	inline int &ref_bombPlantingTime() const
	{
		return (int&) __bombPlantingTime;
	}
	
	inline int &ref_bombDefusionTime() const
	{
		return (int&) __bombDefusionTime;
	}
	
	inline int &ref_bombExplosionTime() const
	{
		return (int&) __bombExplosionTime;
	}
	
	inline int &ref_bombPlantingScore() const
	{
		return (int&) __bombPlantingScore;
	}
	
	inline int &ref_bombDefusionScore() const
	{
		return (int&) __bombDefusionScore;
	}
	
	inline int &ref_bombExplosionScore() const
	{
		return (int&) __bombExplosionScore;
	}
	
	inline float &ref_scoreCoefficientSmallBombSite() const
	{
		return (float&) __scoreCoefficientSmallBombSite;
	}
	
	inline float &ref_scoreCoefficientMediumBombSite() const
	{
		return (float&) __scoreCoefficientMediumBombSite;
	}
	
	inline float &ref_scoreCoefficientLargeBombSite() const
	{
		return (float&) __scoreCoefficientLargeBombSite;
	}
	
	inline float &ref_scoreCoefficientVastBombSite() const
	{
		return (float&) __scoreCoefficientVastBombSite;
	}
	
	inline int &ref_terroristVisionDistance() const
	{
		return (int&) __terroristVisionDistance;
	}
	
	inline int &ref_terroristDeathScore() const
	{
		return (int&) __terroristDeathScore;
	}
	
	inline int &ref_policeVisionDistance() const
	{
		return (int&) __policeVisionDistance;
	}
	
	inline std::map<ESoundIntensity, int> &ref_soundRanges() const
	{
		return (std::map<ESoundIntensity, int>&) __soundRanges;
	}
	
	inline int &ref_maxCycles() const
	{
		return (int&) __maxCycles;
	}
	

public: // setters

	inline void bombPlantingTime(const int &bombPlantingTime)
	{
		__bombPlantingTime = bombPlantingTime;
		has_bombPlantingTime(true);
	}
	
	inline void bombDefusionTime(const int &bombDefusionTime)
	{
		__bombDefusionTime = bombDefusionTime;
		has_bombDefusionTime(true);
	}
	
	inline void bombExplosionTime(const int &bombExplosionTime)
	{
		__bombExplosionTime = bombExplosionTime;
		has_bombExplosionTime(true);
	}
	
	inline void bombPlantingScore(const int &bombPlantingScore)
	{
		__bombPlantingScore = bombPlantingScore;
		has_bombPlantingScore(true);
	}
	
	inline void bombDefusionScore(const int &bombDefusionScore)
	{
		__bombDefusionScore = bombDefusionScore;
		has_bombDefusionScore(true);
	}
	
	inline void bombExplosionScore(const int &bombExplosionScore)
	{
		__bombExplosionScore = bombExplosionScore;
		has_bombExplosionScore(true);
	}
	
	inline void scoreCoefficientSmallBombSite(const float &scoreCoefficientSmallBombSite)
	{
		__scoreCoefficientSmallBombSite = scoreCoefficientSmallBombSite;
		has_scoreCoefficientSmallBombSite(true);
	}
	
	inline void scoreCoefficientMediumBombSite(const float &scoreCoefficientMediumBombSite)
	{
		__scoreCoefficientMediumBombSite = scoreCoefficientMediumBombSite;
		has_scoreCoefficientMediumBombSite(true);
	}
	
	inline void scoreCoefficientLargeBombSite(const float &scoreCoefficientLargeBombSite)
	{
		__scoreCoefficientLargeBombSite = scoreCoefficientLargeBombSite;
		has_scoreCoefficientLargeBombSite(true);
	}
	
	inline void scoreCoefficientVastBombSite(const float &scoreCoefficientVastBombSite)
	{
		__scoreCoefficientVastBombSite = scoreCoefficientVastBombSite;
		has_scoreCoefficientVastBombSite(true);
	}
	
	inline void terroristVisionDistance(const int &terroristVisionDistance)
	{
		__terroristVisionDistance = terroristVisionDistance;
		has_terroristVisionDistance(true);
	}
	
	inline void terroristDeathScore(const int &terroristDeathScore)
	{
		__terroristDeathScore = terroristDeathScore;
		has_terroristDeathScore(true);
	}
	
	inline void policeVisionDistance(const int &policeVisionDistance)
	{
		__policeVisionDistance = policeVisionDistance;
		has_policeVisionDistance(true);
	}
	
	inline void soundRanges(const std::map<ESoundIntensity, int> &soundRanges)
	{
		__soundRanges = soundRanges;
		has_soundRanges(true);
	}
	
	inline void maxCycles(const int &maxCycles)
	{
		__maxCycles = maxCycles;
		has_maxCycles(true);
	}
	

public: // has_attribute getters

	inline bool has_bombPlantingTime() const
	{
		return __has_bombPlantingTime;
	}
	
	inline bool has_bombDefusionTime() const
	{
		return __has_bombDefusionTime;
	}
	
	inline bool has_bombExplosionTime() const
	{
		return __has_bombExplosionTime;
	}
	
	inline bool has_bombPlantingScore() const
	{
		return __has_bombPlantingScore;
	}
	
	inline bool has_bombDefusionScore() const
	{
		return __has_bombDefusionScore;
	}
	
	inline bool has_bombExplosionScore() const
	{
		return __has_bombExplosionScore;
	}
	
	inline bool has_scoreCoefficientSmallBombSite() const
	{
		return __has_scoreCoefficientSmallBombSite;
	}
	
	inline bool has_scoreCoefficientMediumBombSite() const
	{
		return __has_scoreCoefficientMediumBombSite;
	}
	
	inline bool has_scoreCoefficientLargeBombSite() const
	{
		return __has_scoreCoefficientLargeBombSite;
	}
	
	inline bool has_scoreCoefficientVastBombSite() const
	{
		return __has_scoreCoefficientVastBombSite;
	}
	
	inline bool has_terroristVisionDistance() const
	{
		return __has_terroristVisionDistance;
	}
	
	inline bool has_terroristDeathScore() const
	{
		return __has_terroristDeathScore;
	}
	
	inline bool has_policeVisionDistance() const
	{
		return __has_policeVisionDistance;
	}
	
	inline bool has_soundRanges() const
	{
		return __has_soundRanges;
	}
	
	inline bool has_maxCycles() const
	{
		return __has_maxCycles;
	}
	

public: // has_attribute setters

	inline void has_bombPlantingTime(const bool &has_bombPlantingTime)
	{
		__has_bombPlantingTime = has_bombPlantingTime;
	}
	
	inline void has_bombDefusionTime(const bool &has_bombDefusionTime)
	{
		__has_bombDefusionTime = has_bombDefusionTime;
	}
	
	inline void has_bombExplosionTime(const bool &has_bombExplosionTime)
	{
		__has_bombExplosionTime = has_bombExplosionTime;
	}
	
	inline void has_bombPlantingScore(const bool &has_bombPlantingScore)
	{
		__has_bombPlantingScore = has_bombPlantingScore;
	}
	
	inline void has_bombDefusionScore(const bool &has_bombDefusionScore)
	{
		__has_bombDefusionScore = has_bombDefusionScore;
	}
	
	inline void has_bombExplosionScore(const bool &has_bombExplosionScore)
	{
		__has_bombExplosionScore = has_bombExplosionScore;
	}
	
	inline void has_scoreCoefficientSmallBombSite(const bool &has_scoreCoefficientSmallBombSite)
	{
		__has_scoreCoefficientSmallBombSite = has_scoreCoefficientSmallBombSite;
	}
	
	inline void has_scoreCoefficientMediumBombSite(const bool &has_scoreCoefficientMediumBombSite)
	{
		__has_scoreCoefficientMediumBombSite = has_scoreCoefficientMediumBombSite;
	}
	
	inline void has_scoreCoefficientLargeBombSite(const bool &has_scoreCoefficientLargeBombSite)
	{
		__has_scoreCoefficientLargeBombSite = has_scoreCoefficientLargeBombSite;
	}
	
	inline void has_scoreCoefficientVastBombSite(const bool &has_scoreCoefficientVastBombSite)
	{
		__has_scoreCoefficientVastBombSite = has_scoreCoefficientVastBombSite;
	}
	
	inline void has_terroristVisionDistance(const bool &has_terroristVisionDistance)
	{
		__has_terroristVisionDistance = has_terroristVisionDistance;
	}
	
	inline void has_terroristDeathScore(const bool &has_terroristDeathScore)
	{
		__has_terroristDeathScore = has_terroristDeathScore;
	}
	
	inline void has_policeVisionDistance(const bool &has_policeVisionDistance)
	{
		__has_policeVisionDistance = has_policeVisionDistance;
	}
	
	inline void has_soundRanges(const bool &has_soundRanges)
	{
		__has_soundRanges = has_soundRanges;
	}
	
	inline void has_maxCycles(const bool &has_maxCycles)
	{
		__has_maxCycles = has_maxCycles;
	}
	

public:

	Constants()
	{
		has_bombPlantingTime(false);
		has_bombDefusionTime(false);
		has_bombExplosionTime(false);
		has_bombPlantingScore(false);
		has_bombDefusionScore(false);
		has_bombExplosionScore(false);
		has_scoreCoefficientSmallBombSite(false);
		has_scoreCoefficientMediumBombSite(false);
		has_scoreCoefficientLargeBombSite(false);
		has_scoreCoefficientVastBombSite(false);
		has_terroristVisionDistance(false);
		has_terroristDeathScore(false);
		has_policeVisionDistance(false);
		has_soundRanges(false);
		has_maxCycles(false);
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
		
		// serialize bombPlantingTime
		s += __has_bombPlantingTime;
		if (__has_bombPlantingTime)
		{
			int tmp1 = __bombPlantingTime;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize bombDefusionTime
		s += __has_bombDefusionTime;
		if (__has_bombDefusionTime)
		{
			int tmp4 = __bombDefusionTime;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(int));
		}
		
		// serialize bombExplosionTime
		s += __has_bombExplosionTime;
		if (__has_bombExplosionTime)
		{
			int tmp7 = __bombExplosionTime;
			auto tmp8 = reinterpret_cast<char*>(&tmp7);
			s += std::string(tmp8, sizeof(int));
		}
		
		// serialize bombPlantingScore
		s += __has_bombPlantingScore;
		if (__has_bombPlantingScore)
		{
			int tmp10 = __bombPlantingScore;
			auto tmp11 = reinterpret_cast<char*>(&tmp10);
			s += std::string(tmp11, sizeof(int));
		}
		
		// serialize bombDefusionScore
		s += __has_bombDefusionScore;
		if (__has_bombDefusionScore)
		{
			int tmp13 = __bombDefusionScore;
			auto tmp14 = reinterpret_cast<char*>(&tmp13);
			s += std::string(tmp14, sizeof(int));
		}
		
		// serialize bombExplosionScore
		s += __has_bombExplosionScore;
		if (__has_bombExplosionScore)
		{
			int tmp16 = __bombExplosionScore;
			auto tmp17 = reinterpret_cast<char*>(&tmp16);
			s += std::string(tmp17, sizeof(int));
		}
		
		// serialize scoreCoefficientSmallBombSite
		s += __has_scoreCoefficientSmallBombSite;
		if (__has_scoreCoefficientSmallBombSite)
		{
			float tmp19 = __scoreCoefficientSmallBombSite;
			auto tmp20 = reinterpret_cast<char*>(&tmp19);
			s += std::string(tmp20, sizeof(float));
		}
		
		// serialize scoreCoefficientMediumBombSite
		s += __has_scoreCoefficientMediumBombSite;
		if (__has_scoreCoefficientMediumBombSite)
		{
			float tmp22 = __scoreCoefficientMediumBombSite;
			auto tmp23 = reinterpret_cast<char*>(&tmp22);
			s += std::string(tmp23, sizeof(float));
		}
		
		// serialize scoreCoefficientLargeBombSite
		s += __has_scoreCoefficientLargeBombSite;
		if (__has_scoreCoefficientLargeBombSite)
		{
			float tmp25 = __scoreCoefficientLargeBombSite;
			auto tmp26 = reinterpret_cast<char*>(&tmp25);
			s += std::string(tmp26, sizeof(float));
		}
		
		// serialize scoreCoefficientVastBombSite
		s += __has_scoreCoefficientVastBombSite;
		if (__has_scoreCoefficientVastBombSite)
		{
			float tmp28 = __scoreCoefficientVastBombSite;
			auto tmp29 = reinterpret_cast<char*>(&tmp28);
			s += std::string(tmp29, sizeof(float));
		}
		
		// serialize terroristVisionDistance
		s += __has_terroristVisionDistance;
		if (__has_terroristVisionDistance)
		{
			int tmp31 = __terroristVisionDistance;
			auto tmp32 = reinterpret_cast<char*>(&tmp31);
			s += std::string(tmp32, sizeof(int));
		}
		
		// serialize terroristDeathScore
		s += __has_terroristDeathScore;
		if (__has_terroristDeathScore)
		{
			int tmp34 = __terroristDeathScore;
			auto tmp35 = reinterpret_cast<char*>(&tmp34);
			s += std::string(tmp35, sizeof(int));
		}
		
		// serialize policeVisionDistance
		s += __has_policeVisionDistance;
		if (__has_policeVisionDistance)
		{
			int tmp37 = __policeVisionDistance;
			auto tmp38 = reinterpret_cast<char*>(&tmp37);
			s += std::string(tmp38, sizeof(int));
		}
		
		// serialize soundRanges
		s += __has_soundRanges;
		if (__has_soundRanges)
		{
			std::string tmp39 = "";
			unsigned int tmp41 = __soundRanges.size();
			auto tmp42 = reinterpret_cast<char*>(&tmp41);
			tmp39 += std::string(tmp42, sizeof(unsigned int));
			while (tmp39.size() && tmp39.back() == 0)
				tmp39.pop_back();
			unsigned char tmp44 = tmp39.size();
			auto tmp45 = reinterpret_cast<char*>(&tmp44);
			s += std::string(tmp45, sizeof(unsigned char));
			s += tmp39;
			
			for (auto &tmp46 : __soundRanges)
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
		
		// serialize maxCycles
		s += __has_maxCycles;
		if (__has_maxCycles)
		{
			int tmp54 = __maxCycles;
			auto tmp55 = reinterpret_cast<char*>(&tmp54);
			s += std::string(tmp55, sizeof(int));
		}
		
		return s;
	}
	
	unsigned int deserialize(const std::string &s, unsigned int offset=0)
	{
		// deserialize bombPlantingTime
		__has_bombPlantingTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombPlantingTime)
		{
			__bombPlantingTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bombDefusionTime
		__has_bombDefusionTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombDefusionTime)
		{
			__bombDefusionTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bombExplosionTime
		__has_bombExplosionTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombExplosionTime)
		{
			__bombExplosionTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bombPlantingScore
		__has_bombPlantingScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombPlantingScore)
		{
			__bombPlantingScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bombDefusionScore
		__has_bombDefusionScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombDefusionScore)
		{
			__bombDefusionScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize bombExplosionScore
		__has_bombExplosionScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombExplosionScore)
		{
			__bombExplosionScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize scoreCoefficientSmallBombSite
		__has_scoreCoefficientSmallBombSite = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scoreCoefficientSmallBombSite)
		{
			__scoreCoefficientSmallBombSite = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize scoreCoefficientMediumBombSite
		__has_scoreCoefficientMediumBombSite = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scoreCoefficientMediumBombSite)
		{
			__scoreCoefficientMediumBombSite = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize scoreCoefficientLargeBombSite
		__has_scoreCoefficientLargeBombSite = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scoreCoefficientLargeBombSite)
		{
			__scoreCoefficientLargeBombSite = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize scoreCoefficientVastBombSite
		__has_scoreCoefficientVastBombSite = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scoreCoefficientVastBombSite)
		{
			__scoreCoefficientVastBombSite = *((float*) (&s[offset]));
			offset += sizeof(float);
		}
		
		// deserialize terroristVisionDistance
		__has_terroristVisionDistance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terroristVisionDistance)
		{
			__terroristVisionDistance = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize terroristDeathScore
		__has_terroristDeathScore = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terroristDeathScore)
		{
			__terroristDeathScore = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize policeVisionDistance
		__has_policeVisionDistance = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_policeVisionDistance)
		{
			__policeVisionDistance = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize soundRanges
		__has_soundRanges = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_soundRanges)
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
			
			__soundRanges.clear();
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
				
				__soundRanges[tmp60] = tmp61;
			}
		}
		
		// deserialize maxCycles
		__has_maxCycles = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_maxCycles)
		{
			__maxCycles = *((int*) (&s[offset]));
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
	int __explosionRemainingTime;
	int __planterId;
	int __defuserId;

	bool __has_position;
	bool __has_explosionRemainingTime;
	bool __has_planterId;
	bool __has_defuserId;


public: // getters

	inline Position position() const
	{
		return __position;
	}
	
	inline int explosionRemainingTime() const
	{
		return __explosionRemainingTime;
	}
	
	inline int planterId() const
	{
		return __planterId;
	}
	
	inline int defuserId() const
	{
		return __defuserId;
	}
	

public: // reference getters

	inline Position &ref_position() const
	{
		return (Position&) __position;
	}
	
	inline int &ref_explosionRemainingTime() const
	{
		return (int&) __explosionRemainingTime;
	}
	
	inline int &ref_planterId() const
	{
		return (int&) __planterId;
	}
	
	inline int &ref_defuserId() const
	{
		return (int&) __defuserId;
	}
	

public: // setters

	inline void position(const Position &position)
	{
		__position = position;
		has_position(true);
	}
	
	inline void explosionRemainingTime(const int &explosionRemainingTime)
	{
		__explosionRemainingTime = explosionRemainingTime;
		has_explosionRemainingTime(true);
	}
	
	inline void planterId(const int &planterId)
	{
		__planterId = planterId;
		has_planterId(true);
	}
	
	inline void defuserId(const int &defuserId)
	{
		__defuserId = defuserId;
		has_defuserId(true);
	}
	

public: // has_attribute getters

	inline bool has_position() const
	{
		return __has_position;
	}
	
	inline bool has_explosionRemainingTime() const
	{
		return __has_explosionRemainingTime;
	}
	
	inline bool has_planterId() const
	{
		return __has_planterId;
	}
	
	inline bool has_defuserId() const
	{
		return __has_defuserId;
	}
	

public: // has_attribute setters

	inline void has_position(const bool &has_position)
	{
		__has_position = has_position;
	}
	
	inline void has_explosionRemainingTime(const bool &has_explosionRemainingTime)
	{
		__has_explosionRemainingTime = has_explosionRemainingTime;
	}
	
	inline void has_planterId(const bool &has_planterId)
	{
		__has_planterId = has_planterId;
	}
	
	inline void has_defuserId(const bool &has_defuserId)
	{
		__has_defuserId = has_defuserId;
	}
	

public:

	Bomb()
	{
		has_position(false);
		has_explosionRemainingTime(false);
		has_planterId(false);
		has_defuserId(false);
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
		
		// serialize explosionRemainingTime
		s += __has_explosionRemainingTime;
		if (__has_explosionRemainingTime)
		{
			int tmp70 = __explosionRemainingTime;
			auto tmp71 = reinterpret_cast<char*>(&tmp70);
			s += std::string(tmp71, sizeof(int));
		}
		
		// serialize planterId
		s += __has_planterId;
		if (__has_planterId)
		{
			int tmp73 = __planterId;
			auto tmp74 = reinterpret_cast<char*>(&tmp73);
			s += std::string(tmp74, sizeof(int));
		}
		
		// serialize defuserId
		s += __has_defuserId;
		if (__has_defuserId)
		{
			int tmp76 = __defuserId;
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
		
		// deserialize explosionRemainingTime
		__has_explosionRemainingTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_explosionRemainingTime)
		{
			__explosionRemainingTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize planterId
		__has_planterId = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_planterId)
		{
			__planterId = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize defuserId
		__has_defuserId = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_defuserId)
		{
			__defuserId = *((int*) (&s[offset]));
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
	int __plantingRemainingTime;
	std::vector<int> __footstepSounds;
	Status __status;

	bool __has_id;
	bool __has_position;
	bool __has_plantingRemainingTime;
	bool __has_footstepSounds;
	bool __has_status;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline int plantingRemainingTime() const
	{
		return __plantingRemainingTime;
	}
	
	inline std::vector<int> footstepSounds() const
	{
		return __footstepSounds;
	}
	
	inline Status status() const
	{
		return __status;
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
	
	inline int &ref_plantingRemainingTime() const
	{
		return (int&) __plantingRemainingTime;
	}
	
	inline std::vector<int> &ref_footstepSounds() const
	{
		return (std::vector<int>&) __footstepSounds;
	}
	
	inline Status &ref_status() const
	{
		return (Status&) __status;
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
	
	inline void plantingRemainingTime(const int &plantingRemainingTime)
	{
		__plantingRemainingTime = plantingRemainingTime;
		has_plantingRemainingTime(true);
	}
	
	inline void footstepSounds(const std::vector<int> &footstepSounds)
	{
		__footstepSounds = footstepSounds;
		has_footstepSounds(true);
	}
	
	inline void status(const Status &status)
	{
		__status = status;
		has_status(true);
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
	
	inline bool has_plantingRemainingTime() const
	{
		return __has_plantingRemainingTime;
	}
	
	inline bool has_footstepSounds() const
	{
		return __has_footstepSounds;
	}
	
	inline bool has_status() const
	{
		return __has_status;
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
	
	inline void has_plantingRemainingTime(const bool &has_plantingRemainingTime)
	{
		__has_plantingRemainingTime = has_plantingRemainingTime;
	}
	
	inline void has_footstepSounds(const bool &has_footstepSounds)
	{
		__has_footstepSounds = has_footstepSounds;
	}
	
	inline void has_status(const bool &has_status)
	{
		__has_status = has_status;
	}
	

public:

	Terrorist()
	{
		has_id(false);
		has_position(false);
		has_plantingRemainingTime(false);
		has_footstepSounds(false);
		has_status(false);
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
		
		// serialize plantingRemainingTime
		s += __has_plantingRemainingTime;
		if (__has_plantingRemainingTime)
		{
			int tmp82 = __plantingRemainingTime;
			auto tmp83 = reinterpret_cast<char*>(&tmp82);
			s += std::string(tmp83, sizeof(int));
		}
		
		// serialize footstepSounds
		s += __has_footstepSounds;
		if (__has_footstepSounds)
		{
			std::string tmp84 = "";
			unsigned int tmp86 = __footstepSounds.size();
			auto tmp87 = reinterpret_cast<char*>(&tmp86);
			tmp84 += std::string(tmp87, sizeof(unsigned int));
			while (tmp84.size() && tmp84.back() == 0)
				tmp84.pop_back();
			unsigned char tmp89 = tmp84.size();
			auto tmp90 = reinterpret_cast<char*>(&tmp89);
			s += std::string(tmp90, sizeof(unsigned char));
			s += tmp84;
			
			for (auto &tmp91 : __footstepSounds)
			{
				s += '\x01';
				int tmp93 = tmp91;
				auto tmp94 = reinterpret_cast<char*>(&tmp93);
				s += std::string(tmp94, sizeof(int));
			}
		}
		
		// serialize status
		s += __has_status;
		if (__has_status)
		{
			char tmp96 = (char) __status;
			auto tmp97 = reinterpret_cast<char*>(&tmp96);
			s += std::string(tmp97, sizeof(char));
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
		
		// deserialize plantingRemainingTime
		__has_plantingRemainingTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_plantingRemainingTime)
		{
			__plantingRemainingTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize footstepSounds
		__has_footstepSounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_footstepSounds)
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
			
			__footstepSounds.clear();
			for (unsigned int tmp101 = 0; tmp101 < tmp100; tmp101++)
			{
				int tmp102;
				offset++;
				tmp102 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstepSounds.push_back(tmp102);
			}
		}
		
		// deserialize status
		__has_status = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_status)
		{
			char tmp103;
			tmp103 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__status = (Status) tmp103;
		}
		
		return offset;
	}
};


class Police : public KSObject
{

protected:

	int __id;
	Position __position;
	int __defusionRemainingTime;
	std::vector<int> __footstepSounds;
	std::vector<int> __bombSounds;
	Status __status;

	bool __has_id;
	bool __has_position;
	bool __has_defusionRemainingTime;
	bool __has_footstepSounds;
	bool __has_bombSounds;
	bool __has_status;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline Position position() const
	{
		return __position;
	}
	
	inline int defusionRemainingTime() const
	{
		return __defusionRemainingTime;
	}
	
	inline std::vector<int> footstepSounds() const
	{
		return __footstepSounds;
	}
	
	inline std::vector<int> bombSounds() const
	{
		return __bombSounds;
	}
	
	inline Status status() const
	{
		return __status;
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
	
	inline int &ref_defusionRemainingTime() const
	{
		return (int&) __defusionRemainingTime;
	}
	
	inline std::vector<int> &ref_footstepSounds() const
	{
		return (std::vector<int>&) __footstepSounds;
	}
	
	inline std::vector<int> &ref_bombSounds() const
	{
		return (std::vector<int>&) __bombSounds;
	}
	
	inline Status &ref_status() const
	{
		return (Status&) __status;
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
	
	inline void defusionRemainingTime(const int &defusionRemainingTime)
	{
		__defusionRemainingTime = defusionRemainingTime;
		has_defusionRemainingTime(true);
	}
	
	inline void footstepSounds(const std::vector<int> &footstepSounds)
	{
		__footstepSounds = footstepSounds;
		has_footstepSounds(true);
	}
	
	inline void bombSounds(const std::vector<int> &bombSounds)
	{
		__bombSounds = bombSounds;
		has_bombSounds(true);
	}
	
	inline void status(const Status &status)
	{
		__status = status;
		has_status(true);
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
	
	inline bool has_defusionRemainingTime() const
	{
		return __has_defusionRemainingTime;
	}
	
	inline bool has_footstepSounds() const
	{
		return __has_footstepSounds;
	}
	
	inline bool has_bombSounds() const
	{
		return __has_bombSounds;
	}
	
	inline bool has_status() const
	{
		return __has_status;
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
	
	inline void has_defusionRemainingTime(const bool &has_defusionRemainingTime)
	{
		__has_defusionRemainingTime = has_defusionRemainingTime;
	}
	
	inline void has_footstepSounds(const bool &has_footstepSounds)
	{
		__has_footstepSounds = has_footstepSounds;
	}
	
	inline void has_bombSounds(const bool &has_bombSounds)
	{
		__has_bombSounds = has_bombSounds;
	}
	
	inline void has_status(const bool &has_status)
	{
		__has_status = has_status;
	}
	

public:

	Police()
	{
		has_id(false);
		has_position(false);
		has_defusionRemainingTime(false);
		has_footstepSounds(false);
		has_bombSounds(false);
		has_status(false);
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
			int tmp105 = __id;
			auto tmp106 = reinterpret_cast<char*>(&tmp105);
			s += std::string(tmp106, sizeof(int));
		}
		
		// serialize position
		s += __has_position;
		if (__has_position)
		{
			s += __position.serialize();
		}
		
		// serialize defusionRemainingTime
		s += __has_defusionRemainingTime;
		if (__has_defusionRemainingTime)
		{
			int tmp108 = __defusionRemainingTime;
			auto tmp109 = reinterpret_cast<char*>(&tmp108);
			s += std::string(tmp109, sizeof(int));
		}
		
		// serialize footstepSounds
		s += __has_footstepSounds;
		if (__has_footstepSounds)
		{
			std::string tmp110 = "";
			unsigned int tmp112 = __footstepSounds.size();
			auto tmp113 = reinterpret_cast<char*>(&tmp112);
			tmp110 += std::string(tmp113, sizeof(unsigned int));
			while (tmp110.size() && tmp110.back() == 0)
				tmp110.pop_back();
			unsigned char tmp115 = tmp110.size();
			auto tmp116 = reinterpret_cast<char*>(&tmp115);
			s += std::string(tmp116, sizeof(unsigned char));
			s += tmp110;
			
			for (auto &tmp117 : __footstepSounds)
			{
				s += '\x01';
				int tmp119 = tmp117;
				auto tmp120 = reinterpret_cast<char*>(&tmp119);
				s += std::string(tmp120, sizeof(int));
			}
		}
		
		// serialize bombSounds
		s += __has_bombSounds;
		if (__has_bombSounds)
		{
			std::string tmp121 = "";
			unsigned int tmp123 = __bombSounds.size();
			auto tmp124 = reinterpret_cast<char*>(&tmp123);
			tmp121 += std::string(tmp124, sizeof(unsigned int));
			while (tmp121.size() && tmp121.back() == 0)
				tmp121.pop_back();
			unsigned char tmp126 = tmp121.size();
			auto tmp127 = reinterpret_cast<char*>(&tmp126);
			s += std::string(tmp127, sizeof(unsigned char));
			s += tmp121;
			
			for (auto &tmp128 : __bombSounds)
			{
				s += '\x01';
				int tmp130 = tmp128;
				auto tmp131 = reinterpret_cast<char*>(&tmp130);
				s += std::string(tmp131, sizeof(int));
			}
		}
		
		// serialize status
		s += __has_status;
		if (__has_status)
		{
			char tmp133 = (char) __status;
			auto tmp134 = reinterpret_cast<char*>(&tmp133);
			s += std::string(tmp134, sizeof(char));
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
		
		// deserialize defusionRemainingTime
		__has_defusionRemainingTime = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_defusionRemainingTime)
		{
			__defusionRemainingTime = *((int*) (&s[offset]));
			offset += sizeof(int);
		}
		
		// deserialize footstepSounds
		__has_footstepSounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_footstepSounds)
		{
			unsigned char tmp135;
			tmp135 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp136 = std::string(&s[offset], tmp135);
			offset += tmp135;
			while (tmp136.size() < sizeof(unsigned int))
				tmp136 += '\x00';
			unsigned int tmp137;
			tmp137 = *((unsigned int*) (&tmp136[0]));
			
			__footstepSounds.clear();
			for (unsigned int tmp138 = 0; tmp138 < tmp137; tmp138++)
			{
				int tmp139;
				offset++;
				tmp139 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstepSounds.push_back(tmp139);
			}
		}
		
		// deserialize bombSounds
		__has_bombSounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombSounds)
		{
			unsigned char tmp140;
			tmp140 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp141 = std::string(&s[offset], tmp140);
			offset += tmp140;
			while (tmp141.size() < sizeof(unsigned int))
				tmp141 += '\x00';
			unsigned int tmp142;
			tmp142 = *((unsigned int*) (&tmp141[0]));
			
			__bombSounds.clear();
			for (unsigned int tmp143 = 0; tmp143 < tmp142; tmp143++)
			{
				int tmp144;
				offset++;
				tmp144 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bombSounds.push_back(tmp144);
			}
		}
		
		// deserialize status
		__has_status = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_status)
		{
			char tmp145;
			tmp145 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__status = (Status) tmp145;
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
			int tmp147 = __width;
			auto tmp148 = reinterpret_cast<char*>(&tmp147);
			s += std::string(tmp148, sizeof(int));
		}
		
		// serialize height
		s += __has_height;
		if (__has_height)
		{
			int tmp150 = __height;
			auto tmp151 = reinterpret_cast<char*>(&tmp150);
			s += std::string(tmp151, sizeof(int));
		}
		
		// serialize board
		s += __has_board;
		if (__has_board)
		{
			std::string tmp152 = "";
			unsigned int tmp154 = __board.size();
			auto tmp155 = reinterpret_cast<char*>(&tmp154);
			tmp152 += std::string(tmp155, sizeof(unsigned int));
			while (tmp152.size() && tmp152.back() == 0)
				tmp152.pop_back();
			unsigned char tmp157 = tmp152.size();
			auto tmp158 = reinterpret_cast<char*>(&tmp157);
			s += std::string(tmp158, sizeof(unsigned char));
			s += tmp152;
			
			for (auto &tmp159 : __board)
			{
				s += '\x01';
				std::string tmp160 = "";
				unsigned int tmp162 = tmp159.size();
				auto tmp163 = reinterpret_cast<char*>(&tmp162);
				tmp160 += std::string(tmp163, sizeof(unsigned int));
				while (tmp160.size() && tmp160.back() == 0)
					tmp160.pop_back();
				unsigned char tmp165 = tmp160.size();
				auto tmp166 = reinterpret_cast<char*>(&tmp165);
				s += std::string(tmp166, sizeof(unsigned char));
				s += tmp160;
				
				for (auto &tmp167 : tmp159)
				{
					s += '\x01';
					char tmp169 = (char) tmp167;
					auto tmp170 = reinterpret_cast<char*>(&tmp169);
					s += std::string(tmp170, sizeof(char));
				}
			}
		}
		
		// serialize scores
		s += __has_scores;
		if (__has_scores)
		{
			std::string tmp171 = "";
			unsigned int tmp173 = __scores.size();
			auto tmp174 = reinterpret_cast<char*>(&tmp173);
			tmp171 += std::string(tmp174, sizeof(unsigned int));
			while (tmp171.size() && tmp171.back() == 0)
				tmp171.pop_back();
			unsigned char tmp176 = tmp171.size();
			auto tmp177 = reinterpret_cast<char*>(&tmp176);
			s += std::string(tmp177, sizeof(unsigned char));
			s += tmp171;
			
			for (auto &tmp178 : __scores)
			{
				s += '\x01';
				std::string tmp179 = "";
				unsigned int tmp181 = tmp178.first.size();
				auto tmp182 = reinterpret_cast<char*>(&tmp181);
				tmp179 += std::string(tmp182, sizeof(unsigned int));
				while (tmp179.size() && tmp179.back() == 0)
					tmp179.pop_back();
				unsigned char tmp184 = tmp179.size();
				auto tmp185 = reinterpret_cast<char*>(&tmp184);
				s += std::string(tmp185, sizeof(unsigned char));
				s += tmp179;
				
				s += tmp178.first;
				
				s += '\x01';
				float tmp187 = tmp178.second;
				auto tmp188 = reinterpret_cast<char*>(&tmp187);
				s += std::string(tmp188, sizeof(float));
			}
		}
		
		// serialize bombs
		s += __has_bombs;
		if (__has_bombs)
		{
			std::string tmp189 = "";
			unsigned int tmp191 = __bombs.size();
			auto tmp192 = reinterpret_cast<char*>(&tmp191);
			tmp189 += std::string(tmp192, sizeof(unsigned int));
			while (tmp189.size() && tmp189.back() == 0)
				tmp189.pop_back();
			unsigned char tmp194 = tmp189.size();
			auto tmp195 = reinterpret_cast<char*>(&tmp194);
			s += std::string(tmp195, sizeof(unsigned char));
			s += tmp189;
			
			for (auto &tmp196 : __bombs)
			{
				s += '\x01';
				s += tmp196.serialize();
			}
		}
		
		// serialize terrorists
		s += __has_terrorists;
		if (__has_terrorists)
		{
			std::string tmp197 = "";
			unsigned int tmp199 = __terrorists.size();
			auto tmp200 = reinterpret_cast<char*>(&tmp199);
			tmp197 += std::string(tmp200, sizeof(unsigned int));
			while (tmp197.size() && tmp197.back() == 0)
				tmp197.pop_back();
			unsigned char tmp202 = tmp197.size();
			auto tmp203 = reinterpret_cast<char*>(&tmp202);
			s += std::string(tmp203, sizeof(unsigned char));
			s += tmp197;
			
			for (auto &tmp204 : __terrorists)
			{
				s += '\x01';
				s += tmp204.serialize();
			}
		}
		
		// serialize polices
		s += __has_polices;
		if (__has_polices)
		{
			std::string tmp205 = "";
			unsigned int tmp207 = __polices.size();
			auto tmp208 = reinterpret_cast<char*>(&tmp207);
			tmp205 += std::string(tmp208, sizeof(unsigned int));
			while (tmp205.size() && tmp205.back() == 0)
				tmp205.pop_back();
			unsigned char tmp210 = tmp205.size();
			auto tmp211 = reinterpret_cast<char*>(&tmp210);
			s += std::string(tmp211, sizeof(unsigned char));
			s += tmp205;
			
			for (auto &tmp212 : __polices)
			{
				s += '\x01';
				s += tmp212.serialize();
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
			unsigned char tmp213;
			tmp213 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp214 = std::string(&s[offset], tmp213);
			offset += tmp213;
			while (tmp214.size() < sizeof(unsigned int))
				tmp214 += '\x00';
			unsigned int tmp215;
			tmp215 = *((unsigned int*) (&tmp214[0]));
			
			__board.clear();
			for (unsigned int tmp216 = 0; tmp216 < tmp215; tmp216++)
			{
				std::vector<ECell> tmp217;
				offset++;
				unsigned char tmp218;
				tmp218 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp219 = std::string(&s[offset], tmp218);
				offset += tmp218;
				while (tmp219.size() < sizeof(unsigned int))
					tmp219 += '\x00';
				unsigned int tmp220;
				tmp220 = *((unsigned int*) (&tmp219[0]));
				
				tmp217.clear();
				for (unsigned int tmp221 = 0; tmp221 < tmp220; tmp221++)
				{
					ECell tmp222;
					offset++;
					char tmp223;
					tmp223 = *((char*) (&s[offset]));
					offset += sizeof(char);
					tmp222 = (ECell) tmp223;
					tmp217.push_back(tmp222);
				}
				__board.push_back(tmp217);
			}
		}
		
		// deserialize scores
		__has_scores = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_scores)
		{
			unsigned char tmp224;
			tmp224 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp225 = std::string(&s[offset], tmp224);
			offset += tmp224;
			while (tmp225.size() < sizeof(unsigned int))
				tmp225 += '\x00';
			unsigned int tmp226;
			tmp226 = *((unsigned int*) (&tmp225[0]));
			
			__scores.clear();
			for (unsigned int tmp227 = 0; tmp227 < tmp226; tmp227++)
			{
				std::string tmp228;
				offset++;
				unsigned char tmp230;
				tmp230 = *((unsigned char*) (&s[offset]));
				offset += sizeof(unsigned char);
				std::string tmp231 = std::string(&s[offset], tmp230);
				offset += tmp230;
				while (tmp231.size() < sizeof(unsigned int))
					tmp231 += '\x00';
				unsigned int tmp232;
				tmp232 = *((unsigned int*) (&tmp231[0]));
				
				tmp228 = s.substr(offset, tmp232);
				offset += tmp232;
				
				float tmp229;
				offset++;
				tmp229 = *((float*) (&s[offset]));
				offset += sizeof(float);
				
				__scores[tmp228] = tmp229;
			}
		}
		
		// deserialize bombs
		__has_bombs = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombs)
		{
			unsigned char tmp233;
			tmp233 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp234 = std::string(&s[offset], tmp233);
			offset += tmp233;
			while (tmp234.size() < sizeof(unsigned int))
				tmp234 += '\x00';
			unsigned int tmp235;
			tmp235 = *((unsigned int*) (&tmp234[0]));
			
			__bombs.clear();
			for (unsigned int tmp236 = 0; tmp236 < tmp235; tmp236++)
			{
				Bomb tmp237;
				offset++;
				offset = tmp237.deserialize(s, offset);
				__bombs.push_back(tmp237);
			}
		}
		
		// deserialize terrorists
		__has_terrorists = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_terrorists)
		{
			unsigned char tmp238;
			tmp238 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp239 = std::string(&s[offset], tmp238);
			offset += tmp238;
			while (tmp239.size() < sizeof(unsigned int))
				tmp239 += '\x00';
			unsigned int tmp240;
			tmp240 = *((unsigned int*) (&tmp239[0]));
			
			__terrorists.clear();
			for (unsigned int tmp241 = 0; tmp241 < tmp240; tmp241++)
			{
				Terrorist tmp242;
				offset++;
				offset = tmp242.deserialize(s, offset);
				__terrorists.push_back(tmp242);
			}
		}
		
		// deserialize polices
		__has_polices = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_polices)
		{
			unsigned char tmp243;
			tmp243 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp244 = std::string(&s[offset], tmp243);
			offset += tmp243;
			while (tmp244.size() < sizeof(unsigned int))
				tmp244 += '\x00';
			unsigned int tmp245;
			tmp245 = *((unsigned int*) (&tmp244[0]));
			
			__polices.clear();
			for (unsigned int tmp246 = 0; tmp246 < tmp245; tmp246++)
			{
				Police tmp247;
				offset++;
				offset = tmp247.deserialize(s, offset);
				__polices.push_back(tmp247);
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
