#ifndef AI_H
#define AI_H

#include <ChillinClient>

#include "ks/models.h"
#include "ks/commands.h"


class AI : public koala::chillin::client::RealtimeAI<ks::models::World*>
{
public:
    AI(ks::models::World *world);
    ~AI();

    void initialize();
    void decide();
    void sendCommand(ks::KSObject *command);

    void move(int agentId, ks::commands::ECommandDirection moveDirection);
    void plant(int agentId, ks::commands::ECommandDirection bombsiteDirection);
    void defuse(int agentId, ks::commands::ECommandDirection bombsiteDirection);
};

#endif // AI_H
