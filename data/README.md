# D&D 5E Weapon Generator - Data

This directory contains the foundational data for the D&D 5E Weapon Generator.

## Files

### weapon-properties.yaml
Defines all weapon properties from the Player's Handbook, including:
- Core properties: ammunition, finesse, heavy, light, loading, range, reach, special, thrown, two_handed, versatile
- Mastery property (from PHB 2024, optional)
- Bilingual support (Chinese/English)
- Detailed descriptions for each property

### damage-types.yaml
Defines all 13 damage types in D&D 5E:
- Weapon damage types: bludgeoning, piercing, slashing
- Elemental damage types: acid, cold, fire, lightning
- Special damage types: force, necrotic, poison, psychic, radiant, thunder
- Categorized for easy filtering

### base-weapons.yaml
Complete database of 38 weapons from D&D 5E PHB:
- **10 Simple Melee Weapons**: Club, Dagger, Greatclub, Handaxe, Javelin, Light Hammer, Mace, Quarterstaff, Sickle, Spear
- **18 Martial Melee Weapons**: Battleaxe, Flail, Glaive, Greataxe, Greatsword, Halberd, Lance, Longsword, Maul, Morningstar, Pike, Rapier, Scimitar, Shortsword, Trident, War Pick, Warhammer, Whip
- **4 Simple Ranged Weapons**: Light Crossbow, Dart, Shortbow, Sling
- **6 Martial Ranged Weapons**: Blowgun, Hand Crossbow, Heavy Crossbow, Longbow

Each weapon entry includes:
- Unique ID
- Bilingual name (Chinese/English)
- Category (simple_melee, martial_melee, simple_ranged, martial_ranged)
- Damage dice and type
- Cost and weight
- Properties
- Detailed descriptions

## Data Structure

### Weapon Entry Example
```yaml
- id: "longsword"
  name:
    zh: "长剑"
    en: "Longsword"
  category: "martial_melee"
  damage:
    dice: "1d8"
    type: "slashing"
    versatile: "1d10"
  cost: "15 gp"
  weight: 3
  properties:
    - "versatile"
  description:
    zh: "经典的战士武器..."
    en: "A classic fighter's weapon..."
```

## Usage

These YAML files serve as the database for the weapon generator:
1. Load the YAML data into your application
2. Filter by category, damage type, or properties
3. Generate random or custom weapons
4. Format output as weapon cards

## Sources

- Player's Handbook 5th Edition
- SRD 5.1
- 5etools (https://5e.kiwee.top/)
