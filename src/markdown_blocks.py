
from enum import Enum

class BlockType(Enum):
    """meaningful controlled constant's rather than passing strings everywhere."""
    PARAGRAPH = "paragraph"
    HEADING =   "heading" 
    CODE =      "code"
    QUOTE =     "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(line):
    if line.startswith("#"):
        headings_count = 0
        for i in line:
            if i == "#":
                headings_count += 1
                continue
            break
            
        if headings_count >= 1 and headings_count <= 6:
            if len(line) <= headings_count + 1:
                return False
            if line[headings_count] == " " and line[headings_count+1] != " ":
                return True
    return False

def validate_quote_block(lines):
    # print(mk.splitlines())
    for m in lines.splitlines():
        if m.strip()[0] != ">":
            return False
    return True

def is_unordered_list(lines):
    for line in lines.split("\n"):
        if line.startswith("-") and len(line.split()) > 1:
            continue
        else:
            return False
    return True

def is_ordered_list(lines):
    for i, line in enumerate(lines.split("\n"), start=1):
        if len(line.split()) < 2:
            return False
        if line[0] != i and line[1] != ".":
            return False
    return True

def block_to_block_type(mk): 
    if is_heading(mk):
        return BlockType.HEADING    
    if mk.startswith("```") and mk.endswith("```"):
        return BlockType.CODE
    if validate_quote_block(mk):
        return BlockType.QUOTE
    if is_unordered_list(mk):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(mk):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH


if __name__ == "__main__":
    pass
