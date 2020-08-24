__authors__ = ['1493112','1392437', '1420576']
__group__ = 'DL.15'

import numpy as np
import math
import operator
from scipy.spatial.distance import cdist

class KNN:
    def __init__(self, train_data, labels):

        self._init_train(train_data)
        self.labels = np.array(labels)
        #############################################################
        ##  THIS FUNCTION CAN BE MODIFIED FROM THIS POINT, if needed
        #############################################################


    def _init_train(self,train_data):
        """
        initializes the train data
        :param train_data: PxMxNx3 matrix corresponding to P color images
        :return: assigns the train set to the matrix self.train_data shaped as PxD (P points in a D dimensional space)
        """
        #######################################################
        ##  YOU MUST REMOVE THE REST OF THE CODE OF THIS FUNCTION
        ##  AND CHANGE FOR YOUR OWN CODE
        #######################################################
        
        train_data = train_data.reshape(train_data.shape[0],train_data.shape[1]*train_data.shape[2])

        self.train_data = train_data.astype(float)
        #self.train_data = np.random.randint(8,size=[10,14400])


    def get_k_neighbours(self, test_data, k):

        test_data = test_data.reshape(test_data.shape[0], test_data.shape[1] * test_data.shape[2])
        Y = cdist( test_data,  self.train_data ,'euclidean')
        
        imprimir = np.argsort(Y)[:,:k]
        
        imprimir = imprimir.flatten()
        #print(self.labels)
        #print(imprimir)

        b = list(imprimir)
        i = 0
        arg = b
        sn = np.array([])
        j = 0
        while j < len(self.labels):

            if i < len(arg) and arg[i] == j:
                sn = np.append(sn, self.labels[j])
                i = i + 1
                j = 0
            else:
                j = j + 1

        sn = sn.reshape(-1,k)
        self.neighbors =sn
        



    def get_class(self):
       
        a = np.array([])
 
        array = self.neighbors
        print(array)

        i = 0 # iterador per c
     
        if array.shape[1]>=2:
            
            while i < array.shape[0]:
                tots=0
                c, b = np.unique(array[i], return_counts=True)
                #print("esto es c", c)
                #print("esto es b", b)
                count_sort = np.argsort(-b)
                c = c[count_sort]
                  
                b[::-1].sort()
                #print("non", b)
                #print("esto es c sorted", c)
                maxim  =  np.max(b)
                
                #print("Aixo es index maxim", maxim)
                
                
                
                if maxim in b[1:]:
                    #print("estem aqui?")
                    rec=0
                    
                 
                    suma_total = np.sum(b == maxim)
                    #print(suma_total)
                    while  array[i][rec] != c[tots] and tots<suma_total:
                        #print(tots)
                        
                        if array[i][rec] == c[tots]:
                            #print("l'hem trobat")
                            a = np.append(a, array[i][rec])
                        
                        tots = tots +1
                        if tots == suma_total:
                            #print("tots == suma total")
                            rec= rec+1
                            tots=0
                    #print(c[tots])

                if np.all(maxim == b) :
                  
                    a = np.append(a, array[i][0])
                
                else:
                   
                   a = np.append(a, c[tots])
                i=i+1
   
            
        else:
            a = np.append(a, array)

        #print(a)

        return a

    def predict(self, test_data, k):
      
        self.get_k_neighbours(test_data,k)
        result = self.get_class()
        return result
