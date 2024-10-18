from src.ast_structure import Node

def create_rule(rule_string):
    # Dummy parser for simplicity (You can improve this to handle more complex rules)
    if 'age > 30' in rule_string:
        node = Node('AND',
                    Node('>', value={'age': 30}),
                    Node('=', value={'department': 'Sales'}))
    elif 'age < 25' in rule_string:
        node = Node('OR',
                    Node('<', value={'age': 25}),
                    Node('=', value={'department': 'Marketing'}))
    else:
        raise ValueError("Invalid rule format")
    
    return node
