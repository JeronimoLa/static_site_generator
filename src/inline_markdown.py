import re
from textnode import TextNode, TextType

LINK_RE= re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
IMAGE_RE = re.compile(r"\s*!\[(.+?)\]\((https:[^)]*)\)")

def extract_markdown_images(text):
    return [ match for match in IMAGE_RE.findall(text) ]

def extract_markdown_links(text): 
    return [ match for match in LINK_RE.findall(text) ]

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    new_nodes = []
    for old_node in old_nodes:
        
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)
    print(f"New nodes: {new_nodes}")
    return new_nodes
        
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        pos = 0
        for m in LINK_RE.finditer(text):
            start, end = m.span()
            alt, url = m.group(1), m.group(2) 

            if start > pos:
                new_nodes.append(TextNode(text[pos:start], TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, url))
            pos = end

        if pos < len(text):
            new_nodes.append(TextNode(text[pos:], TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    lookup_table = {
        "`" : TextType.CODE,
        "**": TextType.BOLD,
        "_" : TextType.ITALIC
    }

    print(text)
    initial_node = TextNode(text, TextType.TEXT)
    for delimiter, text_type in lookup_table.items():
        if initial_node:
            node = [initial_node]
            initial_node = False
        new_nodes = split_nodes_delimiter(node, delimiter, text_type)
        node = new_nodes

    nodes = split_nodes_image(node)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(mk):
    filtered_blocks = []
    blocks = mk.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())

    return filtered_blocks


def print_nodes(node):
    for n in node:
        print(n)


if __name__ == "__main__":
    mk = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
    markdown_to_blocks(mk)

    # print_nodes(new_nodes)
