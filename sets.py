class Set():
    """Stores elements in a set, which does not allow duplicated values."""
    
    def __init__(self):
        """Creates an empty list to store elements."""
        self.elements = []
        
    def Contains(self, value):
        """Returns if value is in the set."""
        return (value in self.elements)
    
    def Add(self, value):
        """Adds an element to the set."""
        if value not in self.elements:
            self.elements.append(value)
            
    def Remove(self, value):
        """Removes an element from the set."""
        if value in self.elements:
            self.elements.remove(value)
            
    def Size(self):
        """Returns number of elements in the set."""
        return len(self.elements)
    
    def __or__(self, set_input):
        """Returns a new Set with all of the members 
        that were either in self.elements or set_input or both."""
        set_or = Set()
        for value in set_input.elements:
            set_or.Add(value)
        for value in self.elements:
            set_or.Add(value)
        return set_or
    
    def __and__(self, set_input):
        """Returns a new Set with the members that 
        were in both self.elements and set_input."""
        set_and = Set()
        for value in self.elements:
            if set_input.Contains(value):
                set_and.Add(value)
        return set_and
    
    def __sub__(self, set_input):
        """Returns a new Set with all of the members 
        that were in self.elements but not in set_input."""
        set_sub = Set()
        for value in self.elements:
            if not set_input.Contains(value):
                set_sub.Add(value)
        return set_sub