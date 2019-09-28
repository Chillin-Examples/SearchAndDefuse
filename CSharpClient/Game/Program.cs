using System;

using KoalaTeam.Chillin.Client;
using KS.Models;

namespace Game
{
	class Program
	{
		private static readonly string defaultConfigPath = "gamecfg.json";

		static void Main(string[] args)
		{
			var configPath = (args.Length > 0) ? args[0] : defaultConfigPath;

			var world = new World();
			AI ai = new AI(world);

			GameClient app = new GameClient(configPath);
			app.RegisterAI(ai);
			app.Run();
		}
	}
}
