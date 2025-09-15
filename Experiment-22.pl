% --- Knowledge Base ---
% bird(Name, CanFly).

bird(sparrow, yes).
bird(pigeon, yes).
bird(crow, yes).
bird(eagle, yes).
bird(parrot, yes).
bird(owl, yes).
bird(penguin, no).
bird(ostrich, no).
bird(kiwi, no).
bird(emperor_penguin, no).

% --- Rule ---
% can_fly(Bird) - Prints whether the bird can fly or not.

can_fly(Bird) :-
    bird(Bird, yes),
    write(Bird), write(' can fly.'), nl.

can_fly(Bird) :-
    bird(Bird, no),
    write(Bird), write(' cannot fly.'), nl.
