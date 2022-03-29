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
    def __init__(self,extract: list):
        self.training_data = extract
    
    def Fitness(self, test_param : list):
        
        distance_moyenne = 0
        for i in self.training_data :
            t= i[0]
            x_test = test_param[0] * (math.sin(test_param[1] * t + test_param[2]))
            y_test = test_param[3] * (math.sin(test_param[4] * t + test_param[5]))
            distance_moyenne += math.sqrt((x_test-i[1])**2 + (y_test-i[2])**2)
            # distance_moyenne += (x_test-i[1])**2 + (y_test-i[2])**2
        # return float(distance_moyenne/len(self.training_data))
        return distance_moyenne

    def Cross(self,save_result : list) : 
        results = copy.deepcopy(save_result)
       
        

        for i in range(0,len(results)- len(results)%2,2):
            
            results[i][0],results[i+1][0] = results[i][0][:int(len(results[i][0])/2):] + results[i+1][0][int(len(results[i][0])/2)::],results[i+1][0][:int(len(results[i][0])/2):] + results[i][0][int(len(results[i][0])/2)::]
            results[i][1] = self.Fitness(results[i][0])
            results[i+1][1] = self.Fitness(results[i+1][0])

        results.sort(key=lambda x : x[1], reverse = False)

        return results

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

        for i in range(len(save_result)) :
            temp = int(random.randint(0,len(save_result[i][0])))
            for j in range(temp,int(random.randint(temp,len(save_result[i][0])))):
                results[i][0][j] =  random.uniform(-100,100) #Change values random.uniform(a,b) if you want a wider mutation
            results[i][1] = self.Fitness(results[i][0])
        results.sort(key=lambda x : x[1], reverse = False)

        return results

    def Compare(save_result : list, temp : list):

        result = copy.deepcopy(save_result)
        result.extend(x for x in temp if x not in result)
        # result = result + list(set(temp)-set(result))
        
        result.sort(key=lambda x : x[1], reverse = False)

        result = result[:len(save_result)]
        save_result.clear()
        save_result.extend(result)
                
                
        
        return result

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
            while save_result[0][1] > 1:

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
    print(';'.join(map(str,result[0])))
    with open("result.txt",'w') as f:
        temp = ';'.join(map(str,result[0]))
        temp += ' res = ' + str(result[1])
        f.write(temp)
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