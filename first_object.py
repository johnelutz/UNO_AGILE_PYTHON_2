"""
Author: John Lutz
Description: first Class created for UNO Agile Python 2
"""

class My_Obj():
    """
    Title: My_Obj
    Description: This object is meant to demo the basics of classes
    Arguments: name, importance
    Returns: This object returns nothing at all
    """

    def __init__(self, name, importance):
        self.name = name
        self.importance = importance

    def show(self):
        print(self.name, self.importance)

    def mod_name(self, name):
        self.name = name
