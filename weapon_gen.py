"""
D&D 5E Weapon Generator
简单随机武器生成器
"""

import random
import yaml
from pathlib import Path
from typing import Optional, List, Dict, Any


class WeaponGenerator:
    """D&D 5E 武器生成器"""

    def __init__(self, data_dir: Optional[Path] = None):
        """
        初始化武器生成器

        Args:
            data_dir: 数据目录路径，默认为项目根目录下的 data 文件夹
        """
        if data_dir is None:
            # 默认使用项目根目录下的 data 文件夹
            data_dir = Path(__file__).parent / "data"

        self.data_dir = Path(data_dir)
        self._weapons = None
        self._properties = None
        self._damage_types = None
        self._legendary_weapons = None
        self._rarities = {
            'common': {'zh': '常见', 'en': 'Common'},
            'uncommon': {'zh': '少见', 'en': 'Uncommon'},
            'rare': {'zh': '稀有', 'en': 'Rare'},
            'very_rare': {'zh': '非常稀有', 'en': 'Very Rare'},
            'legendary': {'zh': '传奇', 'en': 'Legendary'}
        }

    def _load_yaml(self, filename: str) -> Dict[str, Any]:
        """加载 YAML 文件"""
        filepath = self.data_dir / filename
        with open(filepath, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    @property
    def weapons(self) -> List[Dict[str, Any]]:
        """获取所有武器数据"""
        if self._weapons is None:
            data = self._load_yaml('base-weapons.yaml')
            self._weapons = data['weapons']
        return self._weapons

    @property
    def properties(self) -> Dict[str, Any]:
        """获取所有武器属性"""
        if self._properties is None:
            data = self._load_yaml('weapon-properties.yaml')
            self._properties = data['properties']
        return self._properties

    @property
    def damage_types(self) -> Dict[str, Any]:
        """获取所有伤害类型"""
        if self._damage_types is None:
            data = self._load_yaml('damage-types.yaml')
            self._damage_types = data['damage_types']
        return self._damage_types

    @property
    def legendary_weapons(self) -> List[Dict[str, Any]]:
        """获取所有传奇武器数据"""
        if self._legendary_weapons is None:
            try:
                data = self._load_yaml('legendary-weapons.yaml')
                self._legendary_weapons = data['weapons']
            except FileNotFoundError:
                self._legendary_weapons = []
        return self._legendary_weapons

    def generate(
        self,
        category: Optional[str] = None,
        proficiency: Optional[str] = None,
        damage_type: Optional[str] = None,
        language: str = 'zh'
    ) -> Dict[str, Any]:
        """
        随机生成武器

        Args:
            category: 武器类别 (simple_melee, martial_melee, simple_ranged, martial_ranged)
            proficiency: 熟练度 (simple, martial)
            damage_type: 伤害类型 (bludgeoning, piercing, slashing)
            language: 语言 ('zh' 或 'en')

        Returns:
            武器字典，包含所有属性信息
        """
        # 筛选符合条件的武器
        filtered_weapons = self._filter_weapons(
            category=category,
            proficiency=proficiency,
            damage_type=damage_type
        )

        if not filtered_weapons:
            raise ValueError("没有找到符合条件的武器")

        # 随机选择一个武器
        weapon = random.choice(filtered_weapons)

        # 根据语言设置返回相应的内容
        result = self._format_weapon(weapon, language)

        return result

    def _filter_weapons(
        self,
        category: Optional[str] = None,
        proficiency: Optional[str] = None,
        damage_type: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        根据条件筛选武器

        Args:
            category: 武器类别
            proficiency: 熟练度
            damage_type: 伤害类型

        Returns:
            符合条件的武器列表
        """
        filtered = self.weapons

        # 按类别筛选
        if category:
            filtered = [w for w in filtered if w['category'] == category]

        # 按熟练度筛选（通过类别判断）
        if proficiency:
            if proficiency == 'simple':
                filtered = [w for w in filtered if w['category'].startswith('simple_')]
            elif proficiency == 'martial':
                filtered = [w for w in filtered if w['category'].startswith('martial_')]

        # 按伤害类型筛选
        if damage_type:
            filtered = [w for w in filtered if w['damage']['type'] == damage_type]

        return filtered

    def _format_weapon(self, weapon: Dict[str, Any], language: str) -> Dict[str, Any]:
        """
        格式化武器数据

        Args:
            weapon: 原始武器数据
            language: 语言 ('zh' 或 'en')

        Returns:
            格式化后的武器数据
        """
        result = {
            'id': weapon['id'],
            'name': weapon['name'][language],
            'category': weapon['category'],
            'damage': {
                'dice': weapon['damage']['dice'],
                'type': weapon['damage']['type'],
                'type_name': self.damage_types[weapon['damage']['type']]['name'][language]
            },
            'cost': weapon['cost'],
            'weight': weapon['weight'],
            'properties': [],
            'description': weapon['description'][language]
        }

        # 添加万能伤害（如果有）
        if 'versatile' in weapon['damage']:
            result['damage']['versatile'] = weapon['damage']['versatile']

        # 添加射程（如果有）
        if 'range' in weapon:
            result['range'] = weapon['range']

        # 添加投掷射程（如果有）
        if 'thrown_range' in weapon:
            result['thrown_range'] = weapon['thrown_range']

        # 格式化武器属性
        for prop_id in weapon.get('properties', []):
            if prop_id in self.properties:
                prop = self.properties[prop_id]
                result['properties'].append({
                    'id': prop_id,
                    'name': prop['name'][language],
                    'description': prop['description'][language]
                })

        return result

    def get_weapon_by_id(self, weapon_id: str, language: str = 'zh') -> Optional[Dict[str, Any]]:
        """
        根据 ID 获取武器

        Args:
            weapon_id: 武器 ID
            language: 语言 ('zh' 或 'en')

        Returns:
            武器数据，如果未找到则返回 None
        """
        for weapon in self.weapons:
            if weapon['id'] == weapon_id:
                return self._format_weapon(weapon, language)
        return None

    def list_categories(self) -> List[str]:
        """获取所有武器类别"""
        categories = set(w['category'] for w in self.weapons)
        return sorted(list(categories))

    def list_damage_types(self) -> List[str]:
        """获取所有伤害类型"""
        return sorted(set(w['damage']['type'] for w in self.weapons))

    def generate_legendary(self, language: str = 'zh') -> Dict[str, Any]:
        """
        随机生成传奇武器

        Args:
            language: 语言 ('zh' 或 'en')

        Returns:
            传奇武器字典，包含特殊能力
        """
        if not self.legendary_weapons:
            raise ValueError("没有找到传奇武器数据")

        # 随机选择一个传奇武器
        weapon = random.choice(self.legendary_weapons)

        # 根据语言设置返回相应的内容
        result = self._format_legendary_weapon(weapon, language)

        return result

    def get_legendary_by_id(self, weapon_id: str, language: str = 'zh') -> Optional[Dict[str, Any]]:
        """
        根据 ID 获取传奇武器

        Args:
            weapon_id: 武器 ID
            language: 语言 ('zh' 或 'en')

        Returns:
            传奇武器数据，如果未找到则返回 None
        """
        for weapon in self.legendary_weapons:
            if weapon['id'] == weapon_id:
                return self._format_legendary_weapon(weapon, language)
        return None

    def list_legendary_weapons(self) -> List[str]:
        """获取所有传奇武器 ID"""
        return [w['id'] for w in self.legendary_weapons]

    def _format_legendary_weapon(self, weapon: Dict[str, Any], language: str) -> Dict[str, Any]:
        """
        格式化传奇武器数据

        Args:
            weapon: 原始武器数据
            language: 语言 ('zh' 或 'en')

        Returns:
            格式化后的传奇武器数据
        """
        # 获取稀有度信息
        rarity = weapon.get('rarity', 'legendary')
        rarity_info = self._rarities.get(rarity, self._rarities['legendary'])

        result = {
            'id': weapon['id'],
            'name': weapon['name'][language],
            'category': weapon['category'],
            'rarity': rarity,
            'rarity_name': rarity_info[language],
            'damage': {
                'dice': weapon['damage']['dice'],
                'type': weapon['damage']['type'],
                'type_name': self.damage_types.get(weapon['damage']['type'], {}).get('name', {}).get(language, weapon['damage']['type'])
            },
            'cost': weapon['cost'],
            'weight': weapon['weight'],
            'properties': [],
            'description': weapon['description'][language]
        }

        # 添加万能伤害（如果有）
        if 'versatile' in weapon['damage']:
            result['damage']['versatile'] = weapon['damage']['versatile']

        # 添加射程（如果有）
        if 'range' in weapon:
            result['range'] = weapon['range']

        # 添加投掷射程（如果有）
        if 'thrown_range' in weapon:
            result['thrown_range'] = weapon['thrown_range']

        # 添加魔法加成（如果有）
        if 'magical_bonus' in weapon:
            result['magical_bonus'] = weapon['magical_bonus']

        # 添加充能（如果有）
        if 'charges' in weapon:
            result['charges'] = weapon['charges']

        # 格式化武器属性
        for prop_id in weapon.get('properties', []):
            if prop_id in self.properties:
                prop = self.properties[prop_id]
                result['properties'].append({
                    'id': prop_id,
                    'name': prop['name'][language],
                    'description': prop['description'][language]
                })

        # 添加特殊能力
        if 'special_abilities' in weapon:
            result['special_abilities'] = []
            for ability in weapon['special_abilities']:
                result['special_abilities'].append({
                    'id': ability['id'],
                    'name': ability['name'][language],
                    'description': ability['description'][language]
                })

        return result


def main():
    """命令行接口示例"""
    import json

    generator = WeaponGenerator()

    # 生成随机武器
    print("=== 随机武器生成 ===\n")

    # 示例 1: 完全随机
    weapon1 = generator.generate()
    print("随机武器:")
    print(json.dumps(weapon1, ensure_ascii=False, indent=2))
    print()

    # 示例 2: 指定军用近战武器
    weapon2 = generator.generate(category='martial_melee')
    print("军用近战武器:")
    print(json.dumps(weapon2, ensure_ascii=False, indent=2))
    print()

    # 示例 3: 指定穿刺伤害
    weapon3 = generator.generate(damage_type='piercing')
    print("穿刺伤害武器:")
    print(json.dumps(weapon3, ensure_ascii=False, indent=2))
    print()

    # 示例 4: 英文输出
    weapon4 = generator.generate(language='en')
    print("Random Weapon (English):")
    print(json.dumps(weapon4, ensure_ascii=False, indent=2))
    print()

    # 显示可用的类别和伤害类型
    print("=== 可用武器类别 ===")
    for cat in generator.list_categories():
        print(f"  - {cat}")

    print("\n=== 可用伤害类型 ===")
    for dt in generator.list_damage_types():
        print(f"  - {dt}")


if __name__ == '__main__':
    main()
