package ks.models;

import java.lang.*;
import java.util.*;
import java.nio.*;
import java.nio.charset.Charset;

import ks.KSObject;

public class World extends KSObject
{
	protected Integer width;
	protected Integer height;
	protected List<List<ECell>> board;
	protected Map<String, Float> scores;
	protected List<Bomb> bombs;
	protected List<Terrorist> terrorists;
	protected List<Police> polices;
	protected Constants constants;
	
	// getters
	
	public Integer getWidth()
	{
		return this.width;
	}
	
	public Integer getHeight()
	{
		return this.height;
	}
	
	public List<List<ECell>> getBoard()
	{
		return this.board;
	}
	
	public Map<String, Float> getScores()
	{
		return this.scores;
	}
	
	public List<Bomb> getBombs()
	{
		return this.bombs;
	}
	
	public List<Terrorist> getTerrorists()
	{
		return this.terrorists;
	}
	
	public List<Police> getPolices()
	{
		return this.polices;
	}
	
	public Constants getConstants()
	{
		return this.constants;
	}
	
	
	// setters
	
	public void setWidth(Integer width)
	{
		this.width = width;
	}
	
	public void setHeight(Integer height)
	{
		this.height = height;
	}
	
	public void setBoard(List<List<ECell>> board)
	{
		this.board = board;
	}
	
	public void setScores(Map<String, Float> scores)
	{
		this.scores = scores;
	}
	
	public void setBombs(List<Bomb> bombs)
	{
		this.bombs = bombs;
	}
	
	public void setTerrorists(List<Terrorist> terrorists)
	{
		this.terrorists = terrorists;
	}
	
	public void setPolices(List<Police> polices)
	{
		this.polices = polices;
	}
	
	public void setConstants(Constants constants)
	{
		this.constants = constants;
	}
	
	
	public World()
	{
	}
	
	public static final String nameStatic = "World";
	
	@Override
	public String name() { return "World"; }
	
