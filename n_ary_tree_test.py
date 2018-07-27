import unittest
from n_ary_tree import Node,N_ary_Tree


class TestNAryTree(unittest.TestCase):
    # test find_node function
    def test_find_node(self):
        tree = N_ary_Tree()
        tree.add('example1')
        tree.add('example2','example1')
        tree.add('example4','example1')
        #case1: start
        self.assertEqual(tree.find_node(tree.root,'example1').key,'example1')
        #case2: normal leaf
        self.assertEqual(tree.find_node(tree.root,'example2').key,'example2')
        self.assertEqual(tree.find_node(tree.root,'example4').key,'example4')
        #case3: non exist node
        self.assertEqual(tree.find_node(tree.root,'example3'),None)


    # test add function
    def test_add(self):
        tree = N_ary_Tree()
        tree.add('example1')
        tree.add('example2','example1')
        tree.add('example3','example2')
        tree.add('example4','example1')
        #case1: no children
        self.assertEqual(tree.find_node(tree.root,'example3').children,[])
        #case2: one child
        self.assertEqual(len(tree.find_node(tree.root,'example2').children),1)
        #case3: more than one children
        self.assertEqual(len(tree.find_node(tree.root,'example1').children),2)
        #case4: mutiple level children
        self.assertEqual(len(tree.find_node(tree.root,'example1').children[0].children),1)

    


        



if __name__ == '__main__':
    unittest.main()
        
        
