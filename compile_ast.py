import ast

if __name__ == '__main__':
    source = '6 + 8'
    node = ast.parse(source, mode='eval')

    print(ast.dump(node))
    print(eval(compile(node, '<string>', mode='eval')))
