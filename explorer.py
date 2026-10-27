from textual.widgets import Tree

class Folder:
    def __init__(self, name='default'):
        self.name = name
        self.files = []
        self. folders = []

    def add(self, object):
        if isinstance(object, File):
            self.files.append(object)
        elif isinstance(object, Folder):
            self.folders.append(object)

    def remove(self, object):
        if isinstance(object, str):
            for e in self.files:
                if e.name == object : 
                    self.files.remove(e)
                    return
            for e in self.folders:
                if e.name == object : 
                    self.folders.remove(e)
                    return
        else : 
            try :
                self.files.remove(object)  
            except :
                self.folders.remove(object)

    def toTree(self, node=None):
        newTree = node is None
        if node is None:
            tree = Tree(self.name, self)
            tree.auto_expand = False
            node = tree.root
        for e in self.files:
            node.add_leaf(e.name, e)
        for e in self.folders :
            subNode = node.add(e.name, e)
            e.toTree(node=subNode)
        if newTree :
            return tree
        
        
class File:
    def __init__(self, name):
        self.name = name