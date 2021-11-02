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
    black_list_planet = []  # Инициальзация global перменных
    foundry_list_planet = []
    furnace_list_planet = []
    bioreactor_list_planet = []
    ore_list_planet = []
    sand_list_planet = []
    organic_list_planet = []

    def get_action(self, game: Game) -> Action:
        moves = []  # Инициальзация local перменных
        builds = []
        global planet_index, planet_index_order
        resource_planets = []
        stone_planets = []
        ore_planets = []
        organic_planets = []
        sand_planets = []
        for x, i in enumerate(game.planets):  # Перебор Планет и добавления в local vars
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
        try:  # Проверка: Есть ли на планете камень в нужном количестве
            if game.planets[0].resources[Resource.STONE] > 149:
                print("Провервка")
        except KeyError:
            print("Хуч")
        else:  # Проверка если не было исключения KeyError
            print(game.planets[0].resources)
            if game.planets[0].resources[Resource.STONE] > 149:

                mill = 1110000000000000000000
                for x, i in enumerate(resource_planets):  # Расчёт растояний до планет с harvestable_resource
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
                moves.append(MoveAction(0, planet_index, 50, Resource.STONE))  # Полёт на ближаюшию планету с ресурсами
                self.black_list_planet.append(
                    planet_index)  # Добавление планеты в Black List что бы на неё не продолжали летать

                mill = 1110000000000000000000
                for x, i in enumerate(game.planets):  # Поиск ближайшей планеты для factory
                    if not i.id in self.black_list_planet:
                        i = i.id
                        print(i)
                        rast = dist((game.planets[i].x, game.planets[i].y,),
                                    (game.planets[planet_index].x, game.planets[planet_index].y))
                        print(f"Дистанция {rast}")
                        print(f"ПРошлая дистация: {mill}")
                        if rast < mill:
                            mill = rast
                            planet_index_order = i
                            planet = game.planets[i]

                            print(planet_index_order)
                moves.append(
                    MoveAction(0, planet_index_order, 100, Resource.STONE))  # Полёт на ближайшую планету для factory
                print(f"Planet For Building Factory: {planet_index_order}")

                self.black_list_planet.append(
                    planet_index)  # Добавление планеты в Black List что бы на неё не продолжали летать
                print(f"Black_List_planets: {self.black_list_planet}")
                if game.planets[planet_index].harvestable_resource == Resource.ORE:  # Добавление планет в глобальные
                    # списки
                    self.ore_list_planet.append([planet_index, planet_index_order])
                    self.foundry_list_planet.append([planet_index, planet_index_order])
                elif game.planets[planet_index].harvestable_resource == Resource.SAND:
                    self.sand_list_planet.append([planet_index, planet_index_order])
                    self.furnace_list_planet.append([planet_index, planet_index_order])
                elif game.planets[planet_index].harvestable_resource == Resource.ORGANICS:
                    self.organic_list_planet.append([planet_index, planet_index_order])
                    self.bioreactor_list_planet.append([planet_index, planet_index_order])

        for i in self.black_list_planet:  # Строительство на планетах с ресурсами Добываюших Зданий
            print(i)

            planet = game.planets[i]
            if planet.harvestable_resource == Resource.STONE:
                builds.append(BuildingAction(i, BuildingType.QUARRY))
            elif planet.harvestable_resource == Resource.ORE:
                builds.append(BuildingAction(i, BuildingType.MINES))
            elif planet.harvestable_resource == Resource.SAND:
                builds.append(BuildingAction(i, BuildingType.CAREER))
            elif planet.harvestable_resource == Resource.ORGANICS:
                builds.append(BuildingAction(i, BuildingType.FARM))
        for i in self.foundry_list_planet:  # Отправка Роботов на ближайшую планету с ресурсами(и со зданием для их
            # добычи) если их больше 100
            builds.append(BuildingAction(i[1], BuildingType.FOUNDRY))
            group_size = -1
            for y in game.planets[i[1]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            if group_size > 100:
                moves.append(MoveAction(i[1], i[0], group_size - 100, None))

        for i in self.furnace_list_planet:  # Отправка Роботов на ближайшую планету с ресурсами(и со зданием для их
            # добычи) если их больше 100
            builds.append(BuildingAction(i[1], BuildingType.FURNACE))
            group_size = -1
            for y in game.planets[i[1]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            if group_size > 100:
                moves.append(MoveAction(i[1], i[0], group_size - 100, None))
        for i in self.bioreactor_list_planet:  # Отправка Роботов на ближайшую планету с ресурсами(и со зданием для их
            # добычи) если их больше 100
            builds.append(BuildingAction(i[1], BuildingType.BIOREACTOR))
            group_size = -1
            for y in game.planets[i[1]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            if group_size > 100:
                moves.append(MoveAction(i[1], i[0], group_size - 100, None))
        for x, i in enumerate(self.ore_list_planet):  # Отправка роботов с ресурсами добытыми на планетах на ближайшие
            # заводы если их больше 1
            group_size = -1
            for y in game.planets[i[0]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            try:
                print(game.planets[i[0]].resources[Resource.ORE])
            except KeyError:
                print("Ore in Planet: Null")
            else:
                if group_size > 1 and game.planets[i[0]].resources[Resource.ORE] > 0:
                    moves.append(MoveAction(i[0], i[1], group_size - 1, Resource.ORE))
        for x, i in enumerate(self.sand_list_planet):  # Отправка роботов с ресурсами добытыми на планетах на ближайшие
            # заводы если их больше 1
            group_size = -1
            for y in game.planets[i[0]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            try:
                print(game.planets[i[0]].resources[Resource.SAND])
            except KeyError:
                print("SAND in Planet: Null")
            else:
                if group_size > 1 and game.planets[i[0]].resources[Resource.SAND] > 0:
                    moves.append(MoveAction(i[0], i[1], group_size - 1, Resource.SAND))
        for x, i in enumerate(
                self.organic_list_planet):  # Отправка роботов с ресурсами добытыми на планетах на ближайшие
            # заводы если их больше 1
            group_size = -1
            for y in game.planets[i[0]].worker_groups:
                print(group_size)
                if y.player_index == game.my_index:
                    group_size = y.number
            try:
                print(game.planets[i[0]].resources[Resource.ORGANICS])
            except KeyError:
                print("SAND in Planet: Null")
            else:
                if group_size > 1 and game.planets[i[0]].resources[Resource.ORGANICS] > 0:
                    moves.append(MoveAction(i[0], i[1], group_size - 1, Resource.ORGANICS))

        print(f"Bioreactor_List_planets: {self.bioreactor_list_planet}")  # Принты под конец
        print(f"Furnace_list_planets: {self.furnace_list_planet}")
        print(f"self.foundry_list_planet: {self.foundry_list_planet}")
        print(f"Builds:{builds}")
        print(f"Moves: {moves}")

        return Action(moves, builds, None)
