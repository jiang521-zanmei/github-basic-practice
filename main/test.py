# main/test.py
"""
GitHub基础操作实验测试文件
功能：实现简单的数值计算和字符串处理
"""

def add(a: int, b: int) -> int:
    """两数相加"""
    return a + b

def str_reverse(s: str) -> str:
    """字符串反转"""
    return s[::-1]

if __name__ == "__main__":
    # 测试加法函数
    num1, num2 = 10, 20
    print(f"{num1} + {num2} = {add(num1, num2)}")

    # 测试字符串反转函数
    test_str = "GitHub Basic Practice"
    print(f"字符串反转：{str_reverse(test_str)}")
