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

    if (this->mySide == "Police")
    {
        for (int i = 0; i < this->world->ref_polices().size(); i++)
        {
            Police police = this->world->ref_polices()[i];
            if (police.status() == EAgentStatus::Dead)
                continue;

            bool doingBombOperation = police.defusionRemainingTime() != -1;
            if (doingBombOperation)
            {
                cout << "Agent[" << police.id() << "]: " << "Continue Bomb Operation" << endl;
                continue;
            }

            auto bombsiteDirection = findBombsiteDirection(police.position());
            if (std::get<0>(bombsiteDirection) == false)
            {
                cout << "Agent[" << police.id() << "]: " << "Random Move" << endl;
                move(police.id(), ECommandDirection::Left);
            }
            else
            {
                cout << "Agent[" << police.id() << "]: " << "Start Bomb Operation" << endl;
                defuse(police.id(), std::get<1>(bombsiteDirection));
            }
        }
    }
    else
    {
        for (int i = 0; i < this->world->ref_terrorists().size(); i++)
        {
            Terrorist terrorist = this->world->ref_terrorists()[i];
            if (terrorist.status() == EAgentStatus::Dead)
                continue;

            bool doingBombOperation = terrorist.plantingRemainingTime() != -1;
            if (doingBombOperation)
            {
                cout << "Agent[" << terrorist.id() << "]: " << "Continue Bomb Operation" << endl;
                continue;
            }

            auto bombsiteDirection = findBombsiteDirection(terrorist.position());
            if (std::get<0>(bombsiteDirection) == false)
            {
                cout << "Agent[" << terrorist.id() << "]: " << "Random Move" << endl;
                move(terrorist.id(), ECommandDirection::Down);
            }
            else
            {
                cout << "Agent[" << terrorist.id() << "]: " << "Start Bomb Operation" << endl;
                plant(terrorist.id(), std::get<1>(bombsiteDirection));
            }
        }
    }
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



std::tuple<bool, ECommandDirection> AI::findBombsiteDirection(Position position)
{
    if ((this->world->board()[position.y() - 1][position.x()] >= ECell::SmallBombSite) &&
        (this->world->board()[position.y() - 1][position.x()] <= ECell::VastBombSite))
        return std::make_tuple(true, ECommandDirection::Up);

    if ((this->world->board()[position.y()][position.x() + 1] >= ECell::SmallBombSite) &&
        (this->world->board()[position.y()][position.x() + 1] <= ECell::VastBombSite))
        return std::make_tuple(true, ECommandDirection::Right);

    if ((this->world->board()[position.y() + 1][position.x()] >= ECell::SmallBombSite) &&
        (this->world->board()[position.y() + 1][position.x()] <= ECell::VastBombSite))
        return std::make_tuple(true, ECommandDirection::Down);

    if ((this->world->board()[position.y()][position.x() - 1] >= ECell::SmallBombSite) &&
        (this->world->board()[position.y()][position.x() - 1] <= ECell::VastBombSite))
        return std::make_tuple(true, ECommandDirection::Left);

    return std::make_tuple(false, ECommandDirection::Up);
}
