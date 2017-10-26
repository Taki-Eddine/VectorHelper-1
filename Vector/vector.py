#!/usr/bin/python3
import sys
import os

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

    def Mult2(self):
        """Multiplies all vector elements by 2
        
        Returns:
            a list of the vectors elements multiplied by 2
        """
        for i in range(0, self.size):
            self.__elements[i] = self.__elements[i] * 2
        return self.__elements      
    
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

        if self.size != other.size:
            raise SizeException
        else: 
            sum = list()
            for i in range(0, self.size):
                sum.append(str(self.__elements[i] + other.__elements[i]))
            return VectorHelper(' '.join(sum))

    def __add__(self, other):
        if self.size != other.size:
            raise SizeException
        else:
            sum = list()
            for i in range(0, self.size):
                sum.append(str(self.__elements[i] + other.__elements[i]))
            return VectorHelper(' '.join(sum))
                


    

class SizeException(Exception):
    """Exception class raised when two sizes are different"""
    pass


def main():
    print("_________________________ WELCOME TO VETOR HELPER ________________________ ")
    print("__________________________________________________________________________ ")
    
    vec1 = input("Enter Your Vector: \n ")
    vec1 = VectorHelper(vec1)
    while(1):
	os.system("cls" if os.name == "nt" else "clear")
        print("\n______________________________ MENU ______________________________________\n")
        print("1- Tri du vecteur")
        print("2- inverser le vecteur")
        print("3- Min et Max du vecteur")
        print("4- Multiplier le vecteur par 2")
        print("5- Ajouter un autre vecteur")
        print("6- Nouveau vecteur")
        print("7- Quitter")
        print("__________________________________________________________________________ ")
        answer = input("Votre Choix:\t ")
        if answer == "1" :
            vec1.sort()
            print(vec1.get_elements)    
    
        if answer == "2" :
            print(vec1.inverse())
    
        if answer == "3" :
            print(vec1.MinMax())

        if answer == "4" :
            print(vec1.Mult2())

        if answer == "5" :   
            vec2 = input("enter second  vector: \n")
            vec2 = VectorHelper(vec2)
            try:
                print(vec1.somme(vec2).get_elements)
            except SizeException:
                print("Size of vectors are different")
       
        if answer == "6" :        
            vec1 = input("Enter Your Vector: \n ")
            vec1 = VectorHelper(vec1)
        if answer == "7" :
            sys.exit(0)    

if __name__ == "__main__":
    main()
