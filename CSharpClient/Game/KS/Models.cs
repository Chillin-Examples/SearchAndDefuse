using System;
using System.Linq;
using System.Collections.Generic;

namespace KS.Models
{
	public enum ECell
	{
		Empty = 0,
		SmallBombSite = 1,
		MediumBombSite = 2,
		LargeBombSite = 3,
		VastBombSite = 4,
		Wall = 5,
	}
	
	public enum ESoundIntensity
	{
		Weak = 0,
		Normal = 1,
		Strong = 2,
	}
	
	public enum EAgentStatus
	{
		Alive = 0,
		Dead = 1,
	}
	
	public partial class Constants : KSObject
	{
		public int? BombPlantingTime { get; set; }
		public int? BombDefusionTime { get; set; }
		public int? BombExplosionTime { get; set; }
		public int? BombPlantingScore { get; set; }
		public int? BombDefusionScore { get; set; }
		public int? BombExplosionScore { get; set; }
		public float? ScoreCoefficientSmallBombSite { get; set; }
		public float? ScoreCoefficientMediumBombSite { get; set; }
		public float? ScoreCoefficientLargeBombSite { get; set; }
		public float? ScoreCoefficientVastBombSite { get; set; }
		public int? TerroristVisionDistance { get; set; }
		public int? TerroristDeathScore { get; set; }
		public int? PoliceDeathScore { get; set; }
		public int? PoliceVisionDistance { get; set; }
		public Dictionary<ESoundIntensity?, int?> SoundRanges { get; set; }
		public int? MaxCycles { get; set; }
		

		public Constants()
		{
		}
		
		public new const string NameStatic = "Constants";
		
