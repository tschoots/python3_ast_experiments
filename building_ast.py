import ast


if __name__ == "__main__":
    node = ast.Expression(ast.BinOp(
        ast.Str('xy'),
        ast.Mult(),
        ast.Num(3)
    ))

    fixed = ast.fix_missing_locations(node)

    print(ast.dump(node))
    codeobj = compile(fixed, '<strings>', 'eval')
    print(eval(codeobj))