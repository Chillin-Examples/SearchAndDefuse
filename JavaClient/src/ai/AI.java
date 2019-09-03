package ai;

import team.koala.chillin.client.RealtimeAI;
import ks.KSObject;
import ks.models.*;
import ks.commands.*;


public class AI extends RealtimeAI<World, KSObject> {

	public AI(World world) {
		super(world);
	}

	@Override
	public void initialize() {
		System.out.println("initialize");
	}

	@Override
	public void decide() {
		System.out.println("decide");

		if (this.mySide.equals("Police")) {
	        for (Police police : this.world.getPolices())
	        {
	            if (police.getStatus() == EAgentStatus.Dead)
	                continue;

	            boolean doingBombOperation = police.getDefusionRemainingTime() != -1;
	            if (doingBombOperation)
	            {
	                System.out.println("Agent[" + police.getId() + "]: " + "Continue Bomb Operation");
	                continue;
	            }

	            ECommandDirection bombsiteDirection = findBombsiteDirection(police.getPosition());
	            if (bombsiteDirection == null)
	            {
	            	System.out.println("Agent[" + police.getId() + "]: " + "Random Move");
	            	int randIndex = (int) (Math.random() * ECommandDirection.values().length);
	            	ECommandDirection randDir = ECommandDirection.values()[randIndex];
	                move(police.getId(), randDir);
	            }
	            else
	            {
	            	System.out.println("Agent[" + police.getId() + "]: " + "Start Bomb Operation");
	                defuse(police.getId(), bombsiteDirection);
	            }
	        }
	    }
	    else
	    {
	    	for (Terrorist terrorist : this.world.getTerrorists())
	        {
	            if (terrorist.getStatus() == EAgentStatus.Dead)
	                continue;

	            boolean doingBombOperation = terrorist.getPlantingRemainingTime() != -1;
	            if (doingBombOperation)
	            {
	                System.out.println("Agent[" + terrorist.getId() + "]: " + "Continue Bomb Operation");
	                continue;
	            }

	            ECommandDirection bombsiteDirection = findBombsiteDirection(terrorist.getPosition());
	            if (bombsiteDirection == null)
	            {
	            	System.out.println("Agent[" + terrorist.getId() + "]: " + "Random Move");
	            	int randIndex = (int) (Math.random() * ECommandDirection.values().length);
	            	ECommandDirection randDir = ECommandDirection.values()[randIndex];
	                move(terrorist.getId(), randDir);
	            }
	            else
	            {
	            	System.out.println("Agent[" + terrorist.getId() + "]: " + "Start Bomb Operation");
	                plant(terrorist.getId(), bombsiteDirection);
	            }
	        }
	    }
	}


	public void move(int agentId, ECommandDirection moveDirection)
	{
		this.sendCommand(new Move() {{ id = agentId; direction = moveDirection; }});
	}

	public void plant(int agentId, ECommandDirection bombsiteDirection)
	{
		this.sendCommand(new PlantBomb() {{ id = agentId; direction = bombsiteDirection; }});
	}

	public void defuse(int agentId, ECommandDirection bombsiteDirection)
	{
		this.sendCommand(new DefuseBomb() {{ id = agentId; direction = bombsiteDirection; }});
	}


	private ECommandDirection findBombsiteDirection(Position position)
	{
	    if ((this.world.getBoard().get(position.getY() - 1).get(position.getX()).getValue() >= ECell.SmallBombSite.getValue()) &&
	        (this.world.getBoard().get(position.getY() - 1).get(position.getX()).getValue() <= ECell.VastBombSite.getValue()))
	        return ECommandDirection.Up;

	    if ((this.world.getBoard().get(position.getY()).get(position.getX() + 1).getValue() >= ECell.SmallBombSite.getValue()) &&
	        (this.world.getBoard().get(position.getY()).get(position.getX() + 1).getValue() <= ECell.VastBombSite.getValue()))
	        return ECommandDirection.Right;
	
	    if ((this.world.getBoard().get(position.getY() + 1).get(position.getX()).getValue() >= ECell.SmallBombSite.getValue()) &&
	        (this.world.getBoard().get(position.getY() + 1).get(position.getX()).getValue() <= ECell.VastBombSite.getValue()))
	        return ECommandDirection.Down;
	
	    if ((this.world.getBoard().get(position.getY()).get(position.getX() - 1).getValue() >= ECell.SmallBombSite.getValue()) &&
	        (this.world.getBoard().get(position.getY()).get(position.getX() - 1).getValue() <= ECell.VastBombSite.getValue()))
	        return ECommandDirection.Left;
	
	    return null;
	}
}
