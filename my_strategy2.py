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

    def get_action(self, game: Game) -> Action:

        global planet_index
        moves = []
        builds = []
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
        mill = 1110000000000000000000
        for x, i in enumerate(resource_planets):
            if not i in self.black_list_planet:
                rast = dist((game.planets[i].x, game.planets[i].y,), (0, 0))
                print(f"Дистанция {rast}")
                if rast < mill:
                    mill = rast
                    planet_index = i
                    list_del_index = x
                    print(f"АХахаххаха: {list_del_index}")
                    planet = game.planets[i]
                    if game.planets[0].resources.STONE > 49:
                        self.black_list_planet.append(planet_index)
                        moves.append(MoveAction(0, planet_index, 50, Resource.STONE))
                    if planet.harvestable_resource == Resource.STONE:  # Строим каменоломлю если есть ресурс STONE
                        builds.append(BuildingAction(planet_index, BuildingType.QUARRY))
                    elif planet.harvestable_resource == Resource.ORE:  # Строим шахту если есть ресурс ORE
                        builds.append(BuildingAction(planet_index, BuildingType.MINES))
                    elif planet.harvestable_resource == Resource.SAND:  # Строим карьер если есть ресурс SAND
                        builds.append(BuildingAction(planet_index, BuildingType.CAREER))
                    elif planet.harvestable_resource == Resource.ORGANICS:
                        builds.append(BuildingAction(planet_index, BuildingType.FARM))
        print(self.black_list_planet)
        print(builds)

        print(f"Планеты с ресурсами: {resource_planets}")
        print(f"Планеты с камнем: {stone_planets}")
        print(f"Планеты с песком: {sand_planets}")
        print(f"Планеты с органикой: {organic_planets}")
        print(f"Планеты с рудой: {ore_planets}")
        for planet_index, planet in enumerate(game.planets):
            if planet.harvestable_resource == Resource.STONE:  # Строим каменоломлю если есть ресурс STONE
                builds.append(BuildingAction(planet_index, BuildingType.QUARRY))
            elif planet.harvestable_resource == Resource.ORE:  # Строим шахту если есть ресурс ORE
                builds.append(BuildingAction(planet_index, BuildingType.MINES))
            elif planet.harvestable_resource == Resource.SAND:  # Строим карьер если есть ресурс SAND
                builds.append(BuildingAction(planet_index, BuildingType.CAREER))
            elif planet.harvestable_resource == Resource.ORGANICS:
                builds.append(BuildingAction(planet_index, BuildingType.FARM))

        return Action(moves, builds)
