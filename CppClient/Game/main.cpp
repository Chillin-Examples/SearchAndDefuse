#include <QCoreApplication>

#include <ChillinClient>

#include "ai.h"
#include "ks/models.h"

using namespace koala::chillin::client;
using namespace ks::models;


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    World world;
    AI ai = AI(&world);
    GameClient gc;

    gc.registerAI(&ai);
    gc.run();

    //return a.exec();
}
