#ifndef _KS_COMMANDS_H_
#define _KS_COMMANDS_H_

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


namespace commands
{

enum class ECommandDirection
{
	Up = 0,
	Right = 1,
	Down = 2,
	Left = 3,
};


class Move : public KSObject
{

protected:

	int __id;
	ECommandDirection __direction;

	bool __has_id;
	bool __has_direction;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline ECommandDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline ECommandDirection &ref_direction() const
	{
		return (ECommandDirection&) __direction;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void direction(const ECommandDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	Move()
	{
		has_id(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "Move";
	}
	
	virtual inline const std::string name() const
	{
		return "Move";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp1 = __id;
			auto tmp2 = reinterpret_cast<char*>(&tmp1);
			s += std::string(tmp2, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp4 = (char) __direction;
			auto tmp5 = reinterpret_cast<char*>(&tmp4);
			s += std::string(tmp5, sizeof(char));
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
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp6;
			tmp6 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (ECommandDirection) tmp6;
		}
		
		return offset;
	}
};


class PlantBomb : public KSObject
{

protected:

	int __id;
	ECommandDirection __direction;

	bool __has_id;
	bool __has_direction;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline ECommandDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline ECommandDirection &ref_direction() const
	{
		return (ECommandDirection&) __direction;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void direction(const ECommandDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	PlantBomb()
	{
		has_id(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "PlantBomb";
	}
	
	virtual inline const std::string name() const
	{
		return "PlantBomb";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp8 = __id;
			auto tmp9 = reinterpret_cast<char*>(&tmp8);
			s += std::string(tmp9, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp11 = (char) __direction;
			auto tmp12 = reinterpret_cast<char*>(&tmp11);
			s += std::string(tmp12, sizeof(char));
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
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp13;
			tmp13 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (ECommandDirection) tmp13;
		}
		
		return offset;
	}
};


class DefuseBomb : public KSObject
{

protected:

	int __id;
	ECommandDirection __direction;

	bool __has_id;
	bool __has_direction;


public: // getters

	inline int id() const
	{
		return __id;
	}
	
	inline ECommandDirection direction() const
	{
		return __direction;
	}
	

public: // reference getters

	inline int &ref_id() const
	{
		return (int&) __id;
	}
	
	inline ECommandDirection &ref_direction() const
	{
		return (ECommandDirection&) __direction;
	}
	

public: // setters

	inline void id(const int &id)
	{
		__id = id;
		has_id(true);
	}
	
	inline void direction(const ECommandDirection &direction)
	{
		__direction = direction;
		has_direction(true);
	}
	

public: // has_attribute getters

	inline bool has_id() const
	{
		return __has_id;
	}
	
	inline bool has_direction() const
	{
		return __has_direction;
	}
	

public: // has_attribute setters

	inline void has_id(const bool &has_id)
	{
		__has_id = has_id;
	}
	
	inline void has_direction(const bool &has_direction)
	{
		__has_direction = has_direction;
	}
	

public:

	DefuseBomb()
	{
		has_id(false);
		has_direction(false);
	}
	
	static inline const std::string nameStatic()
	{
		return "DefuseBomb";
	}
	
	virtual inline const std::string name() const
	{
		return "DefuseBomb";
	}
	
	std::string serialize() const
	{
		std::string s = "";
		
		// serialize id
		s += __has_id;
		if (__has_id)
		{
			int tmp15 = __id;
			auto tmp16 = reinterpret_cast<char*>(&tmp15);
			s += std::string(tmp16, sizeof(int));
		}
		
		// serialize direction
		s += __has_direction;
		if (__has_direction)
		{
			char tmp18 = (char) __direction;
			auto tmp19 = reinterpret_cast<char*>(&tmp18);
			s += std::string(tmp19, sizeof(char));
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
		
		// deserialize direction
		__has_direction = *((unsigned char*) (&s[offset]));
		offset += sizeof(unsigned char);
		if (__has_direction)
		{
			char tmp20;
			tmp20 = *((char*) (&s[offset]));
			offset += sizeof(char);
			__direction = (ECommandDirection) tmp20;
		}
		
		return offset;
	}
};

} // namespace commands

} // namespace ks

#endif // _KS_COMMANDS_H_
