# Ralph Agent Configuration

## Build Instructions

```bash
# No build step required - Python project
# Install dependencies first:
pip3 install -r requirements.txt
```

## Test Instructions

```bash
# Run all tests
python3 test_weapon_gen.py

# Run with verbose output
python3 test_weapon_gen.py -v
```

## Run Instructions

```bash
# Run the weapon generator demo
python3 weapon_gen.py

# Use as a module in Python
from weapon_gen import WeaponGenerator

generator = WeaponGenerator()
weapon = generator.generate(category='martial_melee')
print(weapon)
```

## Dependencies

- Python 3.6+
- PyYAML >= 6.0

## Notes
- The weapon_gen.py module provides the main WeaponGenerator class
- Data files are in the data/ directory (YAML format)
- Supports bilingual output (Chinese/English)
