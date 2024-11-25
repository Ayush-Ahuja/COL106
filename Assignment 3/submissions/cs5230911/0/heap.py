'''
Python Code to implement a heap with general comparison function
'''
def comp_1 (a,b):
    if a<b:
        return True
    else:
        return False
    
class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    
    def __init__(self, comparison_function= comp_1, init_array=None):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        if init_array is None:
            init_array = []
        self._comparator = comparison_function
        self._data = init_array[:]
        
    def insert(self, element):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self._data.append(element)
        self._upheap(len(self._data) - 1)
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.is_empty():
            raise Exception
        last = len(self._data) - 1
        self._swap(0, last)
        element = self._data.pop()
        self._downheap(0)
        return element
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.is_empty():
            raise Exception
        top_element = self._data[0]
        return top_element
    
    # You can add more functions if you want to
    def is_empty(self):
        return len(self._data) == 0
    
    def _parent(self, i):
        return (i - 1)//2

    def _left(self, j):
        return 2*j + 1

    def _right(self, j):
        return 2*j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0:
            comparision = self._comparator(self._data[j], self._data[parent])
            if comparision:
                self._swap(j, parent)
                self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                comparision1 = self._comparator(self._data[right], self._data[left])
                if comparision1:
                    small_child = right
            comparision2 = self._comparator(self._data[small_child], self._data[j])
            if comparision2:
                self._swap(j, small_child)
                self._downheap(small_child)

    def update_top(self, value):
        if self.is_empty():
            raise Exception
        else:
            self._data[0] = value