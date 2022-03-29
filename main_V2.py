# from re import A
import numpy as np
import math
import csv
import random
import copy
import matplotlib.pyplot as plt
import math

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
    def __init__(self,extract: np.array,ind :int):
        self.training_data = extract
        self.p1 = 200*np.random.random(ind) -100
        self.p2 = 200*np.random.random(ind) -100
        self.p3 = 200*np.random.random(ind) -100
        self.p4 = 200*np.random.random(ind) -100
        self.p5 = 200*np.random.random(ind) -100
        self.p6 = 200*np.random.random(ind) -100
        self.fitness = self.Fitness()
        self.ind = ind
    
    def Fitness(self,p1,p2,p3,p4,p5,p6):
        x = p1 * np.sin(p2*self.training_data[0] +p3)
        y = p4 * np.sin(p5*self.training_data[0] + p6)
        return (self.training_data[1]-x)**2 + (self.training_data[2]-y)**2
        

    def Cross(self) : 
        

        

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

    def Mutations(self):
        delta=10 
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p1_temp =  np.clip(self.p1 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p2_temp =  np.clip(self.p2 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p3_temp =  np.clip(self.p3 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p4_temp =  np.clip(self.p4 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p5_temp =  np.clip(self.p5 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        temp = np.random.random(self.ind)
        temp = temp<0.5
        p6_temp =  np.clip(self.p6 + (temp * 200*np.random.random(self.ind) -100),-delta,delta)
        

        self.Compare(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp)
         
        



    def Compare(self,p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp):
        # fitness_temp = self.Fitness(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp)
        keep = self.fitness < self.Fitness(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp)
        self.p1 = keep * self.p1 + ~keep * p1_temp
        self.p2 = keep * self.p2 + ~keep * p2_temp
        self.p3 = keep * self.p3 + ~keep * p3_temp
        self.p4 = keep * self.p4 + ~keep * p4_temp
        self.p5 = keep * self.p5 + ~keep * p5_temp
        self.p6 = keep * self.p6 + ~keep * p6_temp
                
        
         

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
            while save_result[0][1] > 10:

                # save_result_temp.clear()
                
                # save_result_temp.extend(self.Iterate(it_bygen))
                save_result_temp = self.Iterate(it_bygen)
                
                Unit.Compare(save_result, save_result_temp)
                
                
                # save_result_temp.clear()
                # save_result_temp.extend(self.Mutations(save_result))
                save_result_temp =self.Mutations(save_result)
                # print("C : ",save_result_temp)
                
                Unit.Compare(save_result, save_result_temp)
                # print("2 :", save_result_temp)
                
                # temp_bool = Unit.Equal(save_result)
                # save_result_temp.clear()
                # save_result_temp.extend(self.Cross(save_result))
                save_result_temp = self.Cross(save_result)
                Unit.Compare(save_result, save_result_temp)




                if counter == 50:
                    # print("temp",save_result[0][0],save_result[0][1])
                    print("temp",save_result[0][1])
                    print("Avg :",Unit.Avg_Fitness(save_result))
                    counter = 0
                counter += 1
            return save_result[0]
        except KeyboardInterrupt:
            return save_result[0]
        
        

                        


    
    

        






if __name__ == "__main__":

    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract)
    # print(IA.Fitness([50,4,5,60,1,2]))
    result = IA.Generation(50)
    print("result :",result)
    for i in range(len(extract)):
        plt.scatter(extract[i][1],extract[i][2],color ='red')
        plt.scatter(result[0][0]* np.sin(result[0][1]*extract[i][0] + result[0][2]),result[0][3]* np.sin(result[0][4]*extract[i][0] + result[0][5]),color='blue' )
    plt.show()
    # print(Unit.Equal([[[1,2,3],1], [[1,2,3],2]]))
    # temp = [[[2,-4,6,10,11,23],10],[[5,7,8,-9,10,1],15],[[3,2,1,-32,-12,16],20]]
    # while True:
    #     temp = IA.Mutations(temp)
    #     print("temp ", temp)
    # temp2 = [[[],3],[[],5],[[],20]]
    # temp = IA.Iterate(5)
    # print(temp)
    # print(Unit.Avg_Fitness(temp))

    # print(IA.Cross(temp))
    # Affiche(temp)
    # print(Unit.Compare(temp,temp2))
    # print(temp)
    # print(IA.Iterate())
    pass