from db import DB
from repository import NoteRepository
from service import Service
from ui import UI

# 前端层通过UI层提供的接口与系统交互
# UI层返回Python内置类型（如字典），而不是领域模型
# 这样可以使前端与领域层解耦，提高系统的可维护性和适应性

def main():
    """
    初始化应用组件

    返回:
        UI: 用户界面对象，可以通过它调用笔记应用的各种功能
    """
    # 初始化组件
    db = DB("notes.db")  # 使用文件数据库
    repository = NoteRepository(db)
    service = Service(repository)
    ui = UI(service)

    return ui

if __name__ == "__main__":
    # 示例用法
    ui = main()

    # 创建笔记示例
    try:
        note_id = ui.create_note("这是一个测试笔记")
        print(f"笔记创建成功，ID: {note_id}")

        # 查询笔记示例
        note = ui.query_note(note_id)
        print("\n笔记详情:")
        print(f"ID: {note['id']}")
        print(f"内容: {note['content']}")
        print(f"创建时间: {note['created_time']}")
        print(f"修改时间: {note['updated_time']}")

        # 更新笔记示例
        updated_note = ui.update_note(note_id, "这是更新后的笔记内容")
        print(f"\n笔记 {note_id} 更新成功")

        # 再次查询笔记，查看更新结果
        updated_note = ui.query_note(note_id)
        print("\n更新后的笔记详情:")
        print(f"ID: {updated_note['id']}")
        print(f"内容: {updated_note['content']}")
        print(f"创建时间: {updated_note['created_time']}")
        print(f"修改时间: {updated_note['updated_time']}")

        # 删除笔记示例
        ui.delete_note(note_id)
        print(f"\n笔记 {note_id} 删除成功")

    except ValueError as e:
        print(f"操作失败: {str(e)}")
