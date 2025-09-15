% --- Knowledge Base ---
% Facts: parent(Parent, Child), male(Name), female(Name)

% --- Genders ---
male(john).
male(mike).
male(rahul).
male(ajay).

female(susan).
female(linda).
female(riya).
female(anjali).

% --- Parent Relationships ---
parent(john, mike).
parent(susan, mike).
parent(john, riya).
parent(susan, riya).
parent(mike, ajay).
parent(linda, ajay).
parent(mike, anjali).
parent(linda, anjali).

% --- Rules ---

% father(Father, Child)
father(Father, Child) :-
    parent(Father, Child),
    male(Father).

% mother(Mother, Child)
mother(Mother, Child) :-
    parent(Mother, Child),
    female(Mother).

% sibling(X, Y) - X and Y are siblings if they share at least one parent
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

% grandparent(GP, GC) - GP is grandparent of GC
grandparent(GP, GC) :-
    parent(GP, P),
    parent(P, GC).

% grandfather(GF, GC)
grandfather(GF, GC) :-
    grandparent(GF, GC),
    male(GF).

% grandmother(GM, GC)
grandmother(GM, GC) :-
    grandparent(GM, GC),
    female(GM).
