from model import *


class MyStrategy:
    def __init__(self):
        pass

    '''
    Примитивная стратегия, которая пытается застроить всю карту каменоломнями и получать очки за добычу камня.
    Смотри подсказки по ее улучшению, оформленные в виде специальных комментариев: # TODO ...
    '''

    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        # прочитать свойства здания "каменоломня"
        quarry_properties = game.building_properties[BuildingType.QUARRY]
        foundry_properties = game.building_properties[BuildingType.FOUNDRY]
        print(foundry_properties)

        # перебрать все планеты
        for planet_index, planet in enumerate(game.planets):

            PlanetResource = planet.harvestable_resource == Resource.ORE or planet.harvestable_resource == Resource.SAND or planet.harvestable_resource == Resource.STONE or planet.harvestable_resource == Resource.ORGANICS

            # попытаться построить каменоломню, ничего не проверяя (вдруг повезет)
            if planet.harvestable_resource == Resource.STONE:  # Строим каменоломлю если есть ресурс STONE
                builds.append(BuildingAction(planet_index, BuildingType.QUARRY))

                # TODO кстати, роботы могут быть заняты не только работой, но и строительством. См. game.max_builders
            elif planet.harvestable_resource == Resource.ORE:

                    # Строим шахту если есть ресурс ORE
                builds.append(BuildingAction(planet_index, BuildingType.MINES))
                next_planet_index = (planet_index + 1) % len(game.planets)
                moves.append(MoveAction(planet_index, next_planet_index, 100, Resource.STONE))
                builds.append(BuildingAction(next_planet_index, BuildingType.FOUNDRY))
            elif planet.harvestable_resource == Resource.SAND:  # Строим карьер если есть ресурс SAND
                builds.append(BuildingAction(planet_index, BuildingType.CAREER))
            elif planet.harvestable_resource == Resource.ORGANICS:
                builds.append(BuildingAction(planet_index, BuildingType.FARM))
            else:
                my_workers = sum(wg.number for wg in planet.worker_groups if wg.player_index == game.my_index)
                # Выбираем Бездельников
                if PlanetResource:
                    my_workers -= quarry_properties.max_workers
                next_planet_index = (planet_index + 1) % len(game.planets)  # выбрать следующую планету
                # TODO перебирать планеты по индексу - плохая идея, лучше искать близкие и пригодные для застройки
                if my_workers > 0 and (planet.building is not None or planet.harvestable_resource != Resource.STONE):
                    while True:
                        if not game.planets[next_planet_index].harvestable_resource is None:
                            send_count = 50
                            moves.append(MoveAction(planet_index, next_planet_index, send_count, Resource.STONE))
                            break
                        else:
                            next_planet_index += 1
                        # отправлять группами по количеству стройматериала, необходимого для постройки следующей каменоломни
            # подсчитать количество своих роботов на этой планете

            my_workers = sum(wg.number for wg in planet.worker_groups if wg.player_index == game.my_index)
            # Выбираем Бездельников
            if PlanetResource:
                my_workers -= quarry_properties.max_workers
            next_planet_index = (planet_index + 1) % len(game.planets)  # выбрать следующую планету
            # TODO перебирать планеты по индексу - плохая идея, лучше искать близкие и пригодные для застройки
            if my_workers > 0 and (planet.building is not None or planet.harvestable_resource != Resource.STONE):
                while True:
                    if not game.planets[next_planet_index].harvestable_resource is None:
                        send_count = 50
                        moves.append(MoveAction(planet_index, next_planet_index, send_count, Resource.STONE))
                        break
                    else:
                        next_planet_index += 1
                    # отправлять группами по количеству стройматериала, необходимого для постройки следующей каменоломни

        # сформировать ответ серверу
        return Action(moves, builds)
