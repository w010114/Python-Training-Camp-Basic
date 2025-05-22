"""
练习: 集合操作

描述：
实现两个学生集合的并集、交集和差集操作。

请补全下面的函数，对两个学生集合进行各种操作。
"""

def student_set_operations(set1, set2, operation):
    """
    对两个学生集合进行操作
    
    参数:
    - set1: 第一个学生集合
    - set2: 第二个学生集合
    - operation: 操作类型 ("union", "intersection", "difference")
    
    返回:
    - 集合操作的结果
    """
    # 请在下方编写代码
    # 创建两个学生集合
    if operation == "union":
        # 并集操作
        return set1.union(set2)
    elif operation == "intersection":
        # 交集操作
        return set1.intersection(set2)
    elif operation == "difference":
        # 差集操作
        return set1.difference(set2)
    else:
        return "无效的操作类型"