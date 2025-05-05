import unittest
import os
from src.infra.db import DB
from src.service.service import Service

class TestNoteApp(unittest.TestCase):
    def setUp(self):
        """每个测试用例前运行，初始化测试环境"""
        # 使用内存数据库进行测试
        self.db = DB(":memory:")
        self.service = Service(self.db)

    def test_create_note(self):
        """测试创建笔记功能"""
        # 测试正常创建笔记
        note_id = self.service.create_note("测试笔记内容")
        self.assertEqual(note_id, 1)  # 第一个笔记ID应该是1

        # 测试创建第二个笔记
        note_id2 = self.service.create_note("第二个笔记")
        self.assertEqual(note_id2, 2)  # 第二个笔记ID应该是2

        # 测试创建空内容笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.create_note("")

    def test_query_note(self):
        """测试查询笔记功能"""
        # 先创建一个笔记
        note_id = self.service.create_note("测试查询笔记")

        # 测试查询存在的笔记
        note = self.service.query_note(note_id)
        self.assertEqual(note["id"], note_id)
        self.assertEqual(note["content"], "测试查询笔记")
        self.assertIn("created_at", note)
        self.assertIn("updated_at", note)

        # 测试查询不存在的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.query_note(999)

        # 测试查询ID为负数的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.query_note(-1)

    def test_update_note(self):
        """测试更新笔记功能"""
        # 先创建一个笔记
        note_id = self.service.create_note("原始内容")

        # 查询原始笔记
        original_note = self.service.query_note(note_id)
        original_updated_at = original_note["updated_at"]

        # 等待一小段时间，确保更新时间会不同
        import time
        time.sleep(1)  # 增加等待时间到1秒

        # 测试更新笔记
        self.service.update_note(note_id, "更新后的内容")

        # 查询更新后的笔记
        updated_note = self.service.query_note(note_id)
        self.assertEqual(updated_note["content"], "更新后的内容")
        self.assertNotEqual(updated_note["updated_at"], original_updated_at)  # 更新时间应该变化

        # 测试更新不存在的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.update_note(999, "新内容")

        # 测试更新ID为负数的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.update_note(-1, "新内容")

        # 测试更新笔记为空内容，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.update_note(note_id, "")

    def test_delete_note(self):
        """测试删除笔记功能"""
        # 先创建一个笔记
        note_id = self.service.create_note("要删除的笔记")

        # 测试删除笔记
        self.assertTrue(self.service.delete_note(note_id))

        # 删除后查询应该抛出异常
        with self.assertRaises(ValueError):
            self.service.query_note(note_id)

        # 测试删除不存在的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.delete_note(999)

        # 测试删除ID为负数的笔记，应该抛出ValueError异常
        with self.assertRaises(ValueError):
            self.service.delete_note(-1)

if __name__ == "__main__":
    unittest.main()
