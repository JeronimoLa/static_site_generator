from inline_markdown import markdown_to_blocks, text_to_textnodes, TextNode, TextType
from markdown_blocks import block_to_block_type, BlockType
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode


def markdown_to_html_node(markdown):
    sections = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
    
        html_nodes = []
        
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            code_text = "\n".join(block.splitlines()[1:-1])+"\n"
            text_nodes = [TextNode(code_text, TextType.CODE)]

        else:
            block = " ".join(block.splitlines())
            text_nodes = text_to_textnodes(block)
            
        
        for text_node in text_nodes:
            html = text_node_to_html_node(text_node)
            html_nodes.append(html)

        paragraph_node = ParentNode(block_type.value, html_nodes)
        sections.append(paragraph_node)
        
    parent_node = ParentNode("div", sections)
        
    return parent_node
        
if __name__ == "__main__":
    md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item    
    
"""
#     md = """
# ```
# This is text that _should_ remain
# the **same** even with inline stuff
# ```
# """

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