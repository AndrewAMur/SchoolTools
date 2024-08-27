import os
from InquirerPy import prompt

NOTES_DIR = os.path.expanduser('~/.school')

def get_subject_dir(subject):
    return os.path.join(NOTES_DIR, subject)

def create_note(subject):
    title = prompt([{
        'type': 'input',
        'name': 'title',
        'message': 'Enter the note title (without .md)'
    }])['title']
    
    content_file = os.path.join(get_subject_dir(subject), f"{title}.md")
    os.system(f"nvim {content_file}")

def delete_note(subject):
    subject_dir = get_subject_dir(subject)
    notes = os.listdir(subject_dir)
    note_files = [f for f in notes if f.endswith('.md')]
    
    if not note_files:
        print("No notes found to delete.")
        return
    
    note_choices = [f[:-3] for f in note_files]
    
    choice = prompt([{
        'type': 'list',
        'name': 'note',
        'message': 'Select the note to delete',
        'choices': note_choices
    }])['note']
    
    os.remove(os.path.join(subject_dir, f"{choice}.md"))
    print(f"Note '{choice}.md' has been deleted.")

def edit_note(subject, note_name):
    note_file = os.path.join(get_subject_dir(subject), f"{note_name}.md")
    os.system(f"nvim {note_file}")

def list_notes(subject):
    subject_dir = get_subject_dir(subject)
    
    notes = sorted(
        [f for f in os.listdir(subject_dir) if f.endswith('.md')],
        key=lambda x: os.path.getmtime(os.path.join(subject_dir, x))
    )
    
    if not notes:
        print("No notes found.")
        return
    
    note_choices = [f[:-3] for f in notes]
    
    selected_note = prompt([{
        'type': 'list',
        'name': 'note',
        'message': 'Select a note',
        'choices': note_choices
    }])['note']
    
    action = prompt([{
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do with the selected note?',
        'choices': ['Edit', 'Return to Main Menu']
    }])['action']
    
    if action == 'Edit':
        edit_note(subject, selected_note)

