import re, time
from textnode import TextNode, TextType

LINK_RE= re.compile(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)")
IMAGE_RE = re.compile(r"\s*!\[(.+?)\]\((https:[^)]*)\)")

def split_nodes_delimiter(old_nodes, delimiter, text_type) -> list[TextNode]:
    new_nodes= []
    words = []
    delimiter_count = 0
    for node in old_nodes:
        # text_string = node.text.split()
        for i, word_text in enumerate(node.text.split()):
            if delimiter in word_text:
                delimiter_count += 1

                if words and delimiter_count < 2:
                    new_nodes.append(TextNode(" ".join(words), TextType.TEXT))
                    words = []
                
                words.append(word_text.strip(delimiter))
                if delimiter_count % 2 == 0 and words:
                    code_text = " ".join(words)
                    new_nodes.append(TextNode(code_text, text_type))
                    words = []
                    delimiter_count = 0

            elif delimiter_count >= 1:
                words.append(word_text)
            
            else:
                words.append(word_text)

            if i == len(node.text.split()) -1:
                new_nodes.append(TextNode(" ".join(words), TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return [ match for match in IMAGE_RE.findall(text) ]

def extract_markdown_links(text): 
    return [ match for match in LINK_RE.findall(text) ]

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        text = node.text
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

# def split_nodes_image(old_nodes):
#     new_nodes = []
#     for node in old_nodes:
#         text = node.text
#         pos = 0
#         for m in IMAGE_RE.finditer(text):
#             start, end = m.span()
#             alt, url = m.group(1), m.group(2) 

#             if start > pos:
#                 new_nodes.append(TextNode(text[pos:start], TextType.TEXT))
#             new_nodes.append(TextNode(alt, TextType.IMAGE, url))
#             pos = end

#         if pos < len(text):
#             new_nodes.append(TextNode(text[pos:], TextType.TEXT))

#     return new_nodes


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

if __name__ == "__main__":
    pass