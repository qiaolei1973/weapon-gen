"""
Tests for D&D 5E Weapon Generator
武器生成器测试
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to path to import weapon_gen
sys.path.insert(0, str(Path(__file__).parent))

from weapon_gen import WeaponGenerator


class TestWeaponGenerator(unittest.TestCase):
    """武器生成器测试类"""

    def setUp(self):
        """测试前设置"""
        self.generator = WeaponGenerator()

    def test_initialization(self):
        """测试初始化"""
        self.assertIsNotNone(self.generator)
        self.assertEqual(self.generator.data_dir.name, 'data')

    def test_load_weapons(self):
        """测试加载武器数据"""
        weapons = self.generator.weapons
        self.assertIsNotNone(weapons)
        self.assertGreater(len(weapons), 0)
        # 应该有 38 个基础武器
        self.assertEqual(len(weapons), 38)

    def test_load_properties(self):
        """测试加载武器属性"""
        properties = self.generator.properties
        self.assertIsNotNone(properties)
        self.assertIn('ammunition', properties)
        self.assertIn('finesse', properties)
        self.assertIn('versatile', properties)
        # 应该有 11 个基础属性
        self.assertEqual(len(properties), 11)

    def test_load_damage_types(self):
        """测试加载伤害类型"""
        damage_types = self.generator.damage_types
        self.assertIsNotNone(damage_types)
        self.assertIn('bludgeoning', damage_types)
        self.assertIn('piercing', damage_types)
        self.assertIn('slashing', damage_types)
        # 应该有 13 种伤害类型
        self.assertEqual(len(damage_types), 13)

    def test_generate_random_weapon(self):
        """测试随机生成武器"""
        weapon = self.generator.generate()
        self.assertIsNotNone(weapon)
        self.assertIn('id', weapon)
        self.assertIn('name', weapon)
        self.assertIn('category', weapon)
        self.assertIn('damage', weapon)
        self.assertIn('cost', weapon)
        self.assertIn('weight', weapon)
        self.assertIn('properties', weapon)
        self.assertIn('description', weapon)

    def test_generate_by_category(self):
        """测试按类别生成武器"""
        # 测试简单近战武器
        weapon = self.generator.generate(category='simple_melee')
        self.assertEqual(weapon['category'], 'simple_melee')

        # 测试军用近战武器
        weapon = self.generator.generate(category='martial_melee')
        self.assertEqual(weapon['category'], 'martial_melee')

        # 测试简单远程武器
        weapon = self.generator.generate(category='simple_ranged')
        self.assertEqual(weapon['category'], 'simple_ranged')

        # 测试军用远程武器
        weapon = self.generator.generate(category='martial_ranged')
        self.assertEqual(weapon['category'], 'martial_ranged')

    def test_generate_by_proficiency(self):
        """测试按熟练度生成武器"""
        # 测试简单武器
        weapon = self.generator.generate(proficiency='simple')
        self.assertTrue(weapon['category'].startswith('simple_'))

        # 测试军用武器
        weapon = self.generator.generate(proficiency='martial')
        self.assertTrue(weapon['category'].startswith('martial_'))

    def test_generate_by_damage_type(self):
        """测试按伤害类型生成武器"""
        # 测试钝击伤害
        weapon = self.generator.generate(damage_type='bludgeoning')
        self.assertEqual(weapon['damage']['type'], 'bludgeoning')

        # 测试穿刺伤害
        weapon = self.generator.generate(damage_type='piercing')
        self.assertEqual(weapon['damage']['type'], 'piercing')

        # 测试挥砍伤害
        weapon = self.generator.generate(damage_type='slashing')
        self.assertEqual(weapon['damage']['type'], 'slashing')

    def test_generate_with_language(self):
        """测试多语言支持"""
        # 测试中文
        weapon_zh = self.generator.generate(language='zh')
        self.assertIsNotNone(weapon_zh['name'])
        # 验证属性描述是中文
        if weapon_zh['properties']:
            self.assertIn('name', weapon_zh['properties'][0])

        # 测试英文
        weapon_en = self.generator.generate(language='en')
        self.assertIsNotNone(weapon_en['name'])
        # 验证属性描述是英文
        if weapon_en['properties']:
            self.assertIn('name', weapon_en['properties'][0])

    def test_get_weapon_by_id(self):
        """测试根据 ID 获取武器"""
        # 测试存在的武器
        weapon = self.generator.get_weapon_by_id('longsword')
        self.assertIsNotNone(weapon)
        self.assertEqual(weapon['id'], 'longsword')

        # 测试不存在的武器
        weapon = self.generator.get_weapon_by_id('nonexistent')
        self.assertIsNone(weapon)

    def test_list_categories(self):
        """测试列出所有类别"""
        categories = self.generator.list_categories()
        self.assertIsNotNone(categories)
        self.assertGreater(len(categories), 0)
        self.assertIn('simple_melee', categories)
        self.assertIn('martial_melee', categories)

    def test_list_damage_types(self):
        """测试列出所有伤害类型"""
        damage_types = self.generator.list_damage_types()
        self.assertIsNotNone(damage_types)
        self.assertGreater(len(damage_types), 0)
        self.assertIn('bludgeoning', damage_types)
        self.assertIn('piercing', damage_types)
        self.assertIn('slashing', damage_types)

    def test_weapon_data_structure(self):
        """测试武器数据结构完整性"""
        weapon = self.generator.generate()

        # 检查基本信息
        self.assertIsInstance(weapon['id'], str)
        self.assertIsInstance(weapon['name'], str)
        self.assertIsInstance(weapon['category'], str)

        # 检查伤害信息
        self.assertIn('dice', weapon['damage'])
        self.assertIn('type', weapon['damage'])
        self.assertIn('type_name', weapon['damage'])
        self.assertIsInstance(weapon['damage']['dice'], str)
        self.assertIsInstance(weapon['damage']['type'], str)
        self.assertIsInstance(weapon['damage']['type_name'], str)

        # 检查重量和价格
        self.assertIsInstance(weapon['weight'], (int, float))
        self.assertIsInstance(weapon['cost'], str)

        # 检查属性列表
        self.assertIsInstance(weapon['properties'], list)

        # 检查描述
        self.assertIsInstance(weapon['description'], str)

    def test_versatile_damage(self):
        """测试万能武器伤害"""
        # 获取一个万能武器（如长剑）
        weapon = self.generator.get_weapon_by_id('longsword')
        self.assertIsNotNone(weapon)
        self.assertIn('versatile', weapon['damage'])

    def test_ranged_weapon_range(self):
        """测试远程武器射程"""
        # 获取一个远程武器（如短弓）
        weapon = self.generator.get_weapon_by_id('shortbow')
        self.assertIsNotNone(weapon)
        self.assertIn('range', weapon)

    def test_thrown_weapon_range(self):
        """测试投掷武器射程"""
        # 获取一个投掷武器（如匕首）
        weapon = self.generator.get_weapon_by_id('dagger')
        self.assertIsNotNone(weapon)
        self.assertIn('thrown_range', weapon)

    def test_combined_filters(self):
        """测试组合筛选条件"""
        # 测试军用近战 + 穿刺伤害
        weapon = self.generator.generate(
            category='martial_melee',
            damage_type='piercing'
        )
        self.assertEqual(weapon['category'], 'martial_melee')
        self.assertEqual(weapon['damage']['type'], 'piercing')


def run_tests():
    """运行所有测试"""
    # 创建测试套件
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestWeaponGenerator)

    # 运行测试
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # 返回测试结果
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
