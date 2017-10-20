#!/usr/bin/python3


class VectorHelper(object):

    __elements = list()
    __size = list()

    def __init__(self, string_vector):
        self.__elements = list(map(float, self.__parse(string_vector)))
        self.__size = len(self.__elements)

    @staticmethod
    def __parse(string):

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
        """
            retourne les elements du vecteur 
        """
        return self.__elements

    @property
    def size(self):
        """
            retourne la taille du vecteur
        """
        return self.__size

    def MinMax(self):
        """
            Gives both Min and Max of Vector
            retourne le plus petit et le plus grand elements du vecteur 
        """
        min = self.__elements[0]
        max = min
        for i in range(1, self.size):
            if self.__elements[i] < min :
                min = self.__elements[i]
            if max < self.__elements[i] :     
                max = self.__elements[i]
              
        return min , max  
