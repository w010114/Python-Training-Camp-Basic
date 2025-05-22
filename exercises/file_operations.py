"""
练习: 文件处理

描述：
本练习帮助您学习如何在Python中进行文件的读取和写入操作。

请补全下面的函数，实现文件的读取和写入功能。
"""

def read_file(file_path):
    """
    读取文本文件内容
    
    参数:
    - file_path: 文件路径
    
    返回:
    - 文件内容字符串
    """
    # 请在下方编写代码
    # 使用open()函数打开文件并读取内容
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"错误：文件 '{file_path}' 不存在"
    except Exception as e:
        return f"读取文件时发生错误：{e}"
    pass

def write_file(file_path, content):
    """
    写入内容到文本文件
    
    参数:
    - file_path: 文件路径
    - content: 要写入的内容
    
    返回:
    - 是否写入成功的布尔值
    """
    # 请在下方编写代码
    # 使用with语句和open()函数写入内容到文件
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        return True
    except PermissionError:
        return f"错误：没有权限写入文件 '{file_path}'"
    except Exception as e:
        return f"写入文件时发生错误：{e}"
    pass 