from model import *





class MyStrategy:
    def __init__(self):
        pass

    def game_param(self, game_r):
        print(f'Мой индекс - {game_r.my_index}\n'
              f'Максимальное количество летящих групп роботов одного игрока - {game_r.max_flying_worker_groups}\n'
              f'Максимальная дистанция скачка - {game_r.max_travel_distance}\n'
              f'Максимальное количество строителей - {game_r.max_builders}')

    def build_prop(self, game_r):
        for i in BuildingType:
            # Всего параметров 10
            print(f'\n{i.name}\n'
                  f'Максимум жизней - {game_r.building_properties[i].max_health}\n'
                  f'Максимум рабочих - {game_r.building_properties[i].max_workers}\n'
                  f'Ресурсы для строительства - {game_r.building_properties[i].build_resources}\n'
                  f'?Добыча? - {game_r.building_properties[i].harvest}\n'
                  f'?Работы требуется? - {game_r.building_properties[i].work_amount}\n'
                  f'?Ресурсов требуется? - {game_r.building_properties[i].work_resources}\n'
                  f'?Количество продукции - {game_r.building_properties[i].produce_amount}\n'
                  f'? - {game_r.building_properties[i].produce_resource}\n'
                  f'? - {game_r.building_properties[i].produce_score}\n'
                  f'?Производит рабочих - {game_r.building_properties[i].produce_worker}')

    def get_action(self, game: Game) -> Action:
        moves = []
        builds = []
        self.game_param(game)
        self.build_prop(game)




        return Action(moves, builds)
