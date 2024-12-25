#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boss_drf.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
# # 导入需要的库
# from sympy import symbols, Eq, solve
#
# # 定义变量
# x, y = symbols('x y')
#
# # 建立方程组
# equation1 = Eq(x + y, 11)
# equation2 = Eq(35*x + 28*y, 350)
#
# # 使用solve解方程组
# solutions = solve((equation1, equation2), (x, y), dict=True)
# sunny_days = solutions[0][x]
# rainy_days = solutions[0][y]
#
# # 输出结果
# print(f"计算结果为：晴天有 {sunny_days} 天，雨天有 {rainy_days} 天。")