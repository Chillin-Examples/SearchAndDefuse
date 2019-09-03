package ks.commands;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class Move extends KSObject
{
	protected Integer id;
	protected ECommandDirection direction;
	
	// getters
	
	public Integer getId()
	{
		return this.id;
	}
	
	public ECommandDirection getDirection()
	{
		return this.direction;
	}
	
	
	// setters
	
	public void setId(Integer id)
	{
		this.id = id;
	}
	
	public void setDirection(ECommandDirection direction)
	{
		this.direction = direction;
	}
	
	
	public Move()
	{
	}
	
	public static final String nameStatic = "Move";
	
	@Override
	public String name() { return "Move"; }
	
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
		
		// serialize direction
		s.add((byte) ((direction == null) ? 0 : 1));
		if (direction != null)
		{
			s.add((byte) (direction.getValue()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize id
		byte tmp0;
		tmp0 = s[offset];
		offset += Byte.BYTES;
		if (tmp0 == 1)
		{
			id = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			id = null;
		
		// deserialize direction
		byte tmp1;
		tmp1 = s[offset];
		offset += Byte.BYTES;
		if (tmp1 == 1)
		{
			byte tmp2;
			tmp2 = s[offset];
			offset += Byte.BYTES;
			direction = ECommandDirection.of(tmp2);
		}
		else
			direction = null;
		
		return offset;
	}
}
