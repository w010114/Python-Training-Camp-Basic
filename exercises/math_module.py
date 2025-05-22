"""
练习: 使用math模块

描述：
使用math模块计算平方根。

请补全下面的函数，使用math模块的sqrt函数计算平方根。
"""

import math  # 导入 math 模块

def calculate_square_root(number):
    """
    计算数字的平方根
    
    参数:
    - number: 非负数
    
    返回:
    - 数字的平方根
    """
    # 请在下方编写代码
    if number < 0:
        return "错误：输入不能为负数"
    return math.sqrt(number)
    pass 