% --- Knowledge Base ---
% adb(Name, DOB).
adb('John', '12-05-2000').
adb('Alice', '23-09-1998').
adb('Bob', '15-01-2002').
adb('Triveni', '13-09-2004').

% --- Rules ---
% find_dob(Name, DOB) - Finds the DOB of a given person.
find_dob(Name, DOB) :-
    adb(Name, DOB).

% find_name(DOB, Name) - Finds the person with a given DOB.
find_name(DOB, Name) :-
    adb(Name, DOB).
