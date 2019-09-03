package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public enum ESoundIntensity
{
	Weak((byte) 0),
	Normal((byte) 1),
	Strong((byte) 2),
	;

	private final byte value;
	ESoundIntensity(byte value) { this.value = value; }
	public byte getValue() { return value; }
	
	private static Map<Byte, ESoundIntensity> reverseLookup;
	
	public static ESoundIntensity of(byte value)
	{
		if (reverseLookup == null)
		{
			reverseLookup = new HashMap<>();
			for (ESoundIntensity c : ESoundIntensity.values())
				reverseLookup.put(c.getValue(), c);
		}
		return reverseLookup.get(value);
	}
}
