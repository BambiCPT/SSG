from htmlnode import HTMLnode, LeafNode, ParentNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
   
    def __eq__(self, other): 
        if (self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url):
            return True
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

    def text_node_to_html_node(text_node): #thought about doing the text_types in a dictionary somehow but might just come back to it at some point for now good enuf
        if text_node.text_type == text_type_text:
            return LeafNode(data=text_node.text)
        elif text_node.text_type == text_type_bold:
            return LeafNode(tag='b', data=text_node.text)
        elif text_node.text_type == text_type_italic:
            return LeafNode(tag='i', data=text_node.text)
        elif text_node.text_type == text_type_code:
            return LeafNode(tag='code', data=text_node.text)
        elif text_node.text_type == text_type_link:
            return LeafNode(tag='a', props={'href': text_node.url}, data=text_node.text)
        elif text_node.text_type == text_type_image:
            return LeafNode(tag='img', data='', props = {'src': text_node.url, 'alt': text_node.text})
        else:
            raise Exception('Invalid text type')

        
