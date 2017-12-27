import typing
from math import radians, cos, sin, asin, sqrt

Coordinate = typing.Tuple[float, float]
Place = typing.List[str]


def max_possible_unique_round_trips_in_given_time_span(time_span_in_hours: float,
                                                       distances_from_origin: typing.List[float]) -> int:
    hours_used: float = 0
    places_visited: int = 0

    for distance in sorted(distances_from_origin):
        round_trip_time = 2 * hours_required_to_fly_distance_in_km_with_santas_sleigh(distance)
        hours_used_if_we_were_to_visit_this_place = hours_used + round_trip_time
        if hours_used_if_we_were_to_visit_this_place > time_span_in_hours:
            break
        hours_used = hours_used_if_we_were_to_visit_this_place
        places_visited += 1

    return places_visited


def hours_required_to_fly_distance_in_km_with_santas_sleigh(distance: float) -> float:
    sleigh_speed_in_km_per_h: float = 7274
    return distance / sleigh_speed_in_km_per_h


def get_capitals_from_place_list(place_list: typing.List[Place]) -> typing.List[Place]:
    place_type_column = 6
    capital_denominator = 'Hovedstad'

    def row_is_a_capital(row: Place) -> bool:
        return row[place_type_column] == capital_denominator

    return list(filter(row_is_a_capital, place_list))


def get_coordinates_from_place(place: Place) -> Coordinate:
    latitude_column, longitude_column = 12, 13
    latitude_as_float: float = float(place[latitude_column])
    longitude_as_float: float = float(place[longitude_column])
    return latitude_as_float, longitude_as_float


def get_distance_from_oslo_to_coordinate(other_place: Coordinate) -> float:
    oslo_coordinates = (59.911491, 10.757933)
    return get_distance_in_kilometers_from_two_decimal_degree_coordinates(oslo_coordinates, other_place)


def get_distance_in_kilometers_from_two_decimal_degree_coordinates(lat_lng1: Coordinate, lat_lng2: Coordinate):
    # Copyright 2016, Chris Youderian, SimpleMaps, http://simplemaps.com/resources/location-distance
    # Released under MIT license - https://opensource.org/licenses/MIT
    def haversine(c1: Coordinate, c2: Coordinate):
        lat1, lng1 = c1
        lat2, lng2 = c2
        lat1_as_radians: float = radians(lat1)
        lat2_as_radians: float = radians(lat2)
        lat_difference: float = lat2_as_radians - lat1_as_radians
        lng_difference: float = radians(lng2 - lng1)
        return sin(lat_difference / 2.0) ** 2 \
               + cos(lat1_as_radians) * cos(lat2_as_radians) * sin(lng_difference / 2.0) ** 2

    earth_radius_in_kilometers: float = 6371
    distance_in_kilometers: float = 2 * earth_radius_in_kilometers * asin(sqrt(haversine(lat_lng1, lat_lng2)))

    return distance_in_kilometers


if __name__ == '__main__':
    places: typing.List[Place] = [l.strip().split('\t') for l in open('./verda.txt', encoding='utf8')]

    coordinate_set: typing.Set[Coordinate] = set(
        [get_coordinates_from_place(l) for l in get_capitals_from_place_list(places)])

    distances = [get_distance_from_oslo_to_coordinate(c) for c in coordinate_set]

    print(max_possible_unique_round_trips_in_given_time_span(24, distances))
