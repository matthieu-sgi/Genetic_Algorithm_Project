# from re import A
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
        # return float(distance_moyenne/len(self.training_data))
        return distance_moyenne

    def Cross(self,save_result : list) : 
        results = copy.deepcopy(save_result)
       
        

        for i in range(0,len(results)- len(results)%2,2):
            
            results[i][0],results[i+1][0] = results[i][0][:int(len(results[i][0])/2):] + results[i+1][0][int(len(results[i][0])/2)::],results[i+1][0][:int(len(results[i][0])/2):] + results[i][0][int(len(results[i][0])/2)::]
            results[i][1] = self.Fitness(results[i][0])
            results[i+1][1] = self.Fitness(results[i+1][0])
        
        return results.sort(key=lambda x : x[1], reverse = False)

    def Equal(results):
        # temp = True
        for i in range(1,len(results)):
            if results[i-1][0] != results[i][0] or results[i-1][1] != results[i][1] :
                return False
        return True
        

    def Avg_Fitness(results):
        avg= 0
        print(results[0])
        for i in results:
            avg += i[1]
        return float(avg/len(results))

    def Mutations(self, save_result : list):
        results = copy.deepcopy(save_result)

        for i in results :
            temp = int(random.randint(0,len(i[0])))
            for j in range(temp,int(random.randint(0,len(i[0])))):
                i[0][j]+=  random.uniform(-50,50) #Change values random.uniform(a,b) if you want a wider mutation
            i[1] = self.Fitness(i[0])
        return results.sort(key=lambda x : x[1], reverse = False)

    def Compare(save_result : list, temp : list):
        for i in range(len(save_result)) :

            if(save_result[i][1]>temp[i][1]) :
                save_result.insert(i)
            
                
                
        
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
        counter = 0
        temp_bool = False
        try : 
            while not temp_bool :

                
                # save_result_temp = self.Iterate(it_bygen)
   
                
                # Unit.Compare(save_result, save_result_temp)
                
                
                # save_result_temp = self.Mutations(save_result)
                
                # Unit.Compare(save_result, save_result_temp)
                
                print(1)
                temp_bool = Unit.Equal(save_result)
                save_result_temp = self.Cross(save_result)
                print(2)
                temp_bool = Unit.Equal(save_result)
                Unit.Compare(save_result, save_result_temp)
                print(3)
                temp_bool = Unit.Equal(save_result)

                if counter == 1000:
                    # print("temp",save_result[0][0],save_result[0][1])
                    print("temp",save_result)
                    print("Avg :",Unit.Avg_Fitness(save_result))
                    counter = 0
                counter += 1
        except KeyboardInterrupt:
            return save_result[0]
        
        

                        


    
    

        






if __name__ == "__main__":

    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract)
    # print(IA.Fitness([50,4,5,60,1,2]))
    result = IA.Generation(20)
    print("result :",result)
    # print(Unit.Equal([[[1,2,3],1], [[1,2,3],2]]))
    # temp = [[[2,4,6,10,11,23],10],[[5,7,8,9,10,1],15]]
    # temp = IA.Iterate(5)
    # print(temp)
    # print(Unit.Avg_Fitness(temp))

    # print(IA.Cross(temp))
    # Affiche(temp)
    # print(Unit.Compare(temp,[[[5,10,15,20,25],5],[[],20]]))
    # print(temp)
    # print(IA.Iterate())
    pass