from collections import deque, defaultdict
from typing import TypeVar, Set, DefaultDict, Deque

T = TypeVar('T')


def add_double_link_to_graph(graph: DefaultDict[T, T], item1: T, item2: T) -> None:
    graph[item1].add(item2)
    graph[item2].add(item1)


if __name__ == '__main__':
    friends: DefaultDict[str, str] = defaultdict(set)
    enemies: DefaultDict[str, str] = defaultdict(set)

    for observation in open('./etterretningsrapport.txt'):
        relation_type, name1, name2 = observation.strip().split(' ')
        if relation_type == 'fiendskap':
            add_double_link_to_graph(enemies, name1, name2)
        else:
            add_double_link_to_graph(friends, name1, name2)

    my_friends: Set[str] = {'Asgeir'}
    my_enemies: Set[str] = {'Beate'}

    queue: Deque = deque(['Asgeir', 'Beate'])
    already_analyzed: Set[str] = set()

    while queue:
        person_we_are_analyzing: str = queue.popleft()

        if person_we_are_analyzing in already_analyzed:
            continue

        enemies_of_person: Set[str] = enemies[person_we_are_analyzing]
        friends_of_person: Set[str] = friends[person_we_are_analyzing]

        queue.extend(enemies_of_person - already_analyzed)
        queue.extend(friends_of_person - already_analyzed)

        if person_we_are_analyzing in my_enemies:
            my_friends |= enemies_of_person
            my_enemies |= friends_of_person

        else:
            my_friends |= friends_of_person
            my_enemies |= enemies_of_person

        already_analyzed.add(person_we_are_analyzing)

    neutral_people = (set(friends) | set(enemies)) - my_friends - my_enemies
    print(len(my_friends), len(my_enemies), len(neutral_people))
