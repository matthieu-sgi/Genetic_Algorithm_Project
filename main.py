import numpy as np
import math
import csv
import random

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

    def Cross(self,save_result : list) : 
        results = save_result
        cross_gen = []
        print(results)
        while len(cross_gen)==0 or  cross_gen[1]> results[-1][1] :
            print("Im in")
            temp = [random.uniform(-100,100) for i in range(6)]
            cross_gen = [temp,self.Fitness(temp)]


        for i in results: # I can change more than one parameter
            index_temp = random.randint(0,len(i[0]))
            i[0][index_temp] = cross_gen[0][index_temp]
            i[1] = self.Fitness(i[0])
        
        return results


                
                

    def Mutations(self, save_result : list):
        results = save_result
        for i in results :
            for j in range(len(i[0])):
                i[0][j]+=  random.uniform(-3,3) #Change values random.uniform(a,b) if you want a wider mutation
            i[1] = self.Fitness(i[0])
        return results


    def Iterate(self):
        save_result=[]
        save_result_temp = []
        
        for i in range(10) :
            test_param = []
            [test_param.append(random.uniform(-100,100)) for i in range(6)]
            save_result.append([test_param,self.Fitness(test_param)])
            save_result.sort(key = lambda x: x[1],reverse = False)

        # while len(save_result) == 0 or save_result[0][1] > 10.0 :
        
        
        return save_result

    
    

        






if __name__ == "__main__":
    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract)
    # print(IA.Fitness([50,4,5,60,1,2]))
    print(IA.Cross([[[1,2,3,4,5,21],IA.Fitness([1,2,3,4,5,21])]]))
    # print(IA.Iterate())
    pass