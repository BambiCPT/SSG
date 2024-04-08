class htmlnode:
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
    
class leafnode(htmlnode):
    def __init__(self, data):
        super().__init__(tag=None, value=None, props=None)
        self.value = data

    def to_html(self):
        if self.value == None:
            raise ValueError('Value cannot be None for a leaf node')
        elif self.tag == None:
            return str(self.value)
        else:
            return f'<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>'
        
leaf = leafnode(data='hello world')
leaf.tag = 'p'
leaf.props = {'class': 'greeting'}
print(leaf.to_html())



