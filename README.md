RuleEngine-AST/
│
├── app.py                  # Main Flask application
├── config.py               # Configuration for database, etc.
├── requirements.txt        # Project dependencies
├── README.md               # Documentation
├── Dockerfile              # Docker setup (Optional)
├── src/                    # Source folder for AST and rule logic
│   ├── ast_structure.py    # AST Node structure
│   ├── rule_creation.py    # Rule creation logic
│   ├── rule_combination.py # Combining rules logic
│   └── rule_evaluation.py  # Rule evaluation logic
├── tests/                  # Unit test folder
│   ├── test_rules.py       # Unit tests for rules
├── templates/              # HTML templates (UI)
│   └── index.html          # Simple UI for rule creation
└── static/                 # Static files (if needed)
    └── styles.css          # Optional CSS
