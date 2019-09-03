package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public enum EAgentStatus
{
	Alive((byte) 0),
	Dead((byte) 1),
	;

	private final byte value;
	EAgentStatus(byte value) { this.value = value; }
	public byte getValue() { return value; }
	
	private static Map<Byte, EAgentStatus> reverseLookup;
	
	public static EAgentStatus of(byte value)
	{
		if (reverseLookup == null)
		{
			reverseLookup = new HashMap<>();
			for (EAgentStatus c : EAgentStatus.values())
				reverseLookup.put(c.getValue(), c);
		}
		return reverseLookup.get(value);
	}
}
