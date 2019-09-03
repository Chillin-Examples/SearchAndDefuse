package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Terrorist extends KSObject
{
	protected Integer id;
	protected Position position;
	protected Integer plantingRemainingTime;
	protected List<ESoundIntensity> footstepSounds;
	protected EAgentStatus status;
	
	// getters
	
	public Integer getId()
	{
		return this.id;
	}
	
	public Position getPosition()
	{
		return this.position;
	}
	
	public Integer getPlantingRemainingTime()
	{
		return this.plantingRemainingTime;
	}
	
	public List<ESoundIntensity> getFootstepSounds()
	{
		return this.footstepSounds;
	}
	
	public EAgentStatus getStatus()
	{
		return this.status;
	}
	
	
	// setters
	
	public void setId(Integer id)
	{
		this.id = id;
	}
	
	public void setPosition(Position position)
	{
		this.position = position;
	}
	
	public void setPlantingRemainingTime(Integer plantingRemainingTime)
	{
		this.plantingRemainingTime = plantingRemainingTime;
	}
	
	public void setFootstepSounds(List<ESoundIntensity> footstepSounds)
	{
		this.footstepSounds = footstepSounds;
	}
	
	public void setStatus(EAgentStatus status)
	{
		this.status = status;
	}
	
	
	public Terrorist()
	{
	}
	
	public static final String nameStatic = "Terrorist";
	
	@Override
	public String name() { return "Terrorist"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize id
		s.add((byte) ((id == null) ? 0 : 1));
		if (id != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(id).array()));
		}
		
		// serialize position
		s.add((byte) ((position == null) ? 0 : 1));
		if (position != null)
		{
			s.addAll(b2B(position.serialize()));
		}
		
		// serialize plantingRemainingTime
		s.add((byte) ((plantingRemainingTime == null) ? 0 : 1));
		if (plantingRemainingTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(plantingRemainingTime).array()));
		}
		
		// serialize footstepSounds
		s.add((byte) ((footstepSounds == null) ? 0 : 1));
		if (footstepSounds != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(footstepSounds.size()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			for (ESoundIntensity tmp1 : footstepSounds)
			{
				s.add((byte) ((tmp1 == null) ? 0 : 1));
				if (tmp1 != null)
				{
					s.add((byte) (tmp1.getValue()));
				}
			}
		}
		
		// serialize status
		s.add((byte) ((status == null) ? 0 : 1));
		if (status != null)
		{
			s.add((byte) (status.getValue()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize id
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			id = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			id = null;
		
		// deserialize position
		byte tmp3;
		tmp3 = s[offset];
		offset += Byte.BYTES;
		if (tmp3 == 1)
		{
			position = new Position();
			offset = position.deserialize(s, offset);
		}
		else
			position = null;
		
		// deserialize plantingRemainingTime
		byte tmp4;
		tmp4 = s[offset];
		offset += Byte.BYTES;
		if (tmp4 == 1)
		{
			plantingRemainingTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			plantingRemainingTime = null;
		
		// deserialize footstepSounds
		byte tmp5;
		tmp5 = s[offset];
		offset += Byte.BYTES;
		if (tmp5 == 1)
		{
			byte tmp6;
			tmp6 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp7 = Arrays.copyOfRange(s, offset, offset + tmp6);
			offset += tmp6;
			int tmp8;
			tmp8 = ByteBuffer.wrap(Arrays.copyOfRange(tmp7, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			footstepSounds = new ArrayList<>();
			for (int tmp9 = 0; tmp9 < tmp8; tmp9++)
			{
				ESoundIntensity tmp10;
				byte tmp11;
				tmp11 = s[offset];
				offset += Byte.BYTES;
				if (tmp11 == 1)
				{
					byte tmp12;
					tmp12 = s[offset];
					offset += Byte.BYTES;
					tmp10 = ESoundIntensity.of(tmp12);
				}
				else
					tmp10 = null;
				footstepSounds.add(tmp10);
			}
		}
		else
			footstepSounds = null;
		
		// deserialize status
		byte tmp13;
		tmp13 = s[offset];
		offset += Byte.BYTES;
		if (tmp13 == 1)
		{
			byte tmp14;
			tmp14 = s[offset];
			offset += Byte.BYTES;
			status = EAgentStatus.of(tmp14);
		}
		else
			status = null;
		
		return offset;
	}
}
