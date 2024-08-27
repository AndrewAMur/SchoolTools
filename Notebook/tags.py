import os
from InquirerPy import prompt

TAGS_DIR = os.path.expanduser('~/.school/tags')

def ensure_tags_dir():
    if not os.path.exists(TAGS_DIR):
        os.makedirs(TAGS_DIR)

def add_tag(subject):
    ensure_tags_dir()
    
    note = prompt([{
        'type': 'input',
        'name': 'note',
        'message': 'Enter the note filename (without .md)'
    }])['note']
    
    tag = prompt([{
        'type': 'input',
        'name': 'tag',
        'message': 'Enter the tag'
    }])['tag']
    
    tag_file = os.path.join(TAGS_DIR, f"{tag}.txt")
    with open(tag_file, 'a') as f:
        f.write(f"{subject}/{note}.md\n")

def list_tags():
    ensure_tags_dir()
    
    tags = [f[:-4] for f in os.listdir(TAGS_DIR) if f.endswith('.txt')]
    
    if not tags:
        print("No tags found.")
        return
    
    selected_tag = prompt([{
        'type': 'list',
        'name': 'tag',
        'message': 'Select a tag to view notes',
        'choices': tags
    }])['tag']
    
    tag_file = os.path.join(TAGS_DIR, f"{selected_tag}.txt")
    if not os.path.exists(tag_file):
        print("No notes found for this tag.")
        return
    
    with open(tag_file, 'r') as f:
        notes = f.readlines()
    
    print(f"Notes for tag '{selected_tag}':")
    for note in notes:
        print(note.strip())

def search_by_tag(subject):
    tag = prompt([{
        'type': 'input',
        'name': 'tag',
        'message': 'Enter the tag'
    }])['tag']
    
    tag_file = os.path.join(TAGS_DIR, f"{tag}.txt")
    if not os.path.exists(tag_file):
        print("No notes found for this tag.")
        return
    
    with open(tag_file, 'r') as f:
        notes = f.readlines()
    
    for note in notes:
        print(note.strip())

def delete_tag():
    ensure_tags_dir()
    
    tags = [f[:-4] for f in os.listdir(TAGS_DIR) if f.endswith('.txt')]
    
    if not tags:
        print("No tags found to delete.")
        return
    
    tag_to_delete = prompt([{
        'type': 'list',
        'name': 'tag',
        'message': 'Select a tag to delete',
        'choices': tags
    }])['tag']
    
    tag_file = os.path.join(TAGS_DIR, f"{tag_to_delete}.txt")
    
    if os.path.exists(tag_file):
        os.remove(tag_file)
        print(f"Tag '{tag_to_delete}' has been deleted.")
    else:
        print("Tag not found.")

