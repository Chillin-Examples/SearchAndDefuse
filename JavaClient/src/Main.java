import team.koala.chillin.client.GameClient;
import ai.AI;
import ks.KSObject;
import ks.models.*;

import java.io.IOException;


public class Main {

	private static String configPath = System.getProperty("user.dir") + "/";
	private static String configFile = "gamecfg.json";


	public static void main(String[] args) throws IOException {
		if (args.length > 0)
			configPath += args[0];
		else
			configPath += configFile;

		KSObject world = new World();
		AI ai = new AI((World) world);

		GameClient app = new GameClient(configPath, args);
		app.registerAI(ai);
		app.run();
	}
}
