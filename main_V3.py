# from re import A
from dataclasses import replace
import numpy as np
import csv
import time
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


class Unit :
    def __init__(self,extract: np.array,ind :int):
        self.ind = ind
        self.training_data = extract
        self.coeff = 10
        self.p1 = np.random.uniform(-100,100,self.ind)
        self.p2 = np.random.uniform(-100,100,self.ind)
        self.p3 = np.random.uniform(-100,100,self.ind)
        self.p4 = np.random.uniform(-100,100,self.ind)
        self.p5 = np.random.uniform(-100,100,self.ind)
        self.p6 = np.random.uniform(-100,100,self.ind)

        self.Sort()
        
    
    def Fitness(self):
        distance = np.zeros(self.ind)
        for i in self.training_data :
            x = self.p1 * np.sin(self.p2*i[0] + self.p3)
            y = self.p4 * np.sin(self.p5*i[0] + self.p6)
            distance +=  np.sqrt((i[1]-x)**2 + (i[2]-y)**2)
        self.fitness = distance
        

    def Cross(self) :
        upper_percent = 0.6
        lower_percent = 0.3
        upper_bound = int(self.ind*upper_percent)
        lower_bound = int(self.ind*lower_percent)
        upper = int(self.ind*(0.2))
        lower = 0
        size_sample = upper_bound - lower_bound
        stock = 1/((np.arange(lower,upper)+1))
        s = np.sum(stock)
        keys = np.random.choice(np.arange(lower,upper),size_sample,replace= True, p=stock/s) 
 
        self.p2[lower_bound:upper_bound] = np.take(self.p2,keys)
        self.p1[lower_bound:upper_bound] = np.take(self.p1,keys)
        self.p3[lower_bound:upper_bound] = np.take(self.p3,keys)
        keys = np.random.choice(np.arange(lower, upper),size_sample,replace= True, p=stock/s) 

        self.p4[lower_bound:upper_bound] = np.take(self.p4,keys)
        self.p5[lower_bound:upper_bound] = np.take(self.p5,keys)
        self.p6[lower_bound:upper_bound] = np.take(self.p6,keys)
        

    def Sort(self):
        self.Fitness()
        keys = np.argsort(self.fitness)
        self.fitness = np.take(self.fitness,keys)
        self.p1 = np.take(self.p1,keys)
        self.p2 = np.take(self.p2,keys)
        self.p3 = np.take(self.p3,keys)
        self.p4 = np.take(self.p4,keys)
        self.p5 = np.take(self.p5,keys)
        self.p6 = np.take(self.p6,keys)

       


    def Avg_Fitness(self):
        
        
        
        return np.mean(self.fitness)

    def Mutations(self):
        delta=100
        par = 0.5
        rate = 0.25
        upper_percent = 0.3
        lower_percent = 0.0
        lower_bond = int(self.ind*lower_percent)
        upper_bond = int(self.ind*upper_percent)
        size_sample = upper_bond - lower_bond
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p1[lower_bond:upper_bond] =  np.clip(self.p1[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p1[lower_bond:upper_bond] =  np.clip(self.p1[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p2[lower_bond:upper_bond] =  np.clip(self.p2[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p2[lower_bond:upper_bond] =  np.clip(self.p2[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p3[lower_bond:upper_bond] =  np.clip(self.p3[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p3[lower_bond:upper_bond] =  np.clip(self.p3[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p4[lower_bond:upper_bond] =  np.clip(self.p4[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p4[lower_bond:upper_bond] =  np.clip(self.p4[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p5[lower_bond:upper_bond] =  np.clip(self.p5[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p5[lower_bond:upper_bond] =  np.clip(self.p5[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p6[lower_bond:upper_bond] =  np.clip(self.p6[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        # self.p6[lower_bond:upper_bond] =  np.clip(self.p6[lower_bond:upper_bond] + (temp * np.random.uniform(-par,par,size_sample)),-delta,delta)




        
         

    def Iterate(self):
        lower_percent = 0.6
        upper_percent = 1
        lower_bound = int(self.ind*lower_percent)
        upper_bound = self.ind 
        size_sample = upper_bound - lower_bound
        self.p1[lower_bound:] = np.random.uniform(-100,100,size_sample)
        self.p2[lower_bound:] = np.random.uniform(-100,100,size_sample)
        self.p3[lower_bound:] = np.random.uniform(-100,100,size_sample)
        self.p4[lower_bound:] = np.random.uniform(-100,100,size_sample)
        self.p5[lower_bound:] = np.random.uniform(-100,100,size_sample)
        self.p6[lower_bound:] = np.random.uniform(-100,100,size_sample)



        
        
        
    

    def Generation(self):
        
        try : 
            counter = 0
            while self.fitness[0]> 4.2:
                start = time.time()
                
                self.Mutations()
                self.Cross()
                self.Iterate()
                self.Sort()
                stop = time.time()
                
                if counter%100==0:
                    print("temp",self.fitness[0])
                    print("Avg :",self.Avg_Fitness())
                    print("Time",stop-start)
                counter += 1
                print("counter",counter)
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0]
        except KeyboardInterrupt:
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0]
        
        

                        


    
    

        






if __name__ == "__main__":

    path = "position_sample.csv"
    extract = ExtractFile(path)
    IA = Unit(extract,20000)
    result = IA.Generation()
    print("result :",result)
    for i in range(len(extract)):
        plt.scatter(extract[i][1],extract[i][2],color ='red')
        plt.scatter(result[0]* np.sin(result[1]*extract[i][0] + result[2]),result[3]* np.sin(result[4]*extract[i][0] + result[5]),color='blue' )
    plt.show()

    pass