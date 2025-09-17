% --- Knowledge Base: Diseases and Diet Suggestions ---
diet(diabetes, 'Eat high-fiber foods, avoid sugar, include whole grains, vegetables, and lean proteins.').
diet(hypertension, 'Follow a low-salt diet, include fruits, vegetables, low-fat dairy, and avoid processed foods.').
diet(obesity, 'Eat low-calorie foods, include more fruits and salads, avoid junk food and sugary drinks.').
diet(anemia, 'Eat iron-rich foods like spinach, beans, liver, and vitamin C-rich foods for better absorption.').
diet(heart_disease, 'Eat low-cholesterol foods, include oats, nuts, olive oil, fish, and avoid fried foods.').
diet(gastric_ulcer, 'Eat soft, non-spicy foods, drink milk, avoid coffee, alcohol, and very spicy dishes.').
diet(kidney_stone, 'Drink plenty of water, limit salt, avoid excessive animal protein, and include citrus fruits.').

% --- Rule to suggest diet ---
suggest_diet(Disease) :-
    diet(Disease, Suggestion),
    write('For '), write(Disease), write(', suggested diet: '), nl,
    write(Suggestion), nl.

% --- If disease not found ---
suggest_diet(Disease) :-
    \+ diet(Disease, _),
    write('No specific diet found for '), write(Disease), write('. Please consult a doctor.'), nl.
