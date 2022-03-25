import numpy as np
import csv

def ExtractFile(path) :
    with open(path,newline=None) as file :
        filereader = list(csv.reader(file))
        filereader = list(map(lambda x : float(x[i]) for i in range(len(x)),filereader))
        print(filereader)
        del filereader[0]
        # return np.array(filereader)
        return filereader

class Unit :
    def __init__(self,extract: np.array):
        self.training_data = extract
    
    def Fitness(self, test_data : np.array):

        pass






if __name__ == "__main__":
    path = "position_sample.csv"
    extract = ExtractFile(path)
    print(extract[0][0][0])
    pass