from datetime import datetime
from typing import Dict, Any

# UI层使用Python内置类型，而不是领域模型
# 这样可以实现关注点分离，防止领域逻辑泄露到UI层，并使UI层更容易适应变化

class UI:
    def __init__(self, service):
        self.service = service

    def create_note(self, content: str) -> int:
        """
        创建笔记

        参数:
            content: 笔记内容，不能为空

        返回:
            int: 创建的笔记ID

        异常:
            ValueError: 当内容为空时抛出
        """
        note = self.service.create_note(content)
        return note.id

    def query_note(self, note_id: int) -> Dict[str, Any]:
        """
        查询笔记

        参数:
            note_id: 笔记ID，不能小于0

        返回:
            Dict[str, Any]: 包含笔记详情的字典

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        note = self.service.query_note(note_id)
        # 将领域模型转换为字典
        return {
            "id": note.id,
            "content": note.content,
            "created_time": note.created_time,
            "updated_time": note.updated_time
        }

    def update_note(self, note_id: int, content: str) -> Dict[str, Any]:
        """
        更新笔记

        参数:
            note_id: 笔记ID，不能小于0
            content: 新的笔记内容，不能为空

        返回:
            Dict[str, Any]: 更新后的笔记详情字典

        异常:
            ValueError: 当ID小于0、内容为空或笔记不存在时抛出
        """
        note = self.service.update_note(note_id, content)
        # 将领域模型转换为字典
        return {
            "id": note.id,
            "content": note.content,
            "created_time": note.created_time,
            "updated_time": note.updated_time
        }

    def delete_note(self, note_id: int) -> None:
        """
        删除笔记

        参数:
            note_id: 笔记ID，不能小于0

        返回:
            None

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        self.service.delete_note(note_id)