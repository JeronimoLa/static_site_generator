from inline_markdown import markdown_to_blocks, text_to_textnodes, TextNode, TextType
from markdown_blocks import block_to_block_type, BlockType
from textnode import text_node_to_html_node
from htmlnode import LeafNode, ParentNode

import time

def get_html_nodes(text_nodes): 
    html_nodes = []
    for text_node in text_nodes:
        html = text_node_to_html_node(text_node)
        html_nodes.append(html)
    return html_nodes

def paragraph_block_to_html(block):
    block = " ".join(block.splitlines())
    text_nodes = text_to_textnodes(block)
    html_nodes = get_html_nodes(text_nodes)
    return ParentNode("p", html_nodes)

def code_block_to_html(block):
    code_text = "\n".join(block.splitlines()[1:-1])+"\n"
    text_nodes = [TextNode(code_text, TextType.CODE)]
    html_nodes = get_html_nodes(text_nodes)
    return ParentNode("pre", html_nodes)
    
def heading_block_to_html(block): 
    block_split = block.split()
    count = len(block_split[0])
    trimmed_block = " ".join(block_split[1:])
    text_nodes = text_to_textnodes(trimmed_block)
    html_nodes = get_html_nodes(text_nodes)
    return ParentNode(f"h{count}", html_nodes)

def quote_block_to_html(block):
    cleaned_text = "</br>".join([ block.strip("> ") for block in block.splitlines() ])
    text_nodes = text_to_textnodes(cleaned_text)
    html_nodes = get_html_nodes(text_nodes)
    node = ParentNode("p", html_nodes)
    return ParentNode("blockquote", [node])

def unordered_list_to_html(block):
    cleaned_text = [ block.strip("- ") for block in block.splitlines() ]
    list_nodes = []
    for text in cleaned_text:
        text_nodes = text_to_textnodes(text)
        html_nodes = get_html_nodes(text_nodes)
        list_nodes.append(ParentNode("li", html_nodes))
    return ParentNode("ul", list_nodes)

def ordered_list_to_html(block):
    cleaned_text = [ " ".join(block.split()[1:]) for block in block.splitlines() ]
    list_nodes = []
    for text in cleaned_text:
        wtf = text_to_textnodes(text)
        html_nodes = get_html_nodes(wtf)
        list_nodes.append(ParentNode("li", html_nodes))
    return ParentNode("ol", list_nodes)

def block_type_to_html(block_type: BlockType, block):
    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_block_to_html(block)
        case BlockType.CODE:
            return code_block_to_html(block)
        case BlockType.HEADING:
            return heading_block_to_html(block)
        case BlockType.QUOTE: 
            return quote_block_to_html(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html(block)
        case BlockType.ORDERED_LIST: 
            return ordered_list_to_html(block)

def markdown_to_html_node(markdown):
    sections = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:    
        html_nodes = []
        block_type = block_to_block_type(block)
        html_nodes = block_type_to_html(block_type, block)            
        sections.append(html_nodes)
    parent_node = ParentNode("div", sections)
    return parent_node
        
if __name__ == "__main__":
    md = """
1. First item
2. Second item
3. Third item

"""
   
    node = markdown_to_html_node(md)
    print(node.to_html())
    