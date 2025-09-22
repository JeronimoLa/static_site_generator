import re
from htmlnode import TextNode, TextType, LeafNode
# from textnode import TextNode, TextType

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

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode(None, text_node.text)
            return node
        case TextType.BOLD:
            node = LeafNode("b", text_node.text)
            return node
        case TextType.ITALIC:
            node = LeafNode("i", text_node.text)
            return node
        case TextType.CODE:
            node = LeafNode("code", text_node.text)
            return node
        case TextType.LINK:
            node = LeafNode("a", text_node.text, {"href": "https://www.google.com"})
            return node
        case TextType.IMAGE:
            node = LeafNode("img", "", {"src": "https://www.google.com/image", "alt": "alt text"})
            return node

if __name__ == "__main__":
    node = TextNode("This is text with a **code block** word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
    for node in new_nodes:
        print(node)
        # self.assertEqual(new_nodes, [ TextNode("This is text with a ", TextType.TEXT),
                                    #   TextNode("code block", TextType.BOLD),
                                    #   TextNode(" word", TextType.TEXT),])