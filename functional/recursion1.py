def test_recursion(num: int) -> int:
    print(f'до рекурсивного вызова: {num = }')
    
    if num > 0:
        result = test_recursion(num - 1)
    else:
        result = num
    
    print(f'после рекурсивного вызова: {result = }')
    return result


var = test_recursion(5)

# до рекурсивного вызова: num = 5
# до рекурсивного вызова: num = 4
# до рекурсивного вызова: num = 3
# до рекурсивного вызова: num = 2
# до рекурсивного вызова: num = 1
# до рекурсивного вызова: num = 0
# после рекурсивного вызова: result = 0
# после рекурсивного вызова: result = 0
# после рекурсивного вызова: result = 0
# после рекурсивного вызова: result = 0
# после рекурсивного вызова: result = 0
# после рекурсивного вызова: result = 0

