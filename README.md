# D&D 5E Weapon Generator

A D&D 5th Edition weapon generator with support for random weapon generation, filtering, and bilingual output (Chinese/English).

## Features

- **Random Weapon Generation**: Generate random weapons from the D&D 5E Player's Handbook
- **Filtering Options**: Filter by category, proficiency, and damage type
- **Bilingual Support**: Output in Chinese or English
- **Complete Database**: 38 base weapons with full properties and descriptions

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Command Line

```bash
python3 weapon_gen.py
```

### As a Python Module

```python
from weapon_gen import WeaponGenerator

# Create generator instance
generator = WeaponGenerator()

# Generate a random weapon
weapon = generator.generate()
print(weapon)

# Generate specific weapon types
weapon = generator.generate(category='martial_melee')
weapon = generator.generate(damage_type='piercing')

# Get weapon by ID
weapon = generator.get_weapon_by_id('longsword')

# List available categories and damage types
categories = generator.list_categories()
damage_types = generator.list_damage_types()
```

## Data Structure

Each weapon includes:
- **ID**: Unique identifier
- **Name**: Bilingual name (Chinese/English)
- **Category**: simple_melee, martial_melee, simple_ranged, martial_ranged
- **Damage**: Dice, type, and versatile damage (if applicable)
- **Properties**: List of weapon properties with descriptions
- **Cost and Weight**: Price and weight in lbs
- **Description**: Detailed flavor text

## Testing

```bash
python3 test_weapon_gen.py
```

## Project Status

See `.ralph/fix_plan.md` for detailed progress tracking.

### Completed
- [x] 基础武器数据库建立 (Basic weapon database)
- [x] 简单随机生成功能 (Simple random generation)

### In Progress
- [ ] 武器卡片输出格式 (Weapon card output format)
- [ ] Claude Skill 基础框架 (Claude Skill framework)

## License

MIT
