from .base import NonRecursiveTreeWalker

class TreeWalker(NonRecursiveTreeWalker):
    def getNodeDetails(self, node): ...
    def getFirstChild(self, node): ...
    def getNextSibling(self, node): ...
    def getParentNode(self, node): ...
