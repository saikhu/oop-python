import datetime 

# Store the next available id for all new notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a string in seachers and store tags for each note.'''

    def __init__(self, memo, tags=''):
        '''Intialize a note with memo and optional space-separated tags. Automatically set the notes's creation date and a unique id.'''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter text. Return True if it matches, False otherwies.
        
        Search is case sensitive and matches both text and tags.'''
        return filter in self.memo or filter in self.tags
    

class Notebook:
    '''Represent a collection of notes that can be tagged, motdified, and searched.'''

    def __init__(self):
        '''Intialize a notebook with an empty list.'''
        self.notes = []
    
    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        print("Could not find the note.")
        return None    

    def modify_memo(self, note_id, memo):
        '''Find the note with given id and changes it's memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
        # self._find_note(note_id).memo = memo

    def modify_tags(self, note_id, tags):
        '''Find the note with given id and chages its tags to the given tags.'''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''Find all the notes that matches the given filter string.'''
        
        return [note for note in self.notes if note.match(filter)]
    
