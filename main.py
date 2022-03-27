import numpy as np
import math
import csv

def ExtractFile(path) :
    
    with open(path,newline=None) as file :
        filereader = list(csv.reader(file,delimiter=';'))
        del filereader[0]
        
        temp = []
        for i in filereader:
            temp+= [[float(j) for j in i]]
        
       
        return temp


class Unit :
    def __init__(self,extract: list):
        self.training_data = extract
    
    def Fitness(self, test_param : list):
        
        distance_moyenne = 0
        for i in self.training_data :
            t= i[0]
            x_test = test_param[0] * (np.sin(test_param[1] * t + test_param[2]))
            y_test = test_param[3] * (np.sin(test_param[4] * t + test_param[5]))
            distance_moyenne += math.sqrt((x_test-i[1])**2 + (y_test-i[2])**2)
        
        return float(distance_moyenne/len(self.training_data))

        






if __name__ == "__main__":
    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract)
    print(IA.Fitness([50,4,5,60,1,2]))
    pass