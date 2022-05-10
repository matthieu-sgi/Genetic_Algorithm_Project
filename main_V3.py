import numpy as np
import csv
import time
import matplotlib.pyplot as plt


def ExtractFile(path) : #Method to extract CSV and return a list
    
    with open(path,newline=None) as file :
        filereader = list(csv.reader(file,delimiter=';'))
        del filereader[0]
        
        temp = []
        for i in filereader:
            temp+= [[float(j) for j in i]]
        
       
        return temp


class Unit : #IA main class
    def __init__(self,extract: np.array,ind :int): #Constructor that initializes random values to parameter's numpy arrays
        self.ind = ind
        self.training_data = extract #Variable that stores the list of training data from position_sample
        self.coeff = 10
        self.p1 = np.random.uniform(-100,100,self.ind)
        self.p2 = np.random.uniform(-100,100,self.ind)
        self.p3 = np.random.uniform(-100,100,self.ind)
        self.p4 = np.random.uniform(-100,100,self.ind)
        self.p5 = np.random.uniform(-100,100,self.ind)
        self.p6 = np.random.uniform(-100,100,self.ind)

        self.Sort() #Sort the values
        
    
    def Fitness(self): #Fitness that sum euclidian distances
        distance = np.zeros(self.ind)
        for i in self.training_data :
            x = self.p1 * np.sin(self.p2*i[0] + self.p3)
            y = self.p4 * np.sin(self.p5*i[0] + self.p6)
            distance +=  np.sqrt((i[1]-x)**2 + (i[2]-y)**2)
        self.fitness = distance
        

    def Cross(self) : #Crossover's function
        upper_percent = 0.6
        lower_percent = 0.3
        upper_bound = int(self.ind*upper_percent)
        lower_bound = int(self.ind*lower_percent)
        upper = int(self.ind*(0.2))
        lower = 0
        size_sample = upper_bound - lower_bound
        stock = 1/((np.arange(lower,upper)+1)) #Weight to make interesting individuals cross more often in order to have better children
        s = np.sum(stock)
        keys = np.random.choice(np.arange(lower,upper),size_sample,replace= True, p=stock/s) #Random key to achieve the crossover
        self.p2[lower_bound:upper_bound] = np.take(self.p2,keys) # Apply the keys found
        self.p1[lower_bound:upper_bound] = np.take(self.p1,keys)
        self.p3[lower_bound:upper_bound] = np.take(self.p3,keys)
        keys = np.random.choice(np.arange(lower, upper),size_sample,replace= True, p=stock/s) 
        self.p4[lower_bound:upper_bound] = np.take(self.p4,keys)
        self.p5[lower_bound:upper_bound] = np.take(self.p5,keys)
        self.p6[lower_bound:upper_bound] = np.take(self.p6,keys)
        

    def Sort(self): #Sorting method buy fitness
        self.Fitness()
        keys = np.argsort(self.fitness) #Get the sorting keys
        self.fitness = np.take(self.fitness,keys)
        self.p1 = np.take(self.p1,keys) #Applying them
        self.p2 = np.take(self.p2,keys)
        self.p3 = np.take(self.p3,keys)
        self.p4 = np.take(self.p4,keys)
        self.p5 = np.take(self.p5,keys)
        self.p6 = np.take(self.p6,keys)

       


    def Avg_Fitness(self): #Average fitness function
        
        
        
        return np.mean(self.fitness)

    def Mutations(self): #Mutation method
        delta=100
        #Normal law parameter. 
        par = 0.1 #Working at 0.1
        #Selection rate parameter
        rate = 0.15 #Working at 0.15
        upper_percent = 0.3
        lower_percent = 0.0
        lower_bond = int(self.ind*lower_percent)
        upper_bond = int(self.ind*upper_percent)
        size_sample = upper_bond - lower_bond
        temp = np.random.random(size_sample) #Randomizing array of float values between 0 and 1
        temp = temp<rate #Transforming it into an array of booleans
        #Applying it to randomize the mutations
        self.p1[lower_bond:upper_bond] =  np.clip(self.p1[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p2[lower_bond:upper_bond] =  np.clip(self.p2[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p3[lower_bond:upper_bond] =  np.clip(self.p3[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p4[lower_bond:upper_bond] =  np.clip(self.p4[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p5[lower_bond:upper_bond] =  np.clip(self.p5[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)
        temp = np.random.random(size_sample)
        temp = temp<rate
        self.p6[lower_bond:upper_bond] =  np.clip(self.p6[lower_bond:upper_bond] + (temp * np.random.normal(0,par,size=size_sample)),-delta,delta)




        
         

    def Iterate(self): #Methods that creates new individuals
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



        
        
        
    

    def Generation(self): #Main method
        
        try : 
            counter = 0
            while self.fitness[0]> 4.1: #Stops when the better indivual's fitness falls below 4.1
                start = time.time() #Calculating iteration's time
                
                self.Mutations() #Applying methods
                self.Cross()
                self.Iterate()
                self.Sort()
                stop = time.time()
                
                if counter%100==0: #Print each 100 iterations
                    print("Best fitness :",self.fitness[0])
                    print("Avg fitness :",self.Avg_Fitness())
                    print("Time :",stop-start)
                counter += 1
            print("counter",counter) #Display iteration counter
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0] #returning result
        except KeyboardInterrupt:
            return self.p1[0],self.p2[0],self.p3[0],self.p4[0],self.p5[0],self.p6[0],self.fitness[0]
        
        



if __name__ == "__main__":

    path = "position_sample.csv"
    extract = ExtractFile(path) #Extracting file
    IA = Unit(extract,10000) #Genrating an object of 10000 indivuals
    result = IA.Generation() #Lauching the IA
    print("result :",result) #Display results
    for i in range(len(extract)): #Display the graph
        plt.scatter(extract[i][1],extract[i][2],color ='red')
        plt.scatter(result[0]* np.sin(result[1]*extract[i][0] + result[2]),result[3]* np.sin(result[4]*extract[i][0] + result[5]),color='blue' )
    plt.show()

    

    ax = plt.axes(projection='3d')

    # Data for a three-dimensional line
    zline = [i[0] for i in extract]
    xline = [i[1] for i in extract]
    yline = [i[2] for i in extract]
    ax.plot3D(xline, yline, zline, 'red',linestyle='',marker='x')

    zline = np.linspace(0,7,10000)
    xline = result[0]* np.sin(result[1]*zline + result[2])
    yline = result[3]* np.sin(result[4]*zline + result[5])
    ax.plot3D(xline, yline, zline, 'gray')
    

    plt.show()

    pass
