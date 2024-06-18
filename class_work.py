from pprint import pprint
import requests
import json

# Итератор

class StarWarsСharacters:

    def __init__(self) -> None:
        pass

    def __iter__(self):
        self.next_link = 'https://swapi.py4e.com/api/people/'
        self.results = iter([]) # Инициализация пустого итератора
        return self

    def _get_results(self):
        response = requests.get(self.next_link).json()
        self.next_link = response['next']
        self.results = iter(response['results'])  # Создание итератора из результатов

    def  _get_item(self):
        try:
            item = next(self.results)  # Получение следующего элемента из итератора
        except StopIteration:
            item = None  # Если итератор пуст, возвращаем None
        return item


    def __next__(self):
        item = self._get_item()
        if item is None:
            if self.next_link is None:
                raise StopIteration  # Прекращаем итерацию, если нет следующей страницы
            self._get_results()
            item = self._get_item()  # Попробуем снова получить элемент после обновления результатов
        return item

    # def __next__(self):
    #     if len(self.results) == 0:
    #         if self.next_link is None:
    #             raise StopIteration
    #         self._get_results()
    #     return self.results.pop()


#  генератор

def get_link_StarWars():
    next_link = 'https://swapi.py4e.com/api/people/'

    while next_link:
        response = requests.get(next_link).json()
        next_link = response['next']
        results = response['results']
        for item in results:
            yield item

for item in get_link_StarWars():
    print(item)


star_wars = {}

for item in StarWarsСharacters():
    star_wars[item['name']] = item

# pprint(star_wars)

pprint({'R2-D2': star_wars['R2-D2']} if 'R2-D2' in star_wars else 'Такого персонажа нет')

# response = requests.get('https://swapi.py4e.com/api/people/').json()
# pprint(response)



