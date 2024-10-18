from src.ast_structure import Node

def combine_rules(rules):
    if not rules:
        raise ValueError("No rules provided")
    
    root = rules[0]
    for rule in rules[1:]:
        root = Node('AND', left=root, right=rule)
    
    return root
