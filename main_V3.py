# from re import A
from dataclasses import replace
import numpy as np
import math
import csv

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
        self.ind = ind
        self.training_data = extract
        self.coeff = 10
        self.p1 = 200*np.random.random(ind) -100
        self.p2 = 200*np.random.random(ind) -100
        self.p3 = 200*np.random.random(ind) -100
        self.p4 = 200*np.random.random(ind) -100
        self.p5 = 200*np.random.random(ind) -100
        self.p6 = 200*np.random.random(ind) -100
        self.fitness = self.Fitness(self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.ind)
        self.Sort()
        
    
    def Fitness(self,p1,p2,p3,p4,p5,p6,ind):
        distance = np.zeros(ind)
        for i in self.training_data :
            x = p1 * np.sin(p2*i[0] +p3)
            y = p4 * np.sin(p5*i[0] + p6)
            distance += np.sqrt((i[1]-x)**2 + (i[2]-y)**2)
        return distance
        

    def Cross(self) :
        keys = np.random.choice(np.arange(int(self.ind*0.1),int(self.ind*0.5)),int(self.ind*0.4),replace= False) 
 
        self.p2[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p2,keys)
        self.p1[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p1,keys)
        self.p3[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p3,keys)
        keys = np.random.choice(np.arange(int(self.ind*0.1),int(self.ind*0.5)),int(self.ind*0.4),replace= False) 

        self.p4[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p4,keys)
        self.p5[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p5,keys)
        self.p6[int(self.ind*0.1):int(self.ind*0.5)] = np.take(self.p6,keys)
        
        self.fitness[int(self.ind*0.1):int(self.ind*0.5)] = self.Fitness(self.p1[int(self.ind*0.1):int(self.ind*0.5)],self.p2[int(self.ind*0.1):int(self.ind*0.5)],self.p3[int(self.ind*0.1):int(self.ind*0.5)],self.p4[int(self.ind*0.1):int(self.ind*0.5)],self.p5[int(self.ind*0.1):int(self.ind*0.5)],self.p6[int(self.ind*0.1):int(self.ind*0.5)],int(self.ind*0.4))
        # p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp = self.Sort(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)
        # self.Compare(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)

    def Sort(self):
        keys = np.argsort(self.fitness)
        self.fitness = np.take(self.fitness,keys)
        self.p1 = np.take(self.p1,keys)
        self.p2 = np.take(self.p2,keys)
        self.p3 = np.take(self.p3,keys)
        self.p4 = np.take(self.p4,keys)
        self.p5 = np.take(self.p5,keys)
        self.p6 = np.take(self.p6,keys)
        # return p1,p2,p3,p4,p5,p6,fitness


    def Equal(results):
        # temp = True
        for i in range(1,len(results)):
            if results[i-1][0] != results[i][0] or results[i-1][1] != results[i][1] :
                return False
        return True
        
    # def Select(self):
    #     self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.fitness = Sort(self.p1,self.p2,self.p3,self.p4,self.p5,self.p6,self.fitness)
    #     self.p1 = self.p1[:self.ind]
    #     self.p2 = self.p2[:self.ind]
    #     self.p3 = self.p3[:self.ind]
    #     self.p4 = self.p4[:self.ind]
    #     self.p5 = self.p5[:self.ind]
    #     self.p6 = self.p6[:self.ind]
    #     self.fitness = self.fitness[:self.ind]

    # def Add_items(self,p1,p2,p3,p4,p5,p6,fitness):
    #     self.p1 = np.append(self.p1,p1)
    #     self.p2 = np.append(self.p2,p2)
    #     self.p3 = np.append(self.p3,p3)
    #     self.p4 = np.append(self.p4,p4)
    #     self.p5 = np.append(self.p5,p5)
    #     self.p6 = np.append(self.p6,p6)
    #     self.fitness = np.append(self.fitness,fitness)

    def Avg_Fitness(self):
        
        
        
        return np.mean(self.fitness)

    def Mutations(self):
        delta=100
        par = 20
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.8
        self.p1[:int(self.ind*0.1)] =  np.clip(self.p1[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.5
        self.p2[:int(self.ind*0.1)] =  np.clip(self.p2[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.5
        self.p3[:int(self.ind*0.1)] =  np.clip(self.p3[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.5
        self.p4[:int(self.ind*0.1)] =  np.clip(self.p4[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.5
        self.p5[:int(self.ind*0.1)] =  np.clip(self.p5[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)
        temp = np.random.random(int(self.ind*0.1))
        temp = temp<0.5
        self.p6[:int(self.ind*0.1)] =  np.clip(self.p6[:int(self.ind*0.1)] + (temp * np.random.normal(0,par,size=int(self.ind*0.1))),-delta,delta)

        self.fitness[:int(self.ind*0.1)] = self.Fitness(self.p1[:int(self.ind*0.1)],self.p2[:int(self.ind*0.1)],self.p3[:int(self.ind*0.1)],self.p4[:int(self.ind*0.1)],self.p5[:int(self.ind*0.1)],self.p6[:int(self.ind*0.1)],int(self.ind*0.1))
        # p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp = self.Sort(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)


        # self.Compare(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)
         
        



    def Compare(self,p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp):
        # fitness_temp = self.Fitness(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp)
        keep = self.fitness < fitness_temp
        self.p1 = keep * self.p1 + ~keep * p1_temp
        self.p2 = keep * self.p2 + ~keep * p2_temp
        self.p3 = keep * self.p3 + ~keep * p3_temp
        self.p4 = keep * self.p4 + ~keep * p4_temp
        self.p5 = keep * self.p5 + ~keep * p5_temp
        self.p6 = keep * self.p6 + ~keep * p6_temp
        self.fitness = keep * self.fitness + ~keep * fitness_temp
                
        
         

    def Iterate(self):
        self.p1[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.p2[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.p3[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.p4[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.p5[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.p6[int(self.ind*0.5):] = 200*np.random.random(int(self.ind*0.5)) -100
        self.fitness[int(self.ind*0.5):] = self.Fitness(self.p1[int(self.ind*0.5):],self.p2[int(self.ind*0.5):],self.p3[int(self.ind*0.5):],self.p4[int(self.ind*0.5):],self.p5[int(self.ind*0.5):],self.p6[int(self.ind*0.5):],int(self.ind*0.5))
        # p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp = self.Sort(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)

        # self.Compare(p1_temp,p2_temp,p3_temp,p4_temp,p5_temp,p6_temp,fitness_temp)


        
        
        
    

    def Generation(self):
        
        try : 
            counter = 0
            while self.fitness[0] > 10:

                
                self.Mutations()
                self.Cross()
                self.Iterate()
                self.Sort()


                if counter == 100:
                    # print("temp",save_result[0][0],save_result[0][1])
                    print("temp",self.fitness[0])
                    print("Avg :",self.Avg_Fitness())
                    counter = 0
                counter += 1
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0]
        except KeyboardInterrupt:
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0]
        
        

                        


    
    

        






if __name__ == "__main__":

    path = "position_sample.csv"
    extract = ExtractFile(path)
    # print(extract)
    IA = Unit(extract,1000)
    # print(IA.Fitness([50,4,5,60,1,2]))
    result = IA.Generation()
    print("result :",result)
    for i in range(len(extract)):
        plt.scatter(extract[i][1],extract[i][2],color ='red')
        plt.scatter(result[0]* np.sin(result[1]*extract[i][0] + result[2]),result[3]* np.sin(result[4]*extract[i][0] + result[5]),color='blue' )
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