# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def generate(nested_list):
            for e in nested_list:
                if e.isInteger():
                    yield e.getInteger()
                else:
                    for ep in generate(e.getList()):
                        yield ep
                        
        self.generator = generate(nestedList)
        self.next_element = None

    def next(self):
        if self.next_element is not None:
            return_element = self.next_element
            self.next_element = None
            return return_element
        return next(self.generator)

    def hasNext(self):
        if self.next_element is not None:
            return True

        try:
            self.next_element = next(self.generator)
        except StopIteration:
            return False
        return True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())