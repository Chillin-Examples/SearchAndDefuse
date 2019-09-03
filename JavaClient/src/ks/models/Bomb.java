package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Bomb extends KSObject
{
	protected Position position;
	protected Integer explosionRemainingTime;
	protected Integer planterId;
	protected Integer defuserId;
	
	// getters
	
	public Position getPosition()
	{
		return this.position;
	}
	
	public Integer getExplosionRemainingTime()
	{
		return this.explosionRemainingTime;
	}
	
	public Integer getPlanterId()
	{
		return this.planterId;
	}
	
	public Integer getDefuserId()
	{
		return this.defuserId;
	}
	
	
	// setters
	
	public void setPosition(Position position)
	{
		this.position = position;
	}
	
	public void setExplosionRemainingTime(Integer explosionRemainingTime)
	{
		this.explosionRemainingTime = explosionRemainingTime;
	}
	
	public void setPlanterId(Integer planterId)
	{
		this.planterId = planterId;
	}
	
	public void setDefuserId(Integer defuserId)
	{
		this.defuserId = defuserId;
	}
	
	
	public Bomb()
	{
	}
	
	public static final String nameStatic = "Bomb";
	
	@Override
	public String name() { return "Bomb"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize position
		s.add((byte) ((position == null) ? 0 : 1));
		if (position != null)
		{
			s.addAll(b2B(position.serialize()));
		}
		
		// serialize explosionRemainingTime
		s.add((byte) ((explosionRemainingTime == null) ? 0 : 1));
		if (explosionRemainingTime != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(explosionRemainingTime).array()));
		}
		
		// serialize planterId
		s.add((byte) ((planterId == null) ? 0 : 1));
		if (planterId != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(planterId).array()));
		}
		
		// serialize defuserId
		s.add((byte) ((defuserId == null) ? 0 : 1));
		if (defuserId != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(defuserId).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize position
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			position = new Position();
			offset = position.deserialize(s, offset);
		}
		else
			position = null;
		
		// deserialize explosionRemainingTime
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			explosionRemainingTime = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			explosionRemainingTime = null;
		
		// deserialize planterId
		byte tmp2;
		tmp2 = s[offset];
		offset += Byte.BYTES;
		if (tmp2 == 1)
		{
			planterId = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			planterId = null;
		
		// deserialize defuserId
		byte tmp3;
		tmp3 = s[offset];
		offset += Byte.BYTES;
		if (tmp3 == 1)
		{
			defuserId = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			defuserId = null;
		
		return offset;
	}
}
