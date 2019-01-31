#include "ai.h"

#include <vector>
#include <iostream>

using namespace std;
using namespace koala::chillin::client;
using namespace ks::models;
using namespace ks::commands;


AI::AI(World *world): RealtimeAI<World*>(world)
{
}

AI::~AI()
{
}

void AI::initialize()
{
    cout << "initialize" << endl;
}

void AI::decide()
{
    cout << "decide" << endl;
}

void AI::sendCommand(ks::KSObject *command)
{
    BaseAI::sendCommand(command);
}

void AI::move(int agentId, ECommandDirection moveDirection)
{
    Move cmd;
    cmd.id(agentId);
    cmd.direction(moveDirection);
    this->sendCommand(&cmd);
}

void AI::plant(int agentId, ECommandDirection bombsiteDirection)
{
    PlantBomb cmd;
    cmd.id(agentId);
    cmd.direction(bombsiteDirection);
    this->sendCommand(&cmd);
}

void AI::defuse(int agentId, ECommandDirection bombsiteDirection)
{
    DefuseBomb cmd;
    cmd.id(agentId);
    cmd.direction(bombsiteDirection);
    this->sendCommand(&cmd);
}
