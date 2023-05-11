stack = []  # 스택 선언
tmp_res = 1
result = 0
chars = list(input())  # 입력값

for i in range(len(chars)):
    if chars[i] == '(':
        tmp_res *= 2
        stack.append(chars[i])

    elif chars[i] == '[':
        tmp_res *= 3
        stack.append(chars[i])

    elif chars[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break

        if chars[i-1] == '(':
            result += tmp_res

        tmp_res //= 2
        stack.pop()

    elif chars[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break

        if chars[i-1] == '[':
            result += tmp_res

        tmp_res //= 3
        stack.pop()

print(0 if stack else result)
