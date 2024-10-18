import unittest
from src.rule_creation import create_rule
from src.rule_combination import combine_rules
from src.rule_evaluation import evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        rule = create_rule("age > 30 AND department = 'Sales'")
        self.assertIsNotNone(rule)
    
    def test_combine_rules(self):
        rule1 = create_rule("age > 30 AND department = 'Sales'")
        rule2 = create_rule("age < 25 AND department = 'Marketing'")
        combined_rule = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_rule)
    
    def test_evaluate_rule(self):
        rule = create_rule("age > 30 AND department = 'Sales'")
        user_data = {'age': 35, 'department': 'Sales'}
        result = evaluate_rule(rule.to_dict(), user_data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
