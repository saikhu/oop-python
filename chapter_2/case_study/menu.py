import sys

from .notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }
    
    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Note
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    def run(self):
        '''Display the menu and resond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice.".format(choice))
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
            
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        if notes:
            self.show_notes(notes)
        else:
            print("No Note found.")

    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")
    
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")

        if memo:
            # Adition from myself book did do that.
            modified = self.notebook.modify_note(id, memo, tags)
            if modified:
                print("The note is successfully modified.")
        # if memo:
        #     self.notebook.modify_memo(id, memo)
        # if tags:
        #     self.notebook.modify_tags(id, tags)
        
    def quit(self):
        print("Thank you for using notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
        