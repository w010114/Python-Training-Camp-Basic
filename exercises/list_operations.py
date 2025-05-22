"""
练习：列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""
def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    if operation == "add":
        # 添加学生
        if len(args) >= 1:
            student_to_add = args[0]
            students.append(student_to_add)
        else:
            return students  # 参数不足，返回原列表

    elif operation == "remove":
        # 删除学生
        if len(args) >= 1:
            student_to_remove = args[0]
            if student_to_remove in students:
                students.remove(student_to_remove)

    elif operation == "update":
        # 修改学生信息
        if len(args) >= 2:
            old_name = args[0]  # 要替换的学生姓名
            new_name = args[1]  # 新的学生姓名
            if old_name in students:
                index = students.index(old_name)
                students[index] = new_name

    return students  # 返回更新后的学生列表