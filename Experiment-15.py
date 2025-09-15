# id3_decision_tree.py
import math
from collections import Counter, defaultdict

# Sample dataset (categorical features)
data = [
    {'Age':'young',  'Income':'low',    'Student':'no',  'Credit':'fair',      'Label':'No'},
    {'Age':'young',  'Income':'low',    'Student':'no',  'Credit':'excellent', 'Label':'No'},
    {'Age':'middle', 'Income':'low',    'Student':'no',  'Credit':'fair',      'Label':'Yes'},
    {'Age':'old',    'Income':'high',   'Student':'no',  'Credit':'fair',      'Label':'Yes'},
    {'Age':'old',    'Income':'high',   'Student':'yes', 'Credit':'excellent', 'Label':'Yes'},
    {'Age':'middle', 'Income':'medium', 'Student':'yes', 'Credit':'excellent', 'Label':'Yes'}
]

features = ['Age', 'Income', 'Student', 'Credit']

# Entropy
def entropy(examples):
    total = len(examples)
    counts = Counter(e['Label'] for e in examples)
    ent = 0.0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent

# Information gain for a feature
def info_gain(examples, feature):
    base = entropy(examples)
    total = len(examples)
    groups = defaultdict(list)
    for e in examples:
        groups[e[feature]].append(e)
    remainder = 0.0
    for subset in groups.values():
        remainder += (len(subset) / total) * entropy(subset)
    return base - remainder

# Majority label
def majority_label(examples):
    counts = Counter(e['Label'] for e in examples)
    return counts.most_common(1)[0][0]

# ID3 algorithm
def id3(examples, available_features):
    labels = [e['Label'] for e in examples]
    # If all labels same -> leaf
    if len(set(labels)) == 1:
        return labels[0]
    # If no features left -> majority
    if not available_features:
        return majority_label(examples)
    # Choose best feature
    gains = [(info_gain(examples, f), f) for f in available_features]
    gains.sort(reverse=True)
    best_gain, best_feature = gains[0]
    if best_gain == 0:
        return majority_label(examples)
    tree = {'feature': best_feature, 'nodes': {}, 'default': majority_label(examples)}
    # For each value of best_feature, build subtree
    values = set(e[best_feature] for e in examples)
    for v in values:
        subset = [e for e in examples if e[best_feature] == v]
        if not subset:
            tree['nodes'][v] = majority_label(examples)
        else:
            remaining = [f for f in available_features if f != best_feature]
            tree['nodes'][v] = id3(subset, remaining)
    return tree

# Classify with the tree
def classify(tree, instance):
    if isinstance(tree, str):
        return tree
    feature = tree['feature']
    val = instance.get(feature)
    if val in tree['nodes']:
        return classify(tree['nodes'][val], instance)
    else:
        return tree['default']

# Nicely print the tree
def pretty_print(tree, indent=""):
    if isinstance(tree, str):
        print(indent + "Label ->", tree)
        return
    print(indent + f"[{tree['feature']}] (default = {tree['default']})")
    for val, subtree in tree['nodes'].items():
        print(indent + f" -> {tree['feature']} = {val}:")
        pretty_print(subtree, indent + "     ")

# Build the tree
decision_tree = id3(data, features)

print("Learned Decision Tree:\n")
pretty_print(decision_tree)

# Test prediction
test_instance = {'Age':'old', 'Income':'medium', 'Student':'yes', 'Credit':'fair'}
prediction = classify(decision_tree, test_instance)
print("\nTest instance:", test_instance)
print("Predicted Label:", prediction)
