from model import *
from math import dist

cost = True


class MyStrategy:
    def __init__(self):
        pass

    '''
    Примитивная стратегия, которая пытается застроить всю карту каменоломнями и получать очки за добычу камня.
    Смотри подсказки по ее улучшению, оформленные в виде специальных комментариев: # TODO ...
    '''
    black_list_planet = []
    foundry_list_planet = []
    furnace_list_planet  = []
    bioreactor_list_planet = []
    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        global planet_index, planet_index_order
        resource_planets = []
        stone_planets = []
        ore_planets = []
        organic_planets = []
        sand_planets = []
        for x, i in enumerate(game.planets):
            if i.harvestable_resource == Resource.STONE:
                resource_planets.append(x)
                stone_planets.append(x)
            elif i.harvestable_resource == Resource.ORE:
                resource_planets.append(x)
                ore_planets.append(x)
            elif i.harvestable_resource == Resource.ORGANICS:
                resource_planets.append(x)
                organic_planets.append(x)
            elif i.harvestable_resource == Resource.SAND:
                resource_planets.append(x)
                sand_planets.append(x)
        try:
            if game.planets[0].resources[Resource.STONE] > 149:
                print("Провервка")
        except KeyError:
            print("Хуч")
        else:
            print(game.planets[0].resources)
            if game.planets[0].resources[Resource.STONE] > 149:

                mill = 1110000000000000000000
                for x, i in enumerate(resource_planets):
                    if not i in self.black_list_planet:
                        rast = dist((game.planets[i].x, game.planets[i].y,), (0, 0))
                        print(f"Дистанция {rast}")
                        print(f"ПРошлая дистация: {mill}")
                        if rast < mill:
                            mill = rast
                            planet_index = i
                            list_del_index = x
                            print(f"АХахаххаха: {list_del_index}")
                            planet = game.planets[i]
                moves.append(MoveAction(0, planet_index, 50, Resource.STONE))
                self.black_list_planet.append(planet_index)




                mill = 1110000000000000000000
                for x, i in enumerate(game.planets):
                    if not i.id in self.black_list_planet :
                        i = i.id
                        print(i)
                        rast = dist((game.planets[i].x, game.planets[i].y,), (game.planets[planet_index].x, game.planets[planet_index].y))
                        print(f"Дистанция {rast}")
                        print(f"ПРошлая дистация: {mill}")
                        if rast < mill:
                            mill = rast
                            planet_index_order = i
                            planet = game.planets[i]

                            print(planet_index_order)
                moves.append(MoveAction(0, planet_index_order, 100, Resource.STONE))
                print(f"\ОРден: {planet_index_order}")

                self.black_list_planet.append(planet_index)
                print(self.black_list_planet)
                print(builds)
                match game.planets[planet_index].harvestable_resource:
                    case Resource.ORE:
                        self.foundry_list_planet.append(planet_index_order)
                    case Resource.SAND:
                        self.furnace_list_planet.append(planet_index_order)
                    case Resource.ORGANICS:
                        self.bioreactor_list_planet.append(planet_index_order)


        for i in self.black_list_planet:

            planet = game.planets[i]
            match planet.harvestable_resource:
                case Resource.STONE:
                    builds.append(BuildingAction(i, BuildingType.QUARRY))
                case Resource.ORE:
                    builds.append(BuildingAction(i, BuildingType.MINES))
                case Resource.SAND:
                    builds.append(BuildingAction(i, BuildingType.CAREER))
                case Resource.ORGANICS:
                    builds.append(BuildingAction(i, BuildingType.FARM))
        for i in self.foundry_list_planet:
            builds.append(BuildingAction(i, BuildingType.FOUNDRY))
        for i in self.furnace_list_planet:
            builds.append(BuildingAction(i, BuildingType.FURNACE))
        for i in self.bioreactor_list_planet:
            builds.append(BuildingAction(i, BuildingType.BIOREACTOR))
        print(self.bioreactor_list_planet)
        print(self.furnace_list_planet)
        print(self.foundry_list_planet)

        return Action(moves, builds, None)
