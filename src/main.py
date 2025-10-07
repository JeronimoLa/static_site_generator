import os, shutil, time, sys
from page_generation import generate_page


def main():
    base_path = ""
    if len(sys.argv) == 2:
        base_path = sys.argv[1]
    else:
        base_path = "/"

    # top_level_path = os.path.abspath(os.path.join(cwd, os.pardir))
    cwd = os.getcwd()
    source_path = cwd + "/static/"
    dest_path = cwd + "/docs/"
    from_path = cwd + "/content"
    template_path = cwd + "/template.html"
    
    cp_contents_to_dir(source_path, dest_path)
    generate_page(from_path, template_path, dest_path, base_path)

def cp_contents_to_dir(source_dir, dest_dir, first_call=True):
    if first_call and os.path.exists(dest_dir):
        for filename in os.listdir(dest_dir):
            file_path = os.path.join(dest_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(filename, "is removed")
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)
                
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    
    for content in os.listdir(source_dir):        
        path = os.path.join(source_dir, content)

        if os.path.isfile(path):
            shutil.copy(path, dest_dir)
            
        if os.path.isdir(path):
            dir_path = dest_dir + content
            cp_contents_to_dir(path, dir_path, first_call=False)
            
            
if __name__ == "__main__":
    main()