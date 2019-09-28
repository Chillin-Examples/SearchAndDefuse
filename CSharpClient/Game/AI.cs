using System;

using KoalaTeam.Chillin.Client;
using KS;
using KS.Commands;
using KS.Models;

using KSObject = KS.KSObject;

namespace Game
{
	public class AI : RealtimeAI<World, KSObject>
	{
		private readonly Random random = new Random();

		public AI(World world) : base(world)
		{
		}

		public override void Initialize()
		{
			Console.WriteLine("initialize");
		}

		public override void Decide()
		{
			Console.WriteLine("decide");

			if (this.MySide == "Police")
			{
				foreach (var police in this.World.Polices)
				{
					if (police.Status == EAgentStatus.Dead)
						continue;

					bool doingBombOperation = police.DefusionRemainingTime != -1;
					if (doingBombOperation)
					{
						Console.WriteLine("Agent[" + police.Id + "]: " + "Continue Bomb Operation");
						continue;
					}

					ECommandDirection? bombsiteDirection = FindBombsiteDirection(police.Position);
					if (bombsiteDirection == null)
					{
						Console.WriteLine("Agent[" + police.Id + "]: " + "Random Move");
						var randDir = (ECommandDirection)random.Next(Enum.GetNames(typeof(ECommandDirection)).Length);
						Move(police.Id, randDir);
					}
					else
					{
						Console.WriteLine("Agent[" + police.Id + "]: " + "Start Bomb Operation");
						Defuse(police.Id, bombsiteDirection.Value);
					}
				}
			}
			else
			{
				foreach (var terrorist in this.World.Terrorists)
				{
					if (terrorist.Status == EAgentStatus.Dead)
						continue;

					bool doingBombOperation = terrorist.PlantingRemainingTime != -1;
					if (doingBombOperation)
					{
						Console.WriteLine("Agent[" + terrorist.Id + "]: " + "Continue Bomb Operation");
						continue;
					}

					ECommandDirection? bombsiteDirection = FindBombsiteDirection(terrorist.Position);
					if (bombsiteDirection == null)
					{
						Console.WriteLine("Agent[" + terrorist.Id + "]: " + "Random Move");
						var randDir = (ECommandDirection)random.Next(Enum.GetNames(typeof(ECommandDirection)).Length);
						Move(terrorist.Id, randDir);
					}
					else
					{
						Console.WriteLine("Agent[" + terrorist.Id + "]: " + "Start Bomb Operation");
						Plant(terrorist.Id, bombsiteDirection.Value);
					}
				}
			}
		}


		public void Move(int? agentId, ECommandDirection moveDirection)
		{
			this.SendCommand(new Move() { Id = agentId, Direction = moveDirection });
		}

		public void Plant(int? agentId, ECommandDirection bombsiteDirection)
		{
			this.SendCommand(new PlantBomb() { Id = agentId, Direction = bombsiteDirection });
		}

		public void Defuse(int? agentId, ECommandDirection bombsiteDirection)
		{
			this.SendCommand(new DefuseBomb() { Id = agentId, Direction = bombsiteDirection });
		}


		private ECommandDirection? FindBombsiteDirection(Position position)
		{
			if ((World.Board[(int)position.Y - 1][(int)position.X].Value >= ECell.SmallBombSite) &&
				(World.Board[(int)position.Y - 1][(int)position.X].Value <= ECell.VastBombSite))
				return ECommandDirection.Up;

			if ((World.Board[(int)position.Y][(int)position.X + 1].Value >= ECell.SmallBombSite) &&
				(World.Board[(int)position.Y][(int)position.X + 1].Value <= ECell.VastBombSite))
				return ECommandDirection.Right;

			if ((World.Board[(int)position.Y + 1][(int)position.X].Value >= ECell.SmallBombSite) &&
				(World.Board[(int)position.Y + 1][(int)position.X].Value <= ECell.VastBombSite))
				return ECommandDirection.Down;

			if ((World.Board[(int)position.Y][(int)position.X - 1].Value >= ECell.SmallBombSite) &&
				(World.Board[(int)position.Y][(int)position.X - 1].Value <= ECell.VastBombSite))
				return ECommandDirection.Left;

			return null;
		}
	}
}
