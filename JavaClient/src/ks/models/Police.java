package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Police extends KSObject
{
	protected Integer id;
	protected Position position;
	protected Integer defusionRemainingTime;
	protected List<ESoundIntensity> footstepSounds;
	protected List<ESoundIntensity> bombSounds;
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
	
	public Integer getDefusionRemainingTime()
	{
		return this.defusionRemainingTime;
	}
	
	public List<ESoundIntensity> getFootstepSounds()
	{
		return this.footstepSounds;
	}
	
	public List<ESoundIntensity> getBombSounds()
	{
		return this.bombSounds;
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
	
	public void setDefusionRemainingTime(Integer defusionRemainingTime)
	{
		this.defusionRemainingTime = defusionRemainingTime;
	}
	
	public void setFootstepSounds(List<ESoundIntensity> footstepSounds)
	{
		this.footstepSounds = footstepSounds;
	}
	
	public void setBombSounds(List<ESoundIntensity> bombSounds)
	{
		this.bombSounds = bombSounds;
	}
	
	public void setStatus(EAgentStatus status)
	{
		this.status = status;
	}
	
	
	public Police()
	{
	}
	
	public static final String nameStatic = "Police";
	
	@Override
	public String name() { return "Police"; }
	
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
		
		// serialize defusionRemainingTime
		s.add((byte) ((defusionRemainingTime == null) ? 0 : 1));
		if (defusionRemainingTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(defusionRemainingTime).array()));
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
		
		// serialize bombSounds
		s.add((byte) ((bombSounds == null) ? 0 : 1));
		if (bombSounds != null)
		{
			List<Byte> tmp2 = new ArrayList<>();
			tmp2.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombSounds.size()).array()));
			while (tmp2.size() > 0 && tmp2.get(tmp2.size() - 1) == 0)
				tmp2.remove(tmp2.size() - 1);
			s.add((byte) tmp2.size());
			s.addAll(tmp2);
			
			for (ESoundIntensity tmp3 : bombSounds)
			{
				s.add((byte) ((tmp3 == null) ? 0 : 1));
				if (tmp3 != null)
				{
					s.add((byte) (tmp3.getValue()));
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
		byte tmp4;
		tmp4 = s[offset];
		offset += Byte.BYTES;
		if (tmp4 == 1)
		{
			id = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			id = null;
		
		// deserialize position
		byte tmp5;
		tmp5 = s[offset];
		offset += Byte.BYTES;
		if (tmp5 == 1)
		{
			position = new Position();
			offset = position.deserialize(s, offset);
		}
		else
			position = null;
		
		// deserialize defusionRemainingTime
		byte tmp6;
		tmp6 = s[offset];
		offset += Byte.BYTES;
		if (tmp6 == 1)
		{
			defusionRemainingTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			defusionRemainingTime = null;
		
		// deserialize footstepSounds
		byte tmp7;
		tmp7 = s[offset];
		offset += Byte.BYTES;
		if (tmp7 == 1)
		{
			byte tmp8;
			tmp8 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp9 = Arrays.copyOfRange(s, offset, offset + tmp8);
			offset += tmp8;
			int tmp10;
			tmp10 = ByteBuffer.wrap(Arrays.copyOfRange(tmp9, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			footstepSounds = new ArrayList<>();
			for (int tmp11 = 0; tmp11 < tmp10; tmp11++)
			{
				ESoundIntensity tmp12;
				byte tmp13;
				tmp13 = s[offset];
				offset += Byte.BYTES;
				if (tmp13 == 1)
				{
					byte tmp14;
					tmp14 = s[offset];
					offset += Byte.BYTES;
					tmp12 = ESoundIntensity.of(tmp14);
				}
				else
					tmp12 = null;
				footstepSounds.add(tmp12);
			}
		}
		else
			footstepSounds = null;
		
		// deserialize bombSounds
		byte tmp15;
		tmp15 = s[offset];
		offset += Byte.BYTES;
		if (tmp15 == 1)
		{
			byte tmp16;
			tmp16 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp17 = Arrays.copyOfRange(s, offset, offset + tmp16);
			offset += tmp16;
			int tmp18;
			tmp18 = ByteBuffer.wrap(Arrays.copyOfRange(tmp17, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			bombSounds = new ArrayList<>();
			for (int tmp19 = 0; tmp19 < tmp18; tmp19++)
			{
				ESoundIntensity tmp20;
				byte tmp21;
				tmp21 = s[offset];
				offset += Byte.BYTES;
				if (tmp21 == 1)
				{
					byte tmp22;
					tmp22 = s[offset];
					offset += Byte.BYTES;
					tmp20 = ESoundIntensity.of(tmp22);
				}
				else
					tmp20 = null;
				bombSounds.add(tmp20);
			}
		}
		else
			bombSounds = null;
		
		// deserialize status
		byte tmp23;
		tmp23 = s[offset];
		offset += Byte.BYTES;
		if (tmp23 == 1)
		{
			byte tmp24;
			tmp24 = s[offset];
			offset += Byte.BYTES;
			status = EAgentStatus.of(tmp24);
		}
		else
			status = null;
		
		return offset;
	}
}
