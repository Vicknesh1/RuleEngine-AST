def evaluate_rule(rule_ast, data):
    if rule_ast['type'] == 'AND':
        return evaluate_rule(rule_ast['left'], data) and evaluate_rule(rule_ast['right'], data)
    elif rule_ast['type'] == 'OR':
        return evaluate_rule(rule_ast['left'], data) or evaluate_rule(rule_ast['right'], data)
    elif rule_ast['type'] == '>':
        return data.get('age', 0) > rule_ast['value']['age']
    elif rule_ast['type'] == '<':
        return data.get('age', 0) < rule_ast['value']['age']
    elif rule_ast['type'] == '=':
        return data.get(rule_ast['value'].keys()) == rule_ast['value'].values()
    else:
        raise ValueError("Invalid rule node type")
