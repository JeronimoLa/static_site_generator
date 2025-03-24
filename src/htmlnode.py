from typing import Optional

class HTMLNode:
    
    def __init__(self, 
                tag: Optional[str] = None,
                value: Optional[str] = None,
                children: Optional[list] = None,
                props: Optional[dict] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attributes = ""
        for k, v in self.props.items():
	        formatted_str = f'{k}="{v}" '
	        attributes += formatted_str

        return attributes

    def __repr__(self, obj):
        print(f"{obj.tag},\n {obj.value},\n  {obj.children},\n {obj.props},\n")


class LeafNode(HTMLNode):
    def __init__(self, tag:Optional[str] = None, value:str = None):
        super().__init__(tag, value)
    
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        


