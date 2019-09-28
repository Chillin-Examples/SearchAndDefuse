using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Commands
{
	public enum ECommandDirection
	{
		Up = 0,
		Right = 1,
		Down = 2,
		Left = 3,
	}
	
	public partial class Move : KSObject
	{
		public int? Id { get; set; }
		public ECommandDirection? Direction { get; set; }
		

		public Move()
		{
		}
		
		public new const string NameStatic = "Move";
		
		public override string Name() => "Move";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			// serialize Direction
			s.Add((byte)((Direction == null) ? 0 : 1));
			if (Direction != null)
			{
				s.Add((byte)((sbyte)Direction));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Id
			byte tmp0;
			tmp0 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp0 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Direction
			byte tmp1;
			tmp1 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp1 == 1)
			{
				sbyte tmp2;
				tmp2 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (ECommandDirection)tmp2;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
	
	public partial class PlantBomb : KSObject
	{
		public int? Id { get; set; }
		public ECommandDirection? Direction { get; set; }
		

		public PlantBomb()
		{
		}
		
		public new const string NameStatic = "PlantBomb";
		
		public override string Name() => "PlantBomb";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			// serialize Direction
			s.Add((byte)((Direction == null) ? 0 : 1));
			if (Direction != null)
			{
				s.Add((byte)((sbyte)Direction));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Id
			byte tmp3;
			tmp3 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp3 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Direction
			byte tmp4;
			tmp4 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp4 == 1)
			{
				sbyte tmp5;
				tmp5 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (ECommandDirection)tmp5;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
	
	public partial class DefuseBomb : KSObject
	{
		public int? Id { get; set; }
		public ECommandDirection? Direction { get; set; }
		

		public DefuseBomb()
		{
		}
		
		public new const string NameStatic = "DefuseBomb";
		
		public override string Name() => "DefuseBomb";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			// serialize Direction
			s.Add((byte)((Direction == null) ? 0 : 1));
			if (Direction != null)
			{
				s.Add((byte)((sbyte)Direction));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Id
			byte tmp6;
			tmp6 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp6 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Direction
			byte tmp7;
			tmp7 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp7 == 1)
			{
				sbyte tmp8;
				tmp8 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Direction = (ECommandDirection)tmp8;
			}
			else
				Direction = null;
			
			return offset;
		}
	}
} // namespace KS.Commands
