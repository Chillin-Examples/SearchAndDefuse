#include "ai.h"

#include <ctime>
#include <vector>
#include <iostream>

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
    srand(time(0));
}

AI::~AI()
{
    if (board)
    {
        for (int i = 0; i < world->height(); i++)
            delete[] board[i];
        delete[] board;
    }
}

void AI::initialize()
{
    cout << "initialize" << endl;
}

void AI::decide()
{
    cout << "decide" << endl;
}

int AI::getRandInt(int start, int end)
{
    return (rand() % (end - start + 1)) + start;
}


void AI::sendCommand(ks::KSObject *command)
{
    BaseAI::sendCommand(command);
}
