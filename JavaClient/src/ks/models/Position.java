package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Position extends KSObject
{
	protected Integer x;
	protected Integer y;
	
	// getters
	
	public Integer getX()
	{
		return this.x;
	}
	
	public Integer getY()
	{
		return this.y;
	}
	
	
	// setters
	
	public void setX(Integer x)
	{
		this.x = x;
	}
	
	public void setY(Integer y)
	{
		this.y = y;
	}
	
	
	public Position()
	{
	}
	
	public static final String nameStatic = "Position";
	
	@Override
	public String name() { return "Position"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize x
		s.add((byte) ((x == null) ? 0 : 1));
		if (x != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(x).array()));
		}
		
		// serialize y
		s.add((byte) ((y == null) ? 0 : 1));
		if (y != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(y).array()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize x
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			x = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			x = null;
		
		// deserialize y
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			y = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			y = null;
		
		return offset;
	}
}