		public override string Name() => "Constants";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize BombPlantingTime
			s.Add((byte)((BombPlantingTime == null) ? 0 : 1));
			if (BombPlantingTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombPlantingTime));
			}
			
			// serialize BombDefusionTime
			s.Add((byte)((BombDefusionTime == null) ? 0 : 1));
			if (BombDefusionTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombDefusionTime));
			}
			
			// serialize BombExplosionTime
			s.Add((byte)((BombExplosionTime == null) ? 0 : 1));
			if (BombExplosionTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombExplosionTime));
			}
			
			// serialize BombPlantingScore
			s.Add((byte)((BombPlantingScore == null) ? 0 : 1));
			if (BombPlantingScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombPlantingScore));
			}
			
			// serialize BombDefusionScore
			s.Add((byte)((BombDefusionScore == null) ? 0 : 1));
			if (BombDefusionScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombDefusionScore));
			}
			
			// serialize BombExplosionScore
			s.Add((byte)((BombExplosionScore == null) ? 0 : 1));
			if (BombExplosionScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)BombExplosionScore));
			}
			
			// serialize ScoreCoefficientSmallBombSite
			s.Add((byte)((ScoreCoefficientSmallBombSite == null) ? 0 : 1));
			if (ScoreCoefficientSmallBombSite != null)
			{
				s.AddRange(BitConverter.GetBytes((float)ScoreCoefficientSmallBombSite));
			}
			
			// serialize ScoreCoefficientMediumBombSite
			s.Add((byte)((ScoreCoefficientMediumBombSite == null) ? 0 : 1));
			if (ScoreCoefficientMediumBombSite != null)
			{
				s.AddRange(BitConverter.GetBytes((float)ScoreCoefficientMediumBombSite));
			}
			
			// serialize ScoreCoefficientLargeBombSite
			s.Add((byte)((ScoreCoefficientLargeBombSite == null) ? 0 : 1));
			if (ScoreCoefficientLargeBombSite != null)
			{
				s.AddRange(BitConverter.GetBytes((float)ScoreCoefficientLargeBombSite));
			}
			
			// serialize ScoreCoefficientVastBombSite
			s.Add((byte)((ScoreCoefficientVastBombSite == null) ? 0 : 1));
			if (ScoreCoefficientVastBombSite != null)
			{
				s.AddRange(BitConverter.GetBytes((float)ScoreCoefficientVastBombSite));
			}
			
			// serialize TerroristVisionDistance
			s.Add((byte)((TerroristVisionDistance == null) ? 0 : 1));
			if (TerroristVisionDistance != null)
			{
				s.AddRange(BitConverter.GetBytes((int)TerroristVisionDistance));
			}
			
			// serialize TerroristDeathScore
			s.Add((byte)((TerroristDeathScore == null) ? 0 : 1));
			if (TerroristDeathScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)TerroristDeathScore));
			}
			
			// serialize PoliceDeathScore
			s.Add((byte)((PoliceDeathScore == null) ? 0 : 1));
			if (PoliceDeathScore != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PoliceDeathScore));
			}
			
			// serialize PoliceVisionDistance
			s.Add((byte)((PoliceVisionDistance == null) ? 0 : 1));
			if (PoliceVisionDistance != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PoliceVisionDistance));
			}
			
			// serialize SoundRanges
			s.Add((byte)((SoundRanges == null) ? 0 : 1));
			if (SoundRanges != null)
			{
				List<byte> tmp0 = new List<byte>();
				tmp0.AddRange(BitConverter.GetBytes((uint)SoundRanges.Count()));
				while (tmp0.Count > 0 && tmp0.Last() == 0)
					tmp0.RemoveAt(tmp0.Count - 1);
				s.Add((byte)tmp0.Count);
				s.AddRange(tmp0);
				
				foreach (var tmp1 in SoundRanges)
				{
					s.Add((byte)((tmp1.Key == null) ? 0 : 1));
					if (tmp1.Key != null)
					{
						s.Add((byte)((sbyte)tmp1.Key));
					}
					
					s.Add((byte)((tmp1.Value == null) ? 0 : 1));
					if (tmp1.Value != null)
					{
						s.AddRange(BitConverter.GetBytes((int)tmp1.Value));
					}
				}
			}
			
			// serialize MaxCycles
			s.Add((byte)((MaxCycles == null) ? 0 : 1));
			if (MaxCycles != null)
			{
				s.AddRange(BitConverter.GetBytes((int)MaxCycles));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize BombPlantingTime
			byte tmp2;
			tmp2 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp2 == 1)
			{
				BombPlantingTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombPlantingTime = null;
			
			// deserialize BombDefusionTime
			byte tmp3;
			tmp3 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp3 == 1)
			{
				BombDefusionTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombDefusionTime = null;
			
			// deserialize BombExplosionTime
			byte tmp4;
			tmp4 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp4 == 1)
			{
				BombExplosionTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombExplosionTime = null;
			
			// deserialize BombPlantingScore
			byte tmp5;
			tmp5 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp5 == 1)
			{
				BombPlantingScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombPlantingScore = null;
			
			// deserialize BombDefusionScore
			byte tmp6;
			tmp6 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp6 == 1)
			{
				BombDefusionScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombDefusionScore = null;
			
			// deserialize BombExplosionScore
			byte tmp7;
			tmp7 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp7 == 1)
			{
				BombExplosionScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				BombExplosionScore = null;
			
			// deserialize ScoreCoefficientSmallBombSite
			byte tmp8;
			tmp8 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp8 == 1)
			{
				ScoreCoefficientSmallBombSite = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				ScoreCoefficientSmallBombSite = null;
			
			// deserialize ScoreCoefficientMediumBombSite
			byte tmp9;
			tmp9 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp9 == 1)
			{
				ScoreCoefficientMediumBombSite = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				ScoreCoefficientMediumBombSite = null;
			
			// deserialize ScoreCoefficientLargeBombSite
			byte tmp10;
			tmp10 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp10 == 1)
			{
				ScoreCoefficientLargeBombSite = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				ScoreCoefficientLargeBombSite = null;
			
			// deserialize ScoreCoefficientVastBombSite
			byte tmp11;
			tmp11 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp11 == 1)
			{
				ScoreCoefficientVastBombSite = BitConverter.ToSingle(s, (int)offset);
				offset += sizeof(float);
			}
			else
				ScoreCoefficientVastBombSite = null;
			
			// deserialize TerroristVisionDistance
			byte tmp12;
			tmp12 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp12 == 1)
			{
				TerroristVisionDistance = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				TerroristVisionDistance = null;
			
			// deserialize TerroristDeathScore
			byte tmp13;
			tmp13 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp13 == 1)
			{
				TerroristDeathScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				TerroristDeathScore = null;
			
			// deserialize PoliceDeathScore
			byte tmp14;
			tmp14 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp14 == 1)
			{
				PoliceDeathScore = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PoliceDeathScore = null;
			
			// deserialize PoliceVisionDistance
			byte tmp15;
			tmp15 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp15 == 1)
			{
				PoliceVisionDistance = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PoliceVisionDistance = null;
			
			// deserialize SoundRanges
			byte tmp16;
			tmp16 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp16 == 1)
			{
				byte tmp17;
				tmp17 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp18 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp18, 0, tmp17);
				offset += tmp17;
				uint tmp19;
				tmp19 = BitConverter.ToUInt32(tmp18, (int)0);
				
				SoundRanges = new Dictionary<ESoundIntensity?, int?>();
				for (uint tmp20 = 0; tmp20 < tmp19; tmp20++)
				{
					ESoundIntensity? tmp21;
					byte tmp23;
					tmp23 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp23 == 1)
					{
						sbyte tmp24;
						tmp24 = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
						tmp21 = (ESoundIntensity)tmp24;
					}
					else
						tmp21 = null;
					
					int? tmp22;
					byte tmp25;
					tmp25 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp25 == 1)
					{
						tmp22 = BitConverter.ToInt32(s, (int)offset);
						offset += sizeof(int);
					}
					else
						tmp22 = null;
					
					SoundRanges[tmp21] = tmp22;
				}
			}
			else
				SoundRanges = null;
			
			// deserialize MaxCycles
			byte tmp26;
			tmp26 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp26 == 1)
			{
				MaxCycles = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				MaxCycles = null;
			
			return offset;
		}
	}
	
	public partial class Position : KSObject
	{
		public int? X { get; set; }
		public int? Y { get; set; }
		

		public Position()
		{
		}
		
		public new const string NameStatic = "Position";
		
		public override string Name() => "Position";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize X
			s.Add((byte)((X == null) ? 0 : 1));
			if (X != null)
			{
				s.AddRange(BitConverter.GetBytes((int)X));
			}
			
			// serialize Y
			s.Add((byte)((Y == null) ? 0 : 1));
			if (Y != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Y));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize X
			byte tmp27;
			tmp27 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp27 == 1)
			{
				X = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				X = null;
			
			// deserialize Y
			byte tmp28;
			tmp28 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp28 == 1)
			{
				Y = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Y = null;
			
			return offset;
		}
	}
	
	public partial class Bomb : KSObject
	{
		public Position Position { get; set; }
		public int? ExplosionRemainingTime { get; set; }
		public int? PlanterId { get; set; }
		public int? DefuserId { get; set; }
		

		public Bomb()
		{
		}
		
		public new const string NameStatic = "Bomb";
		
		public override string Name() => "Bomb";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Position
			s.Add((byte)((Position == null) ? 0 : 1));
			if (Position != null)
			{
				s.AddRange(Position.Serialize());
			}
			
			// serialize ExplosionRemainingTime
			s.Add((byte)((ExplosionRemainingTime == null) ? 0 : 1));
			if (ExplosionRemainingTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)ExplosionRemainingTime));
			}
			
			// serialize PlanterId
			s.Add((byte)((PlanterId == null) ? 0 : 1));
			if (PlanterId != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PlanterId));
			}
			
			// serialize DefuserId
			s.Add((byte)((DefuserId == null) ? 0 : 1));
			if (DefuserId != null)
			{
				s.AddRange(BitConverter.GetBytes((int)DefuserId));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Position
			byte tmp29;
			tmp29 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp29 == 1)
			{
				Position = new Position();
				offset = Position.Deserialize(s, offset);
			}
			else
				Position = null;
			
			// deserialize ExplosionRemainingTime
			byte tmp30;
			tmp30 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp30 == 1)
			{
				ExplosionRemainingTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				ExplosionRemainingTime = null;
			
			// deserialize PlanterId
			byte tmp31;
			tmp31 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp31 == 1)
			{
				PlanterId = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PlanterId = null;
			
			// deserialize DefuserId
			byte tmp32;
			tmp32 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp32 == 1)
			{
				DefuserId = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				DefuserId = null;
			
			return offset;
		}
	}
	
	public partial class Terrorist : KSObject
	{
		public int? Id { get; set; }
		public Position Position { get; set; }
		public int? PlantingRemainingTime { get; set; }
		public List<ESoundIntensity?> FootstepSounds { get; set; }
		public EAgentStatus? Status { get; set; }
		

		public Terrorist()
		{
		}
		
		public new const string NameStatic = "Terrorist";
		
		public override string Name() => "Terrorist";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			// serialize Position
			s.Add((byte)((Position == null) ? 0 : 1));
			if (Position != null)
			{
				s.AddRange(Position.Serialize());
			}
			
			// serialize PlantingRemainingTime
			s.Add((byte)((PlantingRemainingTime == null) ? 0 : 1));
			if (PlantingRemainingTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)PlantingRemainingTime));
			}
			
			// serialize FootstepSounds
			s.Add((byte)((FootstepSounds == null) ? 0 : 1));
			if (FootstepSounds != null)
			{
				List<byte> tmp33 = new List<byte>();
				tmp33.AddRange(BitConverter.GetBytes((uint)FootstepSounds.Count()));
				while (tmp33.Count > 0 && tmp33.Last() == 0)
					tmp33.RemoveAt(tmp33.Count - 1);
				s.Add((byte)tmp33.Count);
				s.AddRange(tmp33);
				
				foreach (var tmp34 in FootstepSounds)
				{
					s.Add((byte)((tmp34 == null) ? 0 : 1));
					if (tmp34 != null)
					{
						s.Add((byte)((sbyte)tmp34));
					}
				}
			}
			
			// serialize Status
			s.Add((byte)((Status == null) ? 0 : 1));
			if (Status != null)
			{
				s.Add((byte)((sbyte)Status));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Id
			byte tmp35;
			tmp35 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp35 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Position
			byte tmp36;
			tmp36 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp36 == 1)
			{
				Position = new Position();
				offset = Position.Deserialize(s, offset);
			}
			else
				Position = null;
			
			// deserialize PlantingRemainingTime
			byte tmp37;
			tmp37 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp37 == 1)
			{
				PlantingRemainingTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				PlantingRemainingTime = null;
			
			// deserialize FootstepSounds
			byte tmp38;
			tmp38 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp38 == 1)
			{
				byte tmp39;
				tmp39 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp40 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp40, 0, tmp39);
				offset += tmp39;
				uint tmp41;
				tmp41 = BitConverter.ToUInt32(tmp40, (int)0);
				
				FootstepSounds = new List<ESoundIntensity?>();
				for (uint tmp42 = 0; tmp42 < tmp41; tmp42++)
				{
					ESoundIntensity? tmp43;
					byte tmp44;
					tmp44 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp44 == 1)
					{
						sbyte tmp45;
						tmp45 = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
						tmp43 = (ESoundIntensity)tmp45;
					}
					else
						tmp43 = null;
					FootstepSounds.Add(tmp43);
				}
			}
			else
				FootstepSounds = null;
			
			// deserialize Status
			byte tmp46;
			tmp46 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp46 == 1)
			{
				sbyte tmp47;
				tmp47 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Status = (EAgentStatus)tmp47;
			}
			else
				Status = null;
			
			return offset;
		}
	}
	
	public partial class Police : KSObject
	{
		public int? Id { get; set; }
		public Position Position { get; set; }
		public int? DefusionRemainingTime { get; set; }
		public List<ESoundIntensity?> FootstepSounds { get; set; }
		public List<ESoundIntensity?> BombSounds { get; set; }
		public EAgentStatus? Status { get; set; }
		

		public Police()
		{
		}
		
		public new const string NameStatic = "Police";
		
		public override string Name() => "Police";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Id
			s.Add((byte)((Id == null) ? 0 : 1));
			if (Id != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Id));
			}
			
			// serialize Position
			s.Add((byte)((Position == null) ? 0 : 1));
			if (Position != null)
			{
				s.AddRange(Position.Serialize());
			}
			
			// serialize DefusionRemainingTime
			s.Add((byte)((DefusionRemainingTime == null) ? 0 : 1));
			if (DefusionRemainingTime != null)
			{
				s.AddRange(BitConverter.GetBytes((int)DefusionRemainingTime));
			}
			
			// serialize FootstepSounds
			s.Add((byte)((FootstepSounds == null) ? 0 : 1));
			if (FootstepSounds != null)
			{
				List<byte> tmp48 = new List<byte>();
				tmp48.AddRange(BitConverter.GetBytes((uint)FootstepSounds.Count()));
				while (tmp48.Count > 0 && tmp48.Last() == 0)
					tmp48.RemoveAt(tmp48.Count - 1);
				s.Add((byte)tmp48.Count);
				s.AddRange(tmp48);
				
				foreach (var tmp49 in FootstepSounds)
				{
					s.Add((byte)((tmp49 == null) ? 0 : 1));
					if (tmp49 != null)
					{
						s.Add((byte)((sbyte)tmp49));
					}
				}
			}
			
			// serialize BombSounds
			s.Add((byte)((BombSounds == null) ? 0 : 1));
			if (BombSounds != null)
			{
				List<byte> tmp50 = new List<byte>();
				tmp50.AddRange(BitConverter.GetBytes((uint)BombSounds.Count()));
				while (tmp50.Count > 0 && tmp50.Last() == 0)
					tmp50.RemoveAt(tmp50.Count - 1);
				s.Add((byte)tmp50.Count);
				s.AddRange(tmp50);
				
				foreach (var tmp51 in BombSounds)
				{
					s.Add((byte)((tmp51 == null) ? 0 : 1));
					if (tmp51 != null)
					{
						s.Add((byte)((sbyte)tmp51));
					}
				}
			}
			
			// serialize Status
			s.Add((byte)((Status == null) ? 0 : 1));
			if (Status != null)
			{
				s.Add((byte)((sbyte)Status));
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Id
			byte tmp52;
			tmp52 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp52 == 1)
			{
				Id = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Id = null;
			
			// deserialize Position
			byte tmp53;
			tmp53 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp53 == 1)
			{
				Position = new Position();
				offset = Position.Deserialize(s, offset);
			}
			else
				Position = null;
			
			// deserialize DefusionRemainingTime
			byte tmp54;
			tmp54 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp54 == 1)
			{
				DefusionRemainingTime = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				DefusionRemainingTime = null;
			
			// deserialize FootstepSounds
			byte tmp55;
			tmp55 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp55 == 1)
			{
				byte tmp56;
				tmp56 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp57 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp57, 0, tmp56);
				offset += tmp56;
				uint tmp58;
				tmp58 = BitConverter.ToUInt32(tmp57, (int)0);
				
				FootstepSounds = new List<ESoundIntensity?>();
				for (uint tmp59 = 0; tmp59 < tmp58; tmp59++)
				{
					ESoundIntensity? tmp60;
					byte tmp61;
					tmp61 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp61 == 1)
					{
						sbyte tmp62;
						tmp62 = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
						tmp60 = (ESoundIntensity)tmp62;
					}
					else
						tmp60 = null;
					FootstepSounds.Add(tmp60);
				}
			}
			else
				FootstepSounds = null;
			
			// deserialize BombSounds
			byte tmp63;
			tmp63 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp63 == 1)
			{
				byte tmp64;
				tmp64 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp65 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp65, 0, tmp64);
				offset += tmp64;
				uint tmp66;
				tmp66 = BitConverter.ToUInt32(tmp65, (int)0);
				
				BombSounds = new List<ESoundIntensity?>();
				for (uint tmp67 = 0; tmp67 < tmp66; tmp67++)
				{
					ESoundIntensity? tmp68;
					byte tmp69;
					tmp69 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp69 == 1)
					{
						sbyte tmp70;
						tmp70 = (sbyte)s[(int)offset];
						offset += sizeof(sbyte);
						tmp68 = (ESoundIntensity)tmp70;
					}
					else
						tmp68 = null;
					BombSounds.Add(tmp68);
				}
			}
			else
				BombSounds = null;
			
			// deserialize Status
			byte tmp71;
			tmp71 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp71 == 1)
			{
				sbyte tmp72;
				tmp72 = (sbyte)s[(int)offset];
				offset += sizeof(sbyte);
				Status = (EAgentStatus)tmp72;
			}
			else
				Status = null;
			
			return offset;
		}
	}
	
	public partial class World : KSObject
	{
		public int? Width { get; set; }
		public int? Height { get; set; }
		public List<List<ECell?>> Board { get; set; }
		public Dictionary<string, float?> Scores { get; set; }
		public List<Bomb> Bombs { get; set; }
		public List<Terrorist> Terrorists { get; set; }
		public List<Police> Polices { get; set; }
		public Constants Constants { get; set; }
		

		public World()
		{
		}
		
		public new const string NameStatic = "World";
		
		public override string Name() => "World";
		
		public override byte[] Serialize()
		{
			List<byte> s = new List<byte>();
			
			// serialize Width
			s.Add((byte)((Width == null) ? 0 : 1));
			if (Width != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Width));
			}
			
			// serialize Height
			s.Add((byte)((Height == null) ? 0 : 1));
			if (Height != null)
			{
				s.AddRange(BitConverter.GetBytes((int)Height));
			}
			
			// serialize Board
			s.Add((byte)((Board == null) ? 0 : 1));
			if (Board != null)
			{
				List<byte> tmp73 = new List<byte>();
				tmp73.AddRange(BitConverter.GetBytes((uint)Board.Count()));
				while (tmp73.Count > 0 && tmp73.Last() == 0)
					tmp73.RemoveAt(tmp73.Count - 1);
				s.Add((byte)tmp73.Count);
				s.AddRange(tmp73);
				
				foreach (var tmp74 in Board)
				{
					s.Add((byte)((tmp74 == null) ? 0 : 1));
					if (tmp74 != null)
					{
						List<byte> tmp75 = new List<byte>();
						tmp75.AddRange(BitConverter.GetBytes((uint)tmp74.Count()));
						while (tmp75.Count > 0 && tmp75.Last() == 0)
							tmp75.RemoveAt(tmp75.Count - 1);
						s.Add((byte)tmp75.Count);
						s.AddRange(tmp75);
						
						foreach (var tmp76 in tmp74)
						{
							s.Add((byte)((tmp76 == null) ? 0 : 1));
							if (tmp76 != null)
							{
								s.Add((byte)((sbyte)tmp76));
							}
						}
					}
				}
			}
			
			// serialize Scores
			s.Add((byte)((Scores == null) ? 0 : 1));
			if (Scores != null)
			{
				List<byte> tmp77 = new List<byte>();
				tmp77.AddRange(BitConverter.GetBytes((uint)Scores.Count()));
				while (tmp77.Count > 0 && tmp77.Last() == 0)
					tmp77.RemoveAt(tmp77.Count - 1);
				s.Add((byte)tmp77.Count);
				s.AddRange(tmp77);
				
				foreach (var tmp78 in Scores)
				{
					s.Add((byte)((tmp78.Key == null) ? 0 : 1));
					if (tmp78.Key != null)
					{
						List<byte> tmp79 = new List<byte>();
						tmp79.AddRange(BitConverter.GetBytes((uint)tmp78.Key.Count()));
						while (tmp79.Count > 0 && tmp79.Last() == 0)
							tmp79.RemoveAt(tmp79.Count - 1);
						s.Add((byte)tmp79.Count);
						s.AddRange(tmp79);
						
						s.AddRange(System.Text.Encoding.GetEncoding("ISO-8859-1").GetBytes(tmp78.Key));
					}
					
					s.Add((byte)((tmp78.Value == null) ? 0 : 1));
					if (tmp78.Value != null)
					{
						s.AddRange(BitConverter.GetBytes((float)tmp78.Value));
					}
				}
			}
			
			// serialize Bombs
			s.Add((byte)((Bombs == null) ? 0 : 1));
			if (Bombs != null)
			{
				List<byte> tmp80 = new List<byte>();
				tmp80.AddRange(BitConverter.GetBytes((uint)Bombs.Count()));
				while (tmp80.Count > 0 && tmp80.Last() == 0)
					tmp80.RemoveAt(tmp80.Count - 1);
				s.Add((byte)tmp80.Count);
				s.AddRange(tmp80);
				
				foreach (var tmp81 in Bombs)
				{
					s.Add((byte)((tmp81 == null) ? 0 : 1));
					if (tmp81 != null)
					{
						s.AddRange(tmp81.Serialize());
					}
				}
			}
			
			// serialize Terrorists
			s.Add((byte)((Terrorists == null) ? 0 : 1));
			if (Terrorists != null)
			{
				List<byte> tmp82 = new List<byte>();
				tmp82.AddRange(BitConverter.GetBytes((uint)Terrorists.Count()));
				while (tmp82.Count > 0 && tmp82.Last() == 0)
					tmp82.RemoveAt(tmp82.Count - 1);
				s.Add((byte)tmp82.Count);
				s.AddRange(tmp82);
				
				foreach (var tmp83 in Terrorists)
				{
					s.Add((byte)((tmp83 == null) ? 0 : 1));
					if (tmp83 != null)
					{
						s.AddRange(tmp83.Serialize());
					}
				}
			}
			
			// serialize Polices
			s.Add((byte)((Polices == null) ? 0 : 1));
			if (Polices != null)
			{
				List<byte> tmp84 = new List<byte>();
				tmp84.AddRange(BitConverter.GetBytes((uint)Polices.Count()));
				while (tmp84.Count > 0 && tmp84.Last() == 0)
					tmp84.RemoveAt(tmp84.Count - 1);
				s.Add((byte)tmp84.Count);
				s.AddRange(tmp84);
				
				foreach (var tmp85 in Polices)
				{
					s.Add((byte)((tmp85 == null) ? 0 : 1));
					if (tmp85 != null)
					{
						s.AddRange(tmp85.Serialize());
					}
				}
			}
			
			// serialize Constants
			s.Add((byte)((Constants == null) ? 0 : 1));
			if (Constants != null)
			{
				s.AddRange(Constants.Serialize());
			}
			
			return s.ToArray();
		}
		
		public override uint Deserialize(byte[] s, uint offset = 0)
		{
			// deserialize Width
			byte tmp86;
			tmp86 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp86 == 1)
			{
				Width = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Width = null;
			
			// deserialize Height
			byte tmp87;
			tmp87 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp87 == 1)
			{
				Height = BitConverter.ToInt32(s, (int)offset);
				offset += sizeof(int);
			}
			else
				Height = null;
			
			// deserialize Board
			byte tmp88;
			tmp88 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp88 == 1)
			{
				byte tmp89;
				tmp89 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp90 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp90, 0, tmp89);
				offset += tmp89;
				uint tmp91;
				tmp91 = BitConverter.ToUInt32(tmp90, (int)0);
				
				Board = new List<List<ECell?>>();
				for (uint tmp92 = 0; tmp92 < tmp91; tmp92++)
				{
					List<ECell?> tmp93;
					byte tmp94;
					tmp94 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp94 == 1)
					{
						byte tmp95;
						tmp95 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp96 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp96, 0, tmp95);
						offset += tmp95;
						uint tmp97;
						tmp97 = BitConverter.ToUInt32(tmp96, (int)0);
						
						tmp93 = new List<ECell?>();
						for (uint tmp98 = 0; tmp98 < tmp97; tmp98++)
						{
							ECell? tmp99;
							byte tmp100;
							tmp100 = (byte)s[(int)offset];
							offset += sizeof(byte);
							if (tmp100 == 1)
							{
								sbyte tmp101;
								tmp101 = (sbyte)s[(int)offset];
								offset += sizeof(sbyte);
								tmp99 = (ECell)tmp101;
							}
							else
								tmp99 = null;
							tmp93.Add(tmp99);
						}
					}
					else
						tmp93 = null;
					Board.Add(tmp93);
				}
			}
			else
				Board = null;
			
			// deserialize Scores
			byte tmp102;
			tmp102 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp102 == 1)
			{
				byte tmp103;
				tmp103 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp104 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp104, 0, tmp103);
				offset += tmp103;
				uint tmp105;
				tmp105 = BitConverter.ToUInt32(tmp104, (int)0);
				
				Scores = new Dictionary<string, float?>();
				for (uint tmp106 = 0; tmp106 < tmp105; tmp106++)
				{
					string tmp107;
					byte tmp109;
					tmp109 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp109 == 1)
					{
						byte tmp110;
						tmp110 = (byte)s[(int)offset];
						offset += sizeof(byte);
						byte[] tmp111 = new byte[sizeof(uint)];
						Array.Copy(s, offset, tmp111, 0, tmp110);
						offset += tmp110;
						uint tmp112;
						tmp112 = BitConverter.ToUInt32(tmp111, (int)0);
						
						tmp107 = System.Text.Encoding.GetEncoding("ISO-8859-1").GetString(s.Skip((int)offset).Take((int)tmp112).ToArray());
						offset += tmp112;
					}
					else
						tmp107 = null;
					
					float? tmp108;
					byte tmp113;
					tmp113 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp113 == 1)
					{
						tmp108 = BitConverter.ToSingle(s, (int)offset);
						offset += sizeof(float);
					}
					else
						tmp108 = null;
					
					Scores[tmp107] = tmp108;
				}
			}
			else
				Scores = null;
			
			// deserialize Bombs
			byte tmp114;
			tmp114 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp114 == 1)
			{
				byte tmp115;
				tmp115 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp116 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp116, 0, tmp115);
				offset += tmp115;
				uint tmp117;
				tmp117 = BitConverter.ToUInt32(tmp116, (int)0);
				
				Bombs = new List<Bomb>();
				for (uint tmp118 = 0; tmp118 < tmp117; tmp118++)
				{
					Bomb tmp119;
					byte tmp120;
					tmp120 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp120 == 1)
					{
						tmp119 = new Bomb();
						offset = tmp119.Deserialize(s, offset);
					}
					else
						tmp119 = null;
					Bombs.Add(tmp119);
				}
			}
			else
				Bombs = null;
			
			// deserialize Terrorists
			byte tmp121;
			tmp121 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp121 == 1)
			{
				byte tmp122;
				tmp122 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp123 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp123, 0, tmp122);
				offset += tmp122;
				uint tmp124;
				tmp124 = BitConverter.ToUInt32(tmp123, (int)0);
				
				Terrorists = new List<Terrorist>();
				for (uint tmp125 = 0; tmp125 < tmp124; tmp125++)
				{
					Terrorist tmp126;
					byte tmp127;
					tmp127 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp127 == 1)
					{
						tmp126 = new Terrorist();
						offset = tmp126.Deserialize(s, offset);
					}
					else
						tmp126 = null;
					Terrorists.Add(tmp126);
				}
			}
			else
				Terrorists = null;
			
			// deserialize Polices
			byte tmp128;
			tmp128 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp128 == 1)
			{
				byte tmp129;
				tmp129 = (byte)s[(int)offset];
				offset += sizeof(byte);
				byte[] tmp130 = new byte[sizeof(uint)];
				Array.Copy(s, offset, tmp130, 0, tmp129);
				offset += tmp129;
				uint tmp131;
				tmp131 = BitConverter.ToUInt32(tmp130, (int)0);
				
				Polices = new List<Police>();
				for (uint tmp132 = 0; tmp132 < tmp131; tmp132++)
				{
					Police tmp133;
					byte tmp134;
					tmp134 = (byte)s[(int)offset];
					offset += sizeof(byte);
					if (tmp134 == 1)
					{
						tmp133 = new Police();
						offset = tmp133.Deserialize(s, offset);
					}
					else
						tmp133 = null;
					Polices.Add(tmp133);
				}
			}
			else
				Polices = null;
			
			// deserialize Constants
			byte tmp135;
			tmp135 = (byte)s[(int)offset];
			offset += sizeof(byte);
			if (tmp135 == 1)
			{
				Constants = new Constants();
				offset = Constants.Deserialize(s, offset);
			}
			else
				Constants = null;
			
			return offset;
		}
	}
} // namespace KS.Models
