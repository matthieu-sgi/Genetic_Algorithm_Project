from re import A
import numpy as np
import math
import csv
import random
import copy

def ExtractFile(path) :
    
    with open(path,newline=None) as file :
        filereader = list(csv.reader(file,delimiter=';'))
        del filereader[0]
        
        temp = []
        for i in filereader:
            temp+= [[float(j) for j in i]]
        
       
        return temp

def Affiche(l : list):
    for i in l:
        
        print(i[1],end = ';')
    print()


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
        results = copy.deepcopy(save_result)
        cross_gen = []
        
        while len(cross_gen)==0 or  cross_gen[1]> results[-1][1] :
            temp = [random.uniform(-100,100) for i in range(6)]
            cross_gen = [temp,self.Fitness(temp)]


        for i in results: # I can change more than one parameter
            index_temp = random.randint(0,len(i[0])-1)
            i[0][index_temp] = cross_gen[0][index_temp]
            i[1] = self.Fitness(i[0])
        
        return results


                
                

    def Mutations(self, save_result : list):
        results = copy.deepcopy(save_result)

        for i in results :
            for j in range(len(i[0])):
                i[0][j]+=  random.uniform(-3,3) #Change values random.uniform(a,b) if you want a wider mutation
            i[1] = self.Fitness(i[0])
        return results

    def Compare(save_result : list, temp : list):
        for i in temp :
            # print("i : ",i[1])
            # print("save ",save_result[-1][1])

            if i[1] < save_result[-1][1]:
                # print("Je compare :", Affiche(temp), "et", Affiche(save_result))
                # print("temp")
                # Affiche(temp)
                # # print("save_result")
                # Affiche(save_result)
                save_result.pop()
                save_result.append(i)
                # print("save result",save_result[-1][1])

                save_result.sort(key=lambda x : x[1], reverse = False)
                
                
        print("end")
        Affiche(save_result)
        return save_result

    def Iterate(self,it):
        save_result=[]
        
        
        for i in range(it) :
            test_param = []
            [test_param.append(random.uniform(-100,100)) for i in range(6)]
            save_result.append([test_param,self.Fitness(test_param)])
            save_result.sort(key = lambda x: x[1],reverse = False)

        


        
        
        return save_result

    def Generation(self,it_bygen : int):
        save_result = self.Iterate(it_bygen)
        save_result_temp = []
        # while save_result[0][1] > 5.0 :
        for i in range(1):
            # print("1 : ", save_result[0][1])
            # print("Iterate")
            save_result_temp = self.Iterate(it_bygen)
            # print("2 : ", save_result[0][1])
            Unit.Compare(save_result, save_result_temp)
            # print("3 : ", save_result[0][1])
            # print("Mutations")
            save_result_temp = self.Mutations(save_result)
            # print("4 : ", save_result[0][1])
            Unit.Compare(save_result, save_result_temp)
            # print("5 : ",save_result[0][1])
            save_result_temp = self.Cross(save_result)
            # print("6 : ", save_result[0][1])
            Unit.Compare(save_result, save_result_temp)
            # print("7 : ", save_result[0][1])
            print("temp",save_result[0][1])
        return save_result[0]
        

                        


    
    

        






if __name__ == "__main__":
    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract)
    # print(IA.Fitness([50,4,5,60,1,2]))
    result = IA.Generation(3)
    print("result :",result)
    # temp = [[[2,4,6,10,11],10],[[],15],[[],14]]
    # Affiche(temp)
    # print(Unit.Compare(temp,[[[5,10,15,20,25],5],[[],20]]))
    # print(temp)
    # print(IA.Iterate())
    pass