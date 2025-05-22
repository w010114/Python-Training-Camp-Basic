"""
练习: 字典操作

描述：
实现对学生成绩字典的添加、删除、修改和查询操作。

请补全下面的函数，对学生成绩字典进行各种操作。
"""

def student_dict_operations(students_dict, operation, *args):
    """
    对学生字典进行操作
    
    参数:
    - students_dict: 学生字典 {姓名: 成绩}
    - operation: 操作类型 ("add", "remove", "update", "get")
    - args: 操作所需的额外参数
    
    返回:
    - 根据操作返回不同结果
    """
    if operation == "add":
        # 添加学生和成绩
        if len(args) == 2:
            name, score = args
            students_dict[name] = score
            return students_dict  # 返回更新后的字典
        else:
            return "添加操作需要提供两个参数：姓名和成绩"
    
    elif operation == "remove":
        # 删除学生
        if len(args) == 1:
            name = args[0]
            if name in students_dict:
                del students_dict[name]
                return students_dict  # 返回更新后的字典
            else:
                return f"学生 {name} 不存在"
        else:
            return "删除操作需要提供一个参数：姓名"
    
    elif operation == "update":
        # 更新学生成绩
        if len(args) == 2:
            name, score = args
            if name in students_dict:
                students_dict[name] = score
                return students_dict  # 返回更新后的字典
            else:
                return f"学生 {name} 不存在"
        else:
            return "更新操作需要提供两个参数：姓名和成绩"
    
    elif operation == "get":
        # 查询学生成绩
        if len(args) == 1:
            name = args[0]
            return students_dict.get(name, f"学生 {name} 不存在")
        else:
            return "查询操作需要提供一个参数：姓名"
    
    else:
        return "无效的操作类型"