"""The base application state."""

import pynecone as pc

class State(pc.State):
    """The base state."""
    show_right_0: bool = False
    show_right_1: bool = False
    show_right_2: bool = False
    show_right_3: bool = False
    show_right_4: bool = False
    show_right_5: bool = False
    show_right_6: bool = False
    show_right_7: bool = False
    show_right_8: bool = False
    show_right_9: bool = False
    show_right_10: bool = False
    show_right_11: bool = False
    show_right_12: bool = False
    show_right_13: bool = False
    show_right_14: bool = False
    
    def right_0(self):
        self.show_right_0 = not (self.show_right_0)
    
    def right_1(self):
        self.show_right_1 = not (self.show_right_1)

    def right_2(self):
        self.show_right_2 = not (self.show_right_2)
    
    def right_3(self):
        self.show_right_3 = not (self.show_right_3)
        
    def right_4(self):
        self.show_right_4 = not (self.show_right_4)

    def right_5(self):
        self.show_right_5 = not (self.show_right_5)
    
    def right_6(self):
        self.show_right_6 = not (self.show_right_6)

    def right_7(self):
        self.show_right_7 = not (self.show_right_7)
    
    def right_8(self):
        self.show_right_8 = not (self.show_right_8)
        
    def right_9(self):
        self.show_right_9 = not (self.show_right_9)
    
    def right_10(self):
        self.show_right_10 = not (self.show_right_10)
    
    def right_11(self):
        self.show_right_11 = not (self.show_right_11)

    def right_12(self):
        self.show_right_12 = not (self.show_right_12)
    
    def right_13(self):
        self.show_right_13 = not (self.show_right_13)
        
    def right_14(self):
        self.show_right_14 = not (self.show_right_14)