# -*- coding: utf-8 -*-

# python imports
from copy import deepcopy

# project imports
from ..helpers.logic.timers import bomb_timer
from ..helpers.logic import vision
from ..helpers.logic.sounds import bombbeep, footsteps
from ..ks.models import ECell, EAgentStatus
from ..gui_events import GuiEventType, GuiEvent


class LogicHandler:

    def __init__(self, world, sides):
        self.world = world
        self._sides = sides
        self._last_cycle_commands = {side: {} for side in self._sides}


    def store_command(self, side_name, command):
        agents = self.world.polices if side_name == 'Police' else self.world.terrorists

        # Dead Agents Should Not Be Removed From Agents List.
        if command.id < 0 or command.id >= len(agents):
            print('Invalid id in command: %s %i' % (side_name, command.id))
            return

        # Dead Agents can't send command
        if agents[command.id].status == EAgentStatus.Dead:
            print('%s(%i) is dead so can\'t send command' % (side_name, command.id))
            return

        print('command: %s(%i)' % (side_name, command.id))
        self._last_cycle_commands[side_name][command.id] = command


    def initialize(self):
        # initialize world vision
        self.world.visions['Police'] = vision.compute_polices_visions(self.world)
        self.world.visions['Terrorist'] = vision.compute_terrorists_visions(self.world)


    def clear_commands(self):
        self._last_cycle_commands = {side: {} for side in self._sides}


    def process(self, current_cycle):
        gui_events = []

        # Reset agents is moving
        self._reset_agents_is_moving()

        # Check timers
        gui_events += bomb_timer.update_bombs_timings(self.world)

        # Check commands
        for side in self._sides:
            for command_id in self._last_cycle_commands[side]:
                gui_events += self.world.apply_command(side, self._last_cycle_commands[side][command_id])

        # update polices visions
        self.world.visions['Police'] = vision.compute_polices_visions(self.world)

        # reset is_shooting
        for police in self.world.polices:
            if police.status == EAgentStatus.Alive:
                police.is_shooting = False

        # check death terrorist that are in police visions
        for terrorist in self.world.terrorists:
            if terrorist.status == EAgentStatus.Alive:
                not_shooting_police = None
                any_police = None

                # Find a police that see the terrorist
                for police in self.world.polices:
                    if police.status == EAgentStatus.Alive and any(terrorist.position == vision_position for vision_position in police.visions):
                        if any_police == None:
                            any_police = police
                        if not police.is_shooting:
                            police.is_shooting = True
                            not_shooting_police = police
                            gui_events.append(GuiEvent(GuiEventType.ShootTerrorist, police=police, terrorist=terrorist))
                            break

                if any_police != None:
                    killer = not_shooting_police if not_shooting_police != None else any_police
                    gui_events += terrorist.die(self.world, killer)

        # update bombs sound
        bombbeep.update_police_bomb_sounds(self.world)

        # update terrorists visions
        self.world.visions['Terrorist'] = vision.compute_terrorists_visions(self.world)

        # Update footsounds
        footsteps.update_police_intensities(self.world)
        footsteps.update_terrorist_intensities(self.world)

        return gui_events


    def _reset_agents_is_moving(self):
        for side in self._sides:
            agents = self.world.polices if side == 'Police' else self.world.terrorists

            for agent in agents:
                agent.is_moving = False


    def get_client_world(self, side_name):
        client_world = deepcopy(self.world)

        if side_name == 'Police':
            client_world.terrorists = []
            client_world.bombs = []
            for vision_position in self.world.visions['Police']:
                for bomb in self.world.bombs:
                    if bomb.explosion_remaining_time != -1 and bomb.position == vision_position:
                        client_world.bombs.append(bomb)

            return client_world

        elif side_name == 'Terrorist':
            client_world.polices = []
            for vision_position in self.world.visions['Terrorist']:
                for police in self.world.polices:
                    if police.position == vision_position:
                        client_world.polices.append(police)
            return client_world


    def check_end_game(self, current_cycle):
        end_game = False
        winner_sidename = None

        # count active bombs
        num_active_bombs = 0
        for bomb in self.world.bombs:
            if bomb.explosion_remaining_time != -1:
                num_active_bombs += 1

        # times up
        if current_cycle >= self.world.constants.max_cycles - 1:
            end_game = True

        # all bombsites exploded
        elif all(cell not in [ECell.SmallBombSite, ECell.MediumBombSite,
                              ECell.LargeBombSite, ECell.VastBombSite] for cell in sum(self.world.board, [])):
            end_game = True

        # all terrorists are dead and there is no active bomb
        elif num_active_bombs == 0 and all(terrorist.status == EAgentStatus.Dead for terrorist in self.world.terrorists):
            end_game = True

        # all polices are dead and there is no active bomb
        elif num_active_bombs == 0 and all(police.status == EAgentStatus.Dead for police in self.world.polices):
            end_game = True

        if self.world.scores['Police'] == self.world.scores['Terrorist']:
            winner_sidename = None
        else:
            winner_sidename = 'Police' if self.world.scores['Police'] > self.world.scores['Terrorist'] else 'Terrorist'

        details = {
            'Scores': {
                'Police': str(self.world.scores['Police']),
                'Terrorist': str(self.world.scores['Terrorist'])
            }
        }

        return end_game, winner_sidename, details
