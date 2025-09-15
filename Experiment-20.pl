% --- Knowledge Base ---
% planet(Name, DistanceFromSun(MillionKm), Diameter(Km), NumberOfMoons).

planet('Mercury', 57.9, 4879, 0).
planet('Venus', 108.2, 12104, 0).
planet('Earth', 149.6, 12756, 1).
planet('Mars', 227.9, 6792, 2).
planet('Jupiter', 778.6, 142984, 79).
planet('Saturn', 1433.5, 120536, 82).
planet('Uranus', 2872.5, 51118, 27).
planet('Neptune', 4495.1, 49528, 14).

% --- Rules ---

% Find distance of a planet from the sun
find_distance(Planet, Distance) :-
    planet(Planet, Distance, _, _).

% Find number of moons of a planet
find_moons(Planet, Moons) :-
    planet(Planet, _, _, Moons).

% Find planets with more than N moons
planets_with_many_moons(N, Planet) :-
    planet(Planet, _, _, Moons),
    Moons > N.

% Find planets closer than a given distance from the Sun
planets_closer_than(Dist, Planet) :-
    planet(Planet, Distance, _, _),
    Distance < Dist.