	@Override
	public byte[] serialize()
	{
		List<Byte> s = new ArrayList<>();
		
		// serialize width
		s.add((byte) ((width == null) ? 0 : 1));
		if (width != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(width).array()));
		}
		
		// serialize height
		s.add((byte) ((height == null) ? 0 : 1));
		if (height != null)
		{
			s.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(height).array()));
		}
		
		// serialize board
		s.add((byte) ((board == null) ? 0 : 1));
		if (board != null)
		{
			List<Byte> tmp0 = new ArrayList<>();
			tmp0.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(board.size()).array()));
			while (tmp0.size() > 0 && tmp0.get(tmp0.size() - 1) == 0)
				tmp0.remove(tmp0.size() - 1);
			s.add((byte) tmp0.size());
			s.addAll(tmp0);
			
			for (List<ECell> tmp1 : board)
			{
				s.add((byte) ((tmp1 == null) ? 0 : 1));
				if (tmp1 != null)
				{
					List<Byte> tmp2 = new ArrayList<>();
					tmp2.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp1.size()).array()));
					while (tmp2.size() > 0 && tmp2.get(tmp2.size() - 1) == 0)
						tmp2.remove(tmp2.size() - 1);
					s.add((byte) tmp2.size());
					s.addAll(tmp2);
					
					for (ECell tmp3 : tmp1)
					{
						s.add((byte) ((tmp3 == null) ? 0 : 1));
						if (tmp3 != null)
						{
							s.add((byte) (tmp3.getValue()));
						}
					}
				}
			}
		}
		
		// serialize scores
		s.add((byte) ((scores == null) ? 0 : 1));
		if (scores != null)
		{
			List<Byte> tmp4 = new ArrayList<>();
			tmp4.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(scores.size()).array()));
			while (tmp4.size() > 0 && tmp4.get(tmp4.size() - 1) == 0)
				tmp4.remove(tmp4.size() - 1);
			s.add((byte) tmp4.size());
			s.addAll(tmp4);
			
			for (Map.Entry<String, Float> tmp5 : scores.entrySet())
			{
				s.add((byte) ((tmp5.getKey() == null) ? 0 : 1));
				if (tmp5.getKey() != null)
				{
					List<Byte> tmp6 = new ArrayList<>();
					tmp6.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(tmp5.getKey().length()).array()));
					while (tmp6.size() > 0 && tmp6.get(tmp6.size() - 1) == 0)
						tmp6.remove(tmp6.size() - 1);
					s.add((byte) tmp6.size());
					s.addAll(tmp6);
					
					s.addAll(b2B(tmp5.getKey().getBytes(Charset.forName("ISO-8859-1"))));
				}
				
				s.add((byte) ((tmp5.getValue() == null) ? 0 : 1));
				if (tmp5.getValue() != null)
				{
					s.addAll(b2B(ByteBuffer.allocate(Float.BYTES).order(ByteOrder.LITTLE_ENDIAN).putFloat(tmp5.getValue()).array()));
				}
			}
		}
		
		// serialize bombs
		s.add((byte) ((bombs == null) ? 0 : 1));
		if (bombs != null)
		{
			List<Byte> tmp7 = new ArrayList<>();
			tmp7.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(bombs.size()).array()));
			while (tmp7.size() > 0 && tmp7.get(tmp7.size() - 1) == 0)
				tmp7.remove(tmp7.size() - 1);
			s.add((byte) tmp7.size());
			s.addAll(tmp7);
			
			for (Bomb tmp8 : bombs)
			{
				s.add((byte) ((tmp8 == null) ? 0 : 1));
				if (tmp8 != null)
				{
					s.addAll(b2B(tmp8.serialize()));
				}
			}
		}
		
		// serialize terrorists
		s.add((byte) ((terrorists == null) ? 0 : 1));
		if (terrorists != null)
		{
			List<Byte> tmp9 = new ArrayList<>();
			tmp9.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(terrorists.size()).array()));
			while (tmp9.size() > 0 && tmp9.get(tmp9.size() - 1) == 0)
				tmp9.remove(tmp9.size() - 1);
			s.add((byte) tmp9.size());
			s.addAll(tmp9);
			
			for (Terrorist tmp10 : terrorists)
			{
				s.add((byte) ((tmp10 == null) ? 0 : 1));
				if (tmp10 != null)
				{
					s.addAll(b2B(tmp10.serialize()));
				}
			}
		}
		
		// serialize polices
		s.add((byte) ((polices == null) ? 0 : 1));
		if (polices != null)
		{
			List<Byte> tmp11 = new ArrayList<>();
			tmp11.addAll(b2B(ByteBuffer.allocate(Integer.BYTES).order(ByteOrder.LITTLE_ENDIAN).putInt(polices.size()).array()));
			while (tmp11.size() > 0 && tmp11.get(tmp11.size() - 1) == 0)
				tmp11.remove(tmp11.size() - 1);
			s.add((byte) tmp11.size());
			s.addAll(tmp11);
			
			for (Police tmp12 : polices)
			{
				s.add((byte) ((tmp12 == null) ? 0 : 1));
				if (tmp12 != null)
				{
					s.addAll(b2B(tmp12.serialize()));
				}
			}
		}
		
		// serialize constants
		s.add((byte) ((constants == null) ? 0 : 1));
		if (constants != null)
		{
			s.addAll(b2B(constants.serialize()));
		}
		
		return B2b(s);
	}
	
	@Override
	protected int deserialize(byte[] s, int offset)
	{
		// deserialize width
		byte tmp13;
		tmp13 = s[offset];
		offset += Byte.BYTES;
		if (tmp13 == 1)
		{
			width = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			width = null;
		
		// deserialize height
		byte tmp14;
		tmp14 = s[offset];
		offset += Byte.BYTES;
		if (tmp14 == 1)
		{
			height = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			offset += Integer.BYTES;
		}
		else
			height = null;
		
		// deserialize board
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
			
			board = new ArrayList<>();
			for (int tmp19 = 0; tmp19 < tmp18; tmp19++)
			{
				List<ECell> tmp20;
				byte tmp21;
				tmp21 = s[offset];
				offset += Byte.BYTES;
				if (tmp21 == 1)
				{
					byte tmp22;
					tmp22 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp23 = Arrays.copyOfRange(s, offset, offset + tmp22);
					offset += tmp22;
					int tmp24;
					tmp24 = ByteBuffer.wrap(Arrays.copyOfRange(tmp23, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp20 = new ArrayList<>();
					for (int tmp25 = 0; tmp25 < tmp24; tmp25++)
					{
						ECell tmp26;
						byte tmp27;
						tmp27 = s[offset];
						offset += Byte.BYTES;
						if (tmp27 == 1)
						{
							byte tmp28;
							tmp28 = s[offset];
							offset += Byte.BYTES;
							tmp26 = ECell.of(tmp28);
						}
						else
							tmp26 = null;
						tmp20.add(tmp26);
					}
				}
				else
					tmp20 = null;
				board.add(tmp20);
			}
		}
		else
			board = null;
		
		// deserialize scores
		byte tmp29;
		tmp29 = s[offset];
		offset += Byte.BYTES;
		if (tmp29 == 1)
		{
			byte tmp30;
			tmp30 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp31 = Arrays.copyOfRange(s, offset, offset + tmp30);
			offset += tmp30;
			int tmp32;
			tmp32 = ByteBuffer.wrap(Arrays.copyOfRange(tmp31, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			scores = new HashMap<>();
			for (int tmp33 = 0; tmp33 < tmp32; tmp33++)
			{
				String tmp34;
				byte tmp36;
				tmp36 = s[offset];
				offset += Byte.BYTES;
				if (tmp36 == 1)
				{
					byte tmp37;
					tmp37 = s[offset];
					offset += Byte.BYTES;
					byte[] tmp38 = Arrays.copyOfRange(s, offset, offset + tmp37);
					offset += tmp37;
					int tmp39;
					tmp39 = ByteBuffer.wrap(Arrays.copyOfRange(tmp38, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
					
					tmp34 = new String(s, offset, tmp39, Charset.forName("ISO-8859-1"));
					offset += tmp39;
				}
				else
					tmp34 = null;
				
				Float tmp35;
				byte tmp40;
				tmp40 = s[offset];
				offset += Byte.BYTES;
				if (tmp40 == 1)
				{
					tmp35 = ByteBuffer.wrap(Arrays.copyOfRange(s, offset, offset + Float.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getFloat();
					offset += Float.BYTES;
				}
				else
					tmp35 = null;
				
				scores.put(tmp34, tmp35);
			}
		}
		else
			scores = null;
		
		// deserialize bombs
		byte tmp41;
		tmp41 = s[offset];
		offset += Byte.BYTES;
		if (tmp41 == 1)
		{
			byte tmp42;
			tmp42 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp43 = Arrays.copyOfRange(s, offset, offset + tmp42);
			offset += tmp42;
			int tmp44;
			tmp44 = ByteBuffer.wrap(Arrays.copyOfRange(tmp43, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			bombs = new ArrayList<>();
			for (int tmp45 = 0; tmp45 < tmp44; tmp45++)
			{
				Bomb tmp46;
				byte tmp47;
				tmp47 = s[offset];
				offset += Byte.BYTES;
				if (tmp47 == 1)
				{
					tmp46 = new Bomb();
					offset = tmp46.deserialize(s, offset);
				}
				else
					tmp46 = null;
				bombs.add(tmp46);
			}
		}
		else
			bombs = null;
		
		// deserialize terrorists
		byte tmp48;
		tmp48 = s[offset];
		offset += Byte.BYTES;
		if (tmp48 == 1)
		{
			byte tmp49;
			tmp49 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp50 = Arrays.copyOfRange(s, offset, offset + tmp49);
			offset += tmp49;
			int tmp51;
			tmp51 = ByteBuffer.wrap(Arrays.copyOfRange(tmp50, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			terrorists = new ArrayList<>();
			for (int tmp52 = 0; tmp52 < tmp51; tmp52++)
			{
				Terrorist tmp53;
				byte tmp54;
				tmp54 = s[offset];
				offset += Byte.BYTES;
				if (tmp54 == 1)
				{
					tmp53 = new Terrorist();
					offset = tmp53.deserialize(s, offset);
				}
				else
					tmp53 = null;
				terrorists.add(tmp53);
			}
		}
		else
			terrorists = null;
		
		// deserialize polices
		byte tmp55;
		tmp55 = s[offset];
		offset += Byte.BYTES;
		if (tmp55 == 1)
		{
			byte tmp56;
			tmp56 = s[offset];
			offset += Byte.BYTES;
			byte[] tmp57 = Arrays.copyOfRange(s, offset, offset + tmp56);
			offset += tmp56;
			int tmp58;
			tmp58 = ByteBuffer.wrap(Arrays.copyOfRange(tmp57, 0, 0 + Integer.BYTES)).order(ByteOrder.LITTLE_ENDIAN).getInt();
			
			polices = new ArrayList<>();
			for (int tmp59 = 0; tmp59 < tmp58; tmp59++)
			{
				Police tmp60;
				byte tmp61;
				tmp61 = s[offset];
				offset += Byte.BYTES;
				if (tmp61 == 1)
				{
					tmp60 = new Police();
					offset = tmp60.deserialize(s, offset);
				}
				else
					tmp60 = null;
				polices.add(tmp60);
			}
		}
		else
			polices = null;
		
		// deserialize constants
		byte tmp62;
		tmp62 = s[offset];
		offset += Byte.BYTES;
		if (tmp62 == 1)
		{
			constants = new Constants();
			offset = constants.deserialize(s, offset);
		}
		else
			constants = null;
		
		return offset;
	}
}
