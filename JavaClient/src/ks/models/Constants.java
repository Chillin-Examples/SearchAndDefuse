package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Constants extends KSObject
{
	protected Integer bombPlantingTime;
	protected Integer bombDefusionTime;
	protected Integer bombExplosionTime;
	protected Integer bombPlantingScore;
	protected Integer bombDefusionScore;
	protected Integer bombExplosionScore;
	protected Float scoreCoefficientSmallBombSite;
	protected Float scoreCoefficientMediumBombSite;
	protected Float scoreCoefficientLargeBombSite;
	protected Float scoreCoefficientVastBombSite;
	protected Integer terroristVisionDistance;
	protected Integer terroristDeathScore;
	protected Integer policeDeathScore;
	protected Integer policeVisionDistance;
	protected Map<ESoundIntensity, Integer> soundRanges;
	protected Integer maxCycles;
	
	// getters
	
	public Integer getBombPlantingTime()
	{
		return this.bombPlantingTime;
	}
	
	public Integer getBombDefusionTime()
	{
		return this.bombDefusionTime;
	}
	
	public Integer getBombExplosionTime()
	{
		return this.bombExplosionTime;
	}
	
	public Integer getBombPlantingScore()
	{
		return this.bombPlantingScore;
	}
	
	public Integer getBombDefusionScore()
	{
		return this.bombDefusionScore;
	}
	
	public Integer getBombExplosionScore()
	{
		return this.bombExplosionScore;
	}
	
	public Float getScoreCoefficientSmallBombSite()
	{
		return this.scoreCoefficientSmallBombSite;
	}
	
	public Float getScoreCoefficientMediumBombSite()
	{
		return this.scoreCoefficientMediumBombSite;
	}
	
	public Float getScoreCoefficientLargeBombSite()
	{
		return this.scoreCoefficientLargeBombSite;
	}
	
	public Float getScoreCoefficientVastBombSite()
	{
		return this.scoreCoefficientVastBombSite;
	}
	
	public Integer getTerroristVisionDistance()
	{
		return this.terroristVisionDistance;
	}
	
	public Integer getTerroristDeathScore()
	{
		return this.terroristDeathScore;
	}
	
	public Integer getPoliceDeathScore()
	{
		return this.policeDeathScore;
	}
	
	public Integer getPoliceVisionDistance()
	{
		return this.policeVisionDistance;
	}
	
	public Map<ESoundIntensity, Integer> getSoundRanges()
	{
		return this.soundRanges;
	}
	
	public Integer getMaxCycles()
	{
		return this.maxCycles;
	}
	
	
	// setters
	
	public void setBombPlantingTime(Integer bombPlantingTime)
	{
		this.bombPlantingTime = bombPlantingTime;
	}
	
	public void setBombDefusionTime(Integer bombDefusionTime)
	{
		this.bombDefusionTime = bombDefusionTime;
	}
	
	public void setBombExplosionTime(Integer bombExplosionTime)
	{
		this.bombExplosionTime = bombExplosionTime;
	}
	
	public void setBombPlantingScore(Integer bombPlantingScore)
	{
		this.bombPlantingScore = bombPlantingScore;
	}
	
	public void setBombDefusionScore(Integer bombDefusionScore)
	{
		this.bombDefusionScore = bombDefusionScore;
	}
	
	public void setBombExplosionScore(Integer bombExplosionScore)
	{
		this.bombExplosionScore = bombExplosionScore;
	}
	
	public void setScoreCoefficientSmallBombSite(Float scoreCoefficientSmallBombSite)
	{
		this.scoreCoefficientSmallBombSite = scoreCoefficientSmallBombSite;
	}
	
	public void setScoreCoefficientMediumBombSite(Float scoreCoefficientMediumBombSite)
	{
		this.scoreCoefficientMediumBombSite = scoreCoefficientMediumBombSite;
	}
	
	public void setScoreCoefficientLargeBombSite(Float scoreCoefficientLargeBombSite)
	{
		this.scoreCoefficientLargeBombSite = scoreCoefficientLargeBombSite;
	}
	
	public void setScoreCoefficientVastBombSite(Float scoreCoefficientVastBombSite)
	{
		this.scoreCoefficientVastBombSite = scoreCoefficientVastBombSite;
	}
	
	public void setTerroristVisionDistance(Integer terroristVisionDistance)
	{
		this.terroristVisionDistance = terroristVisionDistance;
	}
	
	public void setTerroristDeathScore(Integer terroristDeathScore)
	{
		this.terroristDeathScore = terroristDeathScore;
	}
	
	public void setPoliceDeathScore(Integer policeDeathScore)
	{
		this.policeDeathScore = policeDeathScore;
	}
	
	public void setPoliceVisionDistance(Integer policeVisionDistance)
	{
		this.policeVisionDistance = policeVisionDistance;
	}
	
	public void setSoundRanges(Map<ESoundIntensity, Integer> soundRanges)
	{
		this.soundRanges = soundRanges;
	}
	
	public void setMaxCycles(Integer maxCycles)
	{
		this.maxCycles = maxCycles;
	}
	
	
	public Constants()
	{
	}
	
	public static final String nameStatic = "Constants";
	
	@Override
	public String name() { return "Constants"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize bombPlantingTime
		s.add((byte) ((bombPlantingTime == null) ? 0 : 1));
		if (bombPlantingTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombPlantingTime).array()));
		}
		
		// serialize bombDefusionTime
		s.add((byte) ((bombDefusionTime == null) ? 0 : 1));
		if (bombDefusionTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombDefusionTime).array()));
		}
		
		// serialize bombExplosionTime
		s.add((byte) ((bombExplosionTime == null) ? 0 : 1));
		if (bombExplosionTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombExplosionTime).array()));
		}
		
		// serialize bombPlantingScore
		s.add((byte) ((bombPlantingScore == null) ? 0 : 1));
		if (bombPlantingScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombPlantingScore).array()));
		}
		
		// serialize bombDefusionScore
		s.add((byte) ((bombDefusionScore == null) ? 0 : 1));
		if (bombDefusionScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombDefusionScore).array()));
		}
		
		// serialize bombExplosionScore
		s.add((byte) ((bombExplosionScore == null) ? 0 : 1));
		if (bombExplosionScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombExplosionScore).array()));
		}
		
		// serialize scoreCoefficientSmallBombSite
		s.add((byte) ((scoreCoefficientSmallBombSite == null) ? 0 : 1));
		if (scoreCoefficientSmallBombSite != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(scoreCoefficientSmallBombSite).array()));
		}
		
		// serialize scoreCoefficientMediumBombSite
		s.add((byte) ((scoreCoefficientMediumBombSite == null) ? 0 : 1));
		if (scoreCoefficientMediumBombSite != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(scoreCoefficientMediumBombSite).array()));
		}
		
		// serialize scoreCoefficientLargeBombSite
		s.add((byte) ((scoreCoefficientLargeBombSite == null) ? 0 : 1));
		if (scoreCoefficientLargeBombSite != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(scoreCoefficientLargeBombSite).array()));
		}
		
		// serialize scoreCoefficientVastBombSite
		s.add((byte) ((scoreCoefficientVastBombSite == null) ? 0 : 1));
		if (scoreCoefficientVastBombSite != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(scoreCoefficientVastBombSite).array()));
		}
		
		// serialize terroristVisionDistance
		s.add((byte) ((terroristVisionDistance == null) ? 0 : 1));
		if (terroristVisionDistance != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(terroristVisionDistance).array()));
		}
		
		// serialize terroristDeathScore
		s.add((byte) ((terroristDeathScore == null) ? 0 : 1));
		if (terroristDeathScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(terroristDeathScore).array()));
		}
		
		// serialize policeDeathScore
		s.add((byte) ((policeDeathScore == null) ? 0 : 1));
		if (policeDeathScore != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(policeDeathScore).array()));
		}
		
		// serialize policeVisionDistance
		s.add((byte) ((policeVisionDistance == null) ? 0 : 1));
		if (policeVisionDistance != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(policeVisionDistance).array()));
		}
		
		// serialize soundRanges
		s.add((byte) ((soundRanges == null) ? 0 : 1));
		if (soundRanges != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(soundRanges.size()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			for (Map.Entry<ESoundIntensity, Integer> tmp1 : soundRanges.entrySet())
			{
				s.add((byte) ((tmp1.getKey() == null) ? 0 : 1));
				if (tmp1.getKey() != null)
				{
					s.add((byte) (tmp1.getKey().getValue()));
				}
				
				s.add((byte) ((tmp1.getValue() == null) ? 0 : 1));
				if (tmp1.getValue() != null)
				{
					s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp1.getValue()).array()));
				}
			}
		}
		
		// serialize maxCycles
		s.add((byte) ((maxCycles == null) ? 0 : 1));
		if (maxCycles != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(maxCycles).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize bombPlantingTime
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			bombPlantingTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombPlantingTime = null;
		
		// deserialize bombDefusionTime
		byte tmp3;
		tmp3 = s[offset];
		offset += Byte.BYTES;
		if (tmp3 == 1)
		{
			bombDefusionTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombDefusionTime = null;
		
		// deserialize bombExplosionTime
		byte tmp4;
		tmp4 = s[offset];
		offset += Byte.BYTES;
		if (tmp4 == 1)
		{
			bombExplosionTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombExplosionTime = null;
		
		// deserialize bombPlantingScore
		byte tmp5;
		tmp5 = s[offset];
		offset += Byte.BYTES;
		if (tmp5 == 1)
		{
			bombPlantingScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombPlantingScore = null;
		
		// deserialize bombDefusionScore
		byte tmp6;
		tmp6 = s[offset];
		offset += Byte.BYTES;
		if (tmp6 == 1)
		{
			bombDefusionScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombDefusionScore = null;
		
		// deserialize bombExplosionScore
		byte tmp7;
		tmp7 = s[offset];
		offset += Byte.BYTES;
		if (tmp7 == 1)
		{
			bombExplosionScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			bombExplosionScore = null;
		
		// deserialize scoreCoefficientSmallBombSite
		byte tmp8;
		tmp8 = s[offset];
		offset += Byte.BYTES;
		if (tmp8 == 1)
		{
			scoreCoefficientSmallBombSite = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			scoreCoefficientSmallBombSite = null;
		
		// deserialize scoreCoefficientMediumBombSite
		byte tmp9;
		tmp9 = s[offset];
		offset += Byte.BYTES;
		if (tmp9 == 1)
		{
			scoreCoefficientMediumBombSite = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			scoreCoefficientMediumBombSite = null;
		
		// deserialize scoreCoefficientLargeBombSite
		byte tmp10;
		tmp10 = s[offset];
		offset += Byte.BYTES;
		if (tmp10 == 1)
		{
			scoreCoefficientLargeBombSite = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			scoreCoefficientLargeBombSite = null;
		
		// deserialize scoreCoefficientVastBombSite
		byte tmp11;
		tmp11 = s[offset];
		offset += Byte.BYTES;
		if (tmp11 == 1)
		{
			scoreCoefficientVastBombSite = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
			offset += Float.BYTES;
		}
		else
			scoreCoefficientVastBombSite = null;
		
		// deserialize terroristVisionDistance
		byte tmp12;
		tmp12 = s[offset];
		offset += Byte.BYTES;
		if (tmp12 == 1)
		{
			terroristVisionDistance = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			terroristVisionDistance = null;
		
		// deserialize terroristDeathScore
		byte tmp13;
		tmp13 = s[offset];
		offset += Byte.BYTES;
		if (tmp13 == 1)
		{
			terroristDeathScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			terroristDeathScore = null;
		
		// deserialize policeDeathScore
		byte tmp14;
		tmp14 = s[offset];
		offset += Byte.BYTES;
		if (tmp14 == 1)
		{
			policeDeathScore = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			policeDeathScore = null;
		
		// deserialize policeVisionDistance
		byte tmp15;
		tmp15 = s[offset];
		offset += Byte.BYTES;
		if (tmp15 == 1)
		{
			policeVisionDistance = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			policeVisionDistance = null;
		
		// deserialize soundRanges
		byte tmp16;
		tmp16 = s[offset];
		offset += Byte.BYTES;
		if (tmp16 == 1)
		{
			byte tmp17;
			tmp17 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp18 = Arrays.copyOfRange(s, offset, offset + tmp17);
			offset += tmp17;
			int tmp19;
			tmp19 = ByteBuffer.wrap(Arrays.copyOfRange(tmp18, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			soundRanges = new HashMap<>();
			for (int tmp20 = 0; tmp20 < tmp19; tmp20++)
			{
				ESoundIntensity tmp21;
				byte tmp23;
				tmp23 = s[offset];
				offset += Byte.BYTES;
				if (tmp23 == 1)
				{
					byte tmp24;
					tmp24 = s[offset];
					offset += Byte.BYTES;
					tmp21 = ESoundIntensity.of(tmp24);
				}
				else
					tmp21 = null;
				
				Integer tmp22;
				byte tmp25;
				tmp25 = s[offset];
				offset += Byte.BYTES;
				if (tmp25 == 1)
				{
					tmp22 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					offset += Integer.BYTES;
				}
				else
					tmp22 = null;
				
				soundRanges.put(tmp21, tmp22);
			}
		}
		else
			soundRanges = null;
		
		// deserialize maxCycles
		byte tmp26;
		tmp26 = s[offset];
		offset += Byte.BYTES;
		if (tmp26 == 1)
		{
			maxCycles = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			maxCycles = null;
		
		return offset;
	}
}
