import re
from textnode import TextNode, TextType

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
    pattern = r'\s+!\[(.+?)\]\((https:[^)]*)\)'
    return [ match for match in re.findall(pattern, text) ]

def extract_markdown_links(text): 
    pattern = r'(?<!!)\[(.+?)\]\((https:[^)]*)\)'
    return [ match for match in re.findall(pattern, text) ]

if __name__ == "__main__":
    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_images(text)) # should print
    print(extract_markdown_links(text)) # should not
 
    # print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    