# 递归函数模板
# def recursion(level,param1,param2):
#
#     # recursion terminator递归的终止条件
#     if level>MAX_LEVEL:
#         print_result
#         return
#
#     # process logic in current level
#     process_data(level,data)
#
#     # drill down
#     self.recursion(leve1+1,p1,p2)
#
#     # reverse the current level status if needed
#     reverse_state(level)

# 计算n!
def Factorial(n):
    if n <= 1:
        return 1
    return n * Factorial(n - 1)


# 计算斐波那契数列
def Fib(n):
    if n == 0 or n == 1:
        return n
    return Fib(n - 1) + Fib(n - 2)


if __name__ == "__main__":
    print(Fib(10))
