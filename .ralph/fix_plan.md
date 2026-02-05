# Ralph Fix Plan

## High Priority
- [x] 基础武器数据库建立
- [x] 简单随机生成功能
- [ ] 武器卡片输出格式
- [ ] Claude Skill 基础框架
- [ ] 魔法武器生成
- [ ] 稀有度系统
- [ ] 自定义武器参数
- [ ] 武器验证系统
- [ ] 武器背景故事生成
- [ ] 武器变体系统
- [ ] 多语言支持（中英）
- [ ] 高级格式选项
- [ ] 装甲生成器
- [ ] 其他装备生成
- [ ] NPC 装备生成
- [ ] 战利品生成器
- [ ] 酸液 (Acid)
- [ ] 钝击 (Bludgeoning)
- [ ] 冷冻 (Cold)
- [ ] 火焰 (Fire)
- [ ] 力场 (Force)
- [ ] 闪电 (Lightning)
- [ ] 黯蚀 (Necrotic)
- [ ] 穿刺 (Piercing)
- [ ] 毒素 (Poison)
- [ ] 灵能 (Psychic)
- [ ] 光耀 (Radiant)
- [ ] 挥砍 (Slashing)
- [ ] 雷鸣 (Thunder)
- [ ] **非常见 (Uncommon)**: +1 武器


## Medium Priority


## Low Priority


## Completed
- [x] Project enabled for Ralph

## Notes
- Focus on MVP functionality first
- Ensure each feature is properly tested
- Update this file after each major milestone

## Progress Log

### 2025-02-05 - Loop #1
**Completed:** 基础武器数据库建立
- Created data/weapon-properties.yaml with all 11 weapon properties (ammunition, finesse, heavy, light, loading, range, reach, special, thrown, two_handed, versatile)
- Created data/damage-types.yaml with all 13 damage types including weapon damage types (bludgeoning, piercing, slashing)
- Created data/base-weapons.yaml with 38 weapons from D&D 5E PHB:
  - 10 Simple Melee Weapons
  - 18 Martial Melee Weapons
  - 4 Simple Ranged Weapons
  - 6 Martial Ranged Weapons
- All files include Chinese and English translations for bilingual support
- Data structure supports filtering by category, damage type, and weapon properties

### 2025-02-05 - Loop #2
**Completed:** 简单随机生成功能
- Created weapon_gen.py module with WeaponGenerator class
- Implemented random weapon generation with filtering by:
  - Category (simple_melee, martial_melee, simple_ranged, martial_ranged)
  - Proficiency (simple, martial)
  - Damage type (bludgeoning, piercing, slashing)
- Implemented get_weapon_by_id() for direct weapon lookup
- Implemented list_categories() and list_damage_types() helpers
- Added bilingual support (Chinese/English) for all output
- Created comprehensive test suite (test_weapon_gen.py) with 20+ tests
- Created requirements.txt with PyYAML dependency
- Updated AGENT.md with build/run instructions
