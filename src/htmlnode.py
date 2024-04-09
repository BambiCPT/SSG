class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html_attributes = ''
        for prop, value in self.props.items():
            html_attributes += f"{prop}='{value}'"

        return html_attributes.strip()
    
    def __repr__(self):
        return f'HTMLnode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})'
    
class LeafNode(HTMLnode):
    def __init__(self, tag=None, data=None, props=None):
        super().__init__(tag=tag, value=data, props=props)
        

    def to_html(self):
        if self.value == None:
            raise ValueError('Value cannot be None for a leaf node')
        elif self.tag == None:
            return str(self.value)
        else:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>' if self.props else f'<{self.tag}>{self.value}</{self.tag}>'
        
class ParentNode(HTMLnode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
        if children == None:
            raise ValueError('Children cannot be None for a parent node')
        if tag == None:
            raise ValueError('Children cannot be None for a parent node')

    def to_html(self):
        children_html = ''
        for child in self.children:
            children_html += child.to_html()
        return f'<{self.tag}>{children_html}</{self.tag}>'
        


