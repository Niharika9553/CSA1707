% --- Towers of Hanoi Program ---
% hanoi(N, Source, Target, Auxiliary) - Solves the problem for N disks.

hanoi(1, Source, Target, _) :-
    write('Move disk 1 from '), write(Source),
    write(' to '), write(Target), nl.

hanoi(N, Source, Target, Auxiliary) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Auxiliary, Target),
    write('Move disk '), write(N),
    write(' from '), write(Source),
    write(' to '), write(Target), nl,
    hanoi(N1, Auxiliary, Target, Source).
