class Node:
    def __init__(self,key, children =None):
        self.key = key
        self.children = children or []
    
    def __str__(self):
        return str(self.key)


class N_ary_Tree:
    
    def __init_(self):
        self.root = None
        self.size = 0
    
    def find_node(self,node,key):
        if node == None or node.key == key:
            return node
        
        for child in node.children:
            found = self.find_node(child,key)
            if found:
                return found

        return None


    def add(self,new_key,parent_key= None):
        new_node =Node(new_key)
        if parent_key == None:
            self.root = new_node
    
        else:
            parent_node = self.find_node(self.root,parent_key)
            parent_node.children.append(new_node)




    def dfs(self,node):
        path = []
        def recurse(n):
            path.append(n.key)
            if not n.children:
                yield path
            for child in n.children:
                for x in recurse(child):
                    yield x
            path.pop()
        for v in recurse(node):
            yield path
        

    def print_branches(self,node):
        for path in self.dfs(self.root):
            path_str = '<-'.join(map(str,[n for n in path]))
            print path_str




if __name__ == "__main__":
    				
	tree = N_ary_Tree()
	tree.add('10')
	tree.add('20', '10')
	tree.add('30', '10')
	tree.add('60', '20')
	

	
	print tree.print_branches(tree)
