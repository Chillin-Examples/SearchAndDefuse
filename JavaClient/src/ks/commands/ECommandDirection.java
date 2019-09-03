package ks.commands;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public enum ECommandDirection
{
	Up((byte) 0),
	Right((byte) 1),
	Down((byte) 2),
	Left((byte) 3),
	;

	private final byte value;
	ECommandDirection(byte value) { this.value = value; }
	public byte getValue() { return value; }
	
	private static Map<Byte, ECommandDirection> reverseLookup;
	
	public static ECommandDirection of(byte value)
	{
		if (reverseLookup == null)
		{
			reverseLookup = new HashMap<>();
			for (ECommandDirection c : ECommandDirection.values())
				reverseLookup.put(c.getValue(), c);
		}
		return reverseLookup.get(value);
	}
}
