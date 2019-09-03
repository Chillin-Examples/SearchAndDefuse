package ks;

import java.lang.*;
import java.util.*;

public abstract class KSObject
{
	public static final String nameStatic = "";
	public abstract String name();
	public abstract byte[] serialize();
	public int deserialize(byte[] s) { return deserialize(s, 0); }
	protected abstract int deserialize(byte[] s, int offset);


	protected static List<Byte> b2B(byte[] bytes)
	{
		List<Byte> result = new ArrayList<>();
		for (byte b : bytes)
			result.add(b);
		return result;
	}

	protected static byte[] B2b(List<Byte> bytes)
	{
		byte[] result = new byte[bytes.size()];
		for(int i = 0; i < result.length; i++)
			result[i] = bytes.get(i);
		return result;
	}
}
