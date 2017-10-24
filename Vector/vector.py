#!/usr/bin/python3


class VectorHelper(object):
    """Main class

    the class offers methods to opperate on vectors

    Attributes
        elements: a list which contains elemeents of the vector
        size: an int containing the number of elements
    """

    def __init__(self, string_vector):
        """inits VectorHelper with the elements of the vector and its size"""
        self.__elements = list()
        self.__size = 0
        
        self.__elements = list(map(float, self.__parse(string_vector)))
        self.__size = len(self.__elements)

    @staticmethod
    def __parse(string):
        """Takes the string entered by the user and turns it into a list of floats

        the string entered by the user must be containing numbers seperated with a letter or a symbole 
        the numbers mustn't be seperated with "-" or "."

        """
        component = ""
        i = 0
        temp_vector = list()
        while i < len(string):
            char = string[i]
            if char.isdigit() or char == "." or char == "-":
                component += string[i]
            else:
                if i != len(string) - 1:
                    if not string[i + 1].isdigit() and string[i + 1] != "." and string[i + 1] != "-":
                        pass
                    else:
                        temp_vector.append(component)
                        component = ""
            i += 1
        temp_vector.append(component)
        return temp_vector
    
    @property
    def get_elements(self):
        """Gets elements of Vector

        Returns:
            A list of the vector's elements.
        """
        return self.__elements

    @property
    def size(self):
        """Gets size of the vector
            
        Returns: 
            the size of the vector
        """
        return self.__size

    def MinMax(self):
        """Returns both Min and Max of Vector

        Returns:
             a tuple containing min and max values of the vector
        """
        min = self.__elements[0]
        max = min
        for i in range(1, self.size):
            if self.__elements[i] < min :
                min = self.__elements[i]
            if max < self.__elements[i] :     
                max = self.__elements[i]
              
        return min , max  
    def sort(self):
        """Sorts Elements of the vector"""

        for i in range(0, self.size - 1):
            for j in range (0 , self.size - i - 1):
                if self.__elements[j+1] < self.__elements[j] :
                    self.__elements[j] , self.__elements[j+1] = self.__elements[j+1] , self.__elements[j]
    
    def inverse(self):
        """Returns reversed elements of the vec

        Returns:
            a list containing reversed elements of vector
        Example:

            {(1,2,3)} ---> {(3,2,1)}
        """

        reversed = list()
        for i in range(1, self.size + 1):
            reversed.append(self.__elements[self.size - i])
        return reversed    
    
    def somme(self, other):
        """Returns sum of 2 vectors
        
        Adds two vectors element by elemen. if size of vectors is not the same 
        an exception is raised. 

        Args:
            Other: the list of elements we want to add to our vector

        Returns:
            a new list contaion the sum of the two vectors
        Example:

            self = {(1,2,3)} and other = {(2,3,4)}
            returns {(3,5,7)}
        
        Raises:
            SizeException: if the two vectors have different sizes.
        """

        if self.size != other.size :
            raise SizeException("la exception mon friend")
        else: 
            sum = list()
            for i in range(0, self.size):
                sum.append(self.__elements[i] + other.__elements[i] )
            return sum   
                

class SizeException(Exception):
    """Exception class raised when two sizes are different"""

    def __init__(self, msg=None):
        """inits SizeException with none"""
        super(msg)


