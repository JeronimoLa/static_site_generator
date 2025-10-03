from inline_markdown import markdown_to_blocks, text_to_textnodes
from markdown_blocks import block_to_block_type
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode

import time 

def markdown_to_html_node(markdown):
    sections = []
    blocks = markdown_to_blocks(markdown)
    # print(blocks)
    for block in blocks:
    
        html_nodes = []
        
        block_type = block_to_block_type(block) # type paragrah
        # this will be what tells me the inside element within the div is ""
        text_nodes = text_to_textnodes(block)
        # print(text_nodes)
        
        for text_node in text_nodes:
            html = text_node_to_html_node(text_node)
            # print(type(html))
            html_nodes.append(html)
            # if html.tag is None:
                # node = LeafNode("p", html.value)
                # print(node.to_html())
            
                # print("here")
        # print(len(html_nodes))
        paragraph_node = ParentNode(block_type.value, html_nodes)
        # print(paragraph_node.to_html())
        sections.append(paragraph_node)
        # print(parent_node.tag)
        
    parent_node = ParentNode("div", sections)
        
    # print(parent_node.to_html())
    return parent_node

    # time.sleep(100)
        

        
    
    
    
if __name__ == "__main__":
    md = """ 
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
    node = markdown_to_html_node(md)
    print(node.to_html())
    
    




    # <p>This is <b>bolded</b> paragraph text in a p tag here</p>    
# </div>""" 
    # grandchild_node = LeafNode(None, "BEFORE")
    # grandchild_node1 = LeafNode("b", "BOLDED")
    # grandchild_node2 = LeafNode(None, "AFTER")
    # parent_node = ParentNode("div", [grandchild_node, grandchild_node1, grandchild_node2])
    # print(parent_node.to_html())
# <div>