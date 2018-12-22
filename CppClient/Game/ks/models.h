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
	bool __isDead;

	bool __has_id;
	bool __has_position;
	bool __has_plantingRemainingTime;
	bool __has_footstepSounds;
	bool __has_isDead;


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
	
	inline bool isDead() const
	{
		return __isDead;
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
	
	inline bool &ref_isDead() const
	{
		return (bool&) __isDead;
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
	
	inline void isDead(const bool &isDead)
	{
		__isDead = isDead;
		has_isDead(true);
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
	
	inline bool has_isDead() const
	{
		return __has_isDead;
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
	
	inline void has_isDead(const bool &has_isDead)
	{
		__has_isDead = has_isDead;
	}
	

public:

	Terrorist()
	{
		has_id(false);
		has_position(false);
		has_plantingRemainingTime(false);
		has_footstepSounds(false);
		has_isDead(false);
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
		
		// serialize isDead
		s += __has_isDead;
		if (__has_isDead)
		{
			bool tmp96 = __isDead;
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
		
		// deserialize isDead
		__has_isDead = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_isDead)
		{
			__isDead = *((bool*) (&s[offset]));
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
	int __defusionRemainingTime;
	std::vector<int> __footstepSounds;
	std::vector<int> __bombSounds;
	bool __isVisible;

	bool __has_id;
	bool __has_position;
	bool __has_defusionRemainingTime;
	bool __has_footstepSounds;
	bool __has_bombSounds;
	bool __has_isVisible;


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
	
	inline bool isVisible() const
	{
		return __isVisible;
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
	
	inline bool &ref_isVisible() const
	{
		return (bool&) __isVisible;
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
	
	inline void isVisible(const bool &isVisible)
	{
		__isVisible = isVisible;
		has_isVisible(true);
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
	
	inline bool has_isVisible() const
	{
		return __has_isVisible;
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
	
	inline void has_isVisible(const bool &has_isVisible)
	{
		__has_isVisible = has_isVisible;
	}
	

public:

	Police()
	{
		has_id(false);
		has_position(false);
		has_defusionRemainingTime(false);
		has_footstepSounds(false);
		has_bombSounds(false);
		has_isVisible(false);
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
		
		// serialize defusionRemainingTime
		s += __has_defusionRemainingTime;
		if (__has_defusionRemainingTime)
		{
			int tmp107 = __defusionRemainingTime;
			auto tmp108 = reinterpret_cast<char*>(&tmp107);
			s += std::string(tmp108, sizeof(int));
		}
		
		// serialize footstepSounds
		s += __has_footstepSounds;
		if (__has_footstepSounds)
		{
			std::string tmp109 = "";
			unsigned int tmp111 = __footstepSounds.size();
			auto tmp112 = reinterpret_cast<char*>(&tmp111);
			tmp109 += std::string(tmp112, sizeof(unsigned int));
			while (tmp109.size() && tmp109.back() == 0)
				tmp109.pop_back();
			unsigned char tmp114 = tmp109.size();
			auto tmp115 = reinterpret_cast<char*>(&tmp114);
			s += std::string(tmp115, sizeof(unsigned char));
			s += tmp109;
			
			for (auto &tmp116 : __footstepSounds)
			{
				s += '\x01';
				int tmp118 = tmp116;
				auto tmp119 = reinterpret_cast<char*>(&tmp118);
				s += std::string(tmp119, sizeof(int));
			}
		}
		
		// serialize bombSounds
		s += __has_bombSounds;
		if (__has_bombSounds)
		{
			std::string tmp120 = "";
			unsigned int tmp122 = __bombSounds.size();
			auto tmp123 = reinterpret_cast<char*>(&tmp122);
			tmp120 += std::string(tmp123, sizeof(unsigned int));
			while (tmp120.size() && tmp120.back() == 0)
				tmp120.pop_back();
			unsigned char tmp125 = tmp120.size();
			auto tmp126 = reinterpret_cast<char*>(&tmp125);
			s += std::string(tmp126, sizeof(unsigned char));
			s += tmp120;
			
			for (auto &tmp127 : __bombSounds)
			{
				s += '\x01';
				int tmp129 = tmp127;
				auto tmp130 = reinterpret_cast<char*>(&tmp129);
				s += std::string(tmp130, sizeof(int));
			}
		}
		
		// serialize isVisible
		s += __has_isVisible;
		if (__has_isVisible)
		{
			bool tmp132 = __isVisible;
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
			unsigned char tmp134;
			tmp134 = *((unsigned char*) (&s[offset]));
			offset += sizeof(unsigned char);
			std::string tmp135 = std::string(&s[offset], tmp134);
			offset += tmp134;
			while (tmp135.size() < sizeof(unsigned int))
				tmp135 += '\x00';
			unsigned int tmp136;
			tmp136 = *((unsigned int*) (&tmp135[0]));
			
			__footstepSounds.clear();
			for (unsigned int tmp137 = 0; tmp137 < tmp136; tmp137++)
			{
				int tmp138;
				offset++;
				tmp138 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__footstepSounds.push_back(tmp138);
			}
		}
		
		// deserialize bombSounds
		__has_bombSounds = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_bombSounds)
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
			
			__bombSounds.clear();
			for (unsigned int tmp142 = 0; tmp142 < tmp141; tmp142++)
			{
				int tmp143;
				offset++;
				tmp143 = *((int*) (&s[offset]));
				offset += sizeof(int);
				__bombSounds.push_back(tmp143);
			}
		}
		
		// deserialize isVisible
		__has_isVisible = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_isVisible)
		{
			__isVisible = *((bool*) (&s[offset]));
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
