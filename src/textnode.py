text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.__text = text
        self.__text_type = text_type
        self.__url = url
    def __eq__(self, other): 
        if (self.__text == other.__text
            and self.__text_type == other.__text_type
            and self.__url == other.__url):
            return True
    def __repr__(self):
        return f'TextNode({self.__text}, {self.__text_type}, {self.__url})'

