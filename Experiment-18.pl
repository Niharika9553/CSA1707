% sum_n(N, Sum) - Sum is the sum of integers from 1 to N.

sum_n(0, 0).  % Base case: sum of numbers up to 0 is 0

sum_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_n(N1, PartialSum),
    Sum is PartialSum + N.
