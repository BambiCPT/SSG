import unittest
from htmlnode import HTMLnode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_creation(self):
        node = HTMLnode(tag='div', value='hello world!', props={'class': 'container'})
        assert node.tag == 'div'
        assert node.value == 'hello world!'
        assert node.props == {'class': 'container'}

class TestLeafNode(unittest.TestCase):
    def test_leafnode_to_html(self):
        leaf = LeafNode(data='this is a leaf')
        leaf.tag = 'p'
        leaf.props = {'class': 'leaf'}
        assert leaf.to_html() == "<p class='leaf'>this is a leaf</p>"

class TestParentNode(unittest.TestCase):
    def test_single_child(self):
        parent = ParentNode('div', [
            LeafNode(tag='p', data='Hello World')
        ])
        expected_html = '<div><p>Hello World</p></div>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_multiple_children(self):
        parent = ParentNode('ul', [
            LeafNode('li', 'Item 1'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ])
        expected_html = '<ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul>'
        self.assertEqual(parent.to_html(), expected_html)

    def test_nested_nodes(self):
        nested_parent = ParentNode('div', [
            ParentNode('ul', [
                LeafNode('li', 'Nested 1'),
                LeafNode('li', 'Nested 2')
            ]),
            LeafNode('p', 'Another paragraph')
        ])
        expected_html = '<div><ul><li>Nested 1</li><li>Nested 2</li></ul><p>Another paragraph</p></div>'
        self.assertEqual(nested_parent.to_html(), expected_html)

    def test_no_tag(self):
        with self.assertRaises(ValueError):
            parent = ParentNode(tag=None, children=[
                LeafNode('p', 'Hello World')
            ])
    
    def test_no_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode('div', None)


if __name__ == "__main__":
    unittest.main()

