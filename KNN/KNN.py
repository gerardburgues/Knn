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
     


    def _init_train(self,train_data):
        
        train_data = train_data.reshape(train_data.shape[0],train_data.shape[1]*train_data.shape[2])

        self.train_data = train_data.astype(float)
    

    def get_k_neighbours(self, test_data, k):

        test_data = test_data.reshape(test_data.shape[0], test_data.shape[1] * test_data.shape[2])
        Y = cdist( test_data,  self.train_data ,'euclidean')
        
        imprimir = np.argsort(Y)[:,:k]
        
        imprimir = imprimir.flatten()

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

        i = 0
     
        if array.shape[1]>=2:
            
            while i < array.shape[0]:
                tots=0
                c, b = np.unique(array[i], return_counts=True)
                count_sort = np.argsort(-b)
                c = c[count_sort]
                  
                b[::-1].sort()
                maxim  =  np.max(b)
                

                
                
                if maxim in b[1:]:
                    rec=0
                    
                 
                    suma_total = np.sum(b == maxim)
                   
                    while  array[i][rec] != c[tots] and tots<suma_total:
                       
                        if array[i][rec] == c[tots]:
                           
                            a = np.append(a, array[i][rec])
                        
                        tots = tots +1
                        if tots == suma_total:
                            
                            rec= rec+1
                            tots=0
                  
                if np.all(maxim == b) :
                  
                    a = np.append(a, array[i][0])
                
                else:
                   
                   a = np.append(a, c[tots])
                i=i+1
   
            
        else:
            a = np.append(a, array)

        

        return a

    def predict(self, test_data, k):
      
        self.get_k_neighbours(test_data,k)
        result = self.get_class()
        return result
