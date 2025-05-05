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
        return self.service.create_note(content)

    def query_note(self, note_id: int) -> dict:
        """
        查询笔记

        参数:
            note_id: 笔记ID，不能小于0

        返回:
            dict: 包含笔记详情的字典，包括id、内容、创建时间和修改时间

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        return self.service.query_note(note_id)

    def update_note(self, note_id: int, content: str) -> bool:
        """
        更新笔记

        参数:
            note_id: 笔记ID，不能小于0
            content: 新的笔记内容，不能为空

        返回:
            bool: 更新成功返回True

        异常:
            ValueError: 当ID小于0、内容为空或笔记不存在时抛出
        """
        return self.service.update_note(note_id, content)

    def delete_note(self, note_id: int) -> bool:
        """
        删除笔记

        参数:
            note_id: 笔记ID，不能小于0

        返回:
            bool: 删除成功返回True

        异常:
            ValueError: 当ID小于0或笔记不存在时抛出
        """
        return self.service.delete_note(note_id)