import os
from InquirerPy import prompt
from notes import create_note, delete_note, edit_note, list_notes
from tags import add_tag, search_by_tag, list_tags, delete_tag

def main():
    subject = prompt([{
        'type': 'list',
        'name': 'subject',
        'message': 'Choose a subject',
        'choices': ['Chemistry', 'Computer', 'English', 'French', 'Greek', 'Mathematics', 'Physics']
    }])['subject']

    action = prompt([{
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': ['Create Note', 'Delete Note', 'Edit Note', 'List Notes', 'Add Tag', 'Search by Tag', 'List Tags', 'Delete Tag', 'Exit']
    }])['action']

    if action == 'Create Note':
        create_note(subject)
    elif action == 'Delete Note':
        delete_note(subject)
    elif action == 'Edit Note':
        list_notes(subject)
    elif action == 'List Notes':
        list_notes(subject)
    elif action == 'Add Tag':
        add_tag(subject)
    elif action == 'Search by Tag':
        search_by_tag(subject)
    elif action == 'List Tags':
        list_tags()
    elif action == 'Delete Tag':
        delete_tag()
    elif action == 'Exit':
        exit()

if __name__ == '__main__':
    main()

