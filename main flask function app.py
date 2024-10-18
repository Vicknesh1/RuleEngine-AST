from flask import Flask, jsonify, request
from src.ast_structure import Node
from src.rule_creation import create_rule
from src.rule_combination import combine_rules
from src.rule_evaluation import evaluate_rule

app = Flask(__name__)

# Sample rule storage (In real implementation, this can be a database)
rules_store = []

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json.get('rule_string')
    if not rule_string:
        return jsonify({'error': 'Rule string is required'}), 400
    try:
        rule_ast = create_rule(rule_string)
        rules_store.append(rule_ast)
        return jsonify({'message': 'Rule created', 'ast': rule_ast.to_dict()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['GET'])
def combine_rules_endpoint():
    if not rules_store:
        return jsonify({'error': 'No rules to combine'}), 400
    try:
        combined_ast = combine_rules(rules_store)
        return jsonify({'combined_ast': combined_ast.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_ast = request.json.get('rule_ast')
    user_data = request.json.get('data')
    if not rule_ast or not user_data:
        return jsonify({'error': 'Rule AST and user data are required'}), 400
    try:
        result = evaluate_rule(rule_ast, user_data)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
