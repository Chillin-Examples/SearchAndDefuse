package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public enum ECell
{
	Empty((byte) 0),
	SmallBombSite((byte) 1),
	MediumBombSite((byte) 2),
	LargeBombSite((byte) 3),
	VastBombSite((byte) 4),
	Wall((byte) 5),
	;

	private final byte value;
	ECell(byte value) { this.value = value; }
	public byte getValue() { return value; }
	
	private static Map<Byte, ECell> reverseLookup;
	
	public static ECell of(byte value)
	{
		if (reverseLookup == null)
		{
			reverseLookup = new HashMap<>();
			for (ECell c : ECell.values())
				reverseLookup.put(c.getValue(), c);
		}
		return reverseLookup.get(value);
	}
}
