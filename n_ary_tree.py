

# Node class: store each email as a node
# key: message id; children: emails reply to this message id
class Node:
    def __init__(self,key, children = []):
        self.key = key
        self.children =  []
    
    def __str__(self):
        return str(self.key)

# N_ary_Tree class: create conversation, group messages related to each other
class N_ary_Tree:
    
    def __init__(self):
        self.root = Node('conversation: ')
    
    
    # Find the 'In-Reply-To' message by id
    # key: 'In-Reply-To' message id
    # node: start point
    def find_node(self,node,key):
        
        if  node.key == key:
            return node
        
        for child in node.children:
            found = self.find_node(child,key)
            if found:
                return found
        return None


    
   
    
    # Function to add child to node
    # parent_key: 'In-Reply-To' message id
    # new_key: message id of email needed to be add to the tree
    def add(self,new_key,parent_key='conversation: '):
        
        new_node = Node(new_key)
        
        parent_node = self.find_node(self.root,parent_key)
        parent_node.children.append(new_node)


    # dfs function to loop through each branches
    # node: root
    def dfs(self,node):
        path = []
        # visit node recursively
        def recurse(n):
            path.append(n.key)
            if not n.children:
                yield path
            for child in n.children:
                for c in recurse(child):
                    yield c
            path.pop()
        for n in recurse(node):
            yield path

        
    # Function to print each branch node to leaf
    def print_branches(self,node):
        for path in self.dfs(self.root):
            path_str = '<-'.join(map(str,path[1:]))
            print path_str

