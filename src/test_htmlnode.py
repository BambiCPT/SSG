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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


if __name__ == "__main__":
    unittest.main()

