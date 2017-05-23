import ast


class MyVisitor(ast.NodeVisitor):
    def visit_Str(self, node):
        print('\tFound string "%s"' % node.s)

    def generic_visit(self, node):
        print('type : %s' % type(node).__name__ )
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        print('\tName : %s,%s' % (node.id, node.ctx))



class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        print('transformer : %s' % node.s)
        return ast.Str('str: ' + node.s)


if __name__ == '__main__':
    node = ast.parse('''
favs = ['berry', 'apple']
name = 'peter'
    
for item in favs:
    print( '%s likes %s' % (name, item) )
    ''')

    node2 = ast.parse('''
class MyVisitor(ast.NodeVisitor):
    def visit_Str(self, node):
        print('\tFound string "%s"' % node.s)

    def generic_visit(self, node):
        print('type : %s' % type(node).__name__ )
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Name(self, node):
        print('\tName : %s,%s' % (node.id, node.ctx))



class MyTransformer(ast.NodeTransformer):
    def visit_Str(self, node):
        print('transformer : %s' % node.s)
        return ast.Str('str: ' + node.s)
    ''')

    fixed = ast.fix_missing_locations(node)

    print(ast.dump(fixed))

    #MyTransformer().visit(fixed)
    MyVisitor().visit(fixed)


    exec(compile(fixed, '<string>', 'exec'))

    fixed2 = ast.fix_missing_locations(node2)
    print(ast.dump(fixed2))