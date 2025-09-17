/* 
Monkey and Banana Problem
Monkey wants to get the banana hanging from the ceiling.
Initial state:
- Monkey at door
- Box at window
- Monkey on floor
- Banana hanging
Goal: Monkey has banana
*/

/* --- Representation: state(MonkeyPosition, MonkeyOnBox?, BoxPosition, HasBanana?) --- */
/* MonkeyOnBox? = onfloor | onbox */
/* HasBanana? = has | hasnot */

/* --- Initial State --- */
initial_state(state(door, onfloor, window, hasnot)).

/* --- Goal State --- */
goal_state(state(_, _, _, has)).

/* --- Actions --- */
move(state(door, onfloor, Box, hasnot),
     state(middle, onfloor, Box, hasnot),
     'Monkey walks from door to middle').

move(state(window, onfloor, Box, hasnot),
     state(middle, onfloor, Box, hasnot),
     'Monkey walks from window to middle').

move(state(middle, onfloor, window, hasnot),
     state(middle, onfloor, middle, hasnot),
     'Monkey pushes box from window to middle').

move(state(middle, onfloor, middle, hasnot),
     state(middle, onbox, middle, hasnot),
     'Monkey climbs on box').

move(state(middle, onbox, middle, hasnot),
     state(middle, onbox, middle, has),
     'Monkey takes banana').

/* --- Plan to Get Banana --- */
plan(State, []) :- goal_state(State).

plan(State, [Action|Plan]) :-
    move(State, NextState, Action),
    plan(NextState, Plan).

solve :-
    initial_state(Initial),
    plan(Initial, Plan),
    write('Plan for Monkey to get Banana:'), nl,
    print_plan(Plan).

print_plan([]).
print_plan([Step|Rest]) :-
    write('- '), write(Step), nl,
    print_plan(Rest).
