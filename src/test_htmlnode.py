import unittest
from htmlnode import htmlnode, leafnode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode_creation(self):
        node = htmlnode(tag='div', value='hello world!', props={'class': 'container'})
        assert node.tag == 'div'
        assert node.value == 'hello world!'
        assert node.props == {'class': 'container'}

    def test_leafnode_to_html(self):
        leaf = leafnode(data='this is a leaf')
        leaf.tag = 'p'
        leaf.props = {'class': 'leaf'}
        assert leaf.to_html() == "<p class='leaf'>this is a leaf</p>"

if __name__ == "__main__":
    unittest.main()

