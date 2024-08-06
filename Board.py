import random

#generates a nonogram board based on input size
class Board:

    def __init__(self, size):
        bigList=[[random.randint(0,1) for i in range(size)] for i in range(size)]
        self.pieces=bigList
        self.sl=size
    
    def get_side_values(self):
        row_values=[]
        column_values=[]

        #for rows
        for i in range(self.sl):
            currentValues=[]
            currentSum=0
            for j in range(self.sl):
                
                if self.pieces[i][j]==1:
                    currentSum+=1
                else:
                    if currentSum!=0:
                        currentValues.append(currentSum)
                    currentSum=0
                    
                if j==self.sl-1:
                    if currentSum!=0:
                        currentValues.append(currentSum) 
            row_values.append(currentValues)

        for i in range(self.sl):
            currentValues=[]
            currentSum=0
            for j in range(self.sl):
                if self.pieces[j][i]==1:
                    currentSum+=1
                else:
                    if currentSum!=0:
                        currentValues.append(currentSum)
                    currentSum=0
                    
                if j==self.sl-1:
                    if currentSum!=0:
                        currentValues.append(currentSum)
            column_values.append(currentValues)
            
        return row_values,column_values

    def __str__(self):
        finalOutput=""

        for i in range(self.sl):
            for j in range(self.sl):
                if self.pieces[i][j]==1:
                    finalOutput+=("\u25a0 ")
                else:
                    finalOutput+=("x ")
            finalOutput+="\n"

        return finalOutput

    def get_row_buffer(self):
        maxL=[]
        l=self.get_side_values()
        
        for i in range(self.sl):
            maxL.append(len(l[0][i]))
        return (max(maxL))*2

    def get_column_max_size(self):
        maxL=[]
        l=self.get_side_values()
        
        for i in range(self.sl):
            maxL.append(len(l[1][i]))
        return (max(maxL))
    
    def print_table(self):
        #need to make a sparate function for initial column #s

        finalOutput=""
        l=self.get_side_values()
        maxC=self.get_column_max_size()+1

        rowBuffer=self.get_row_buffer()+1
        
        for i in range(maxC):
            finalOutput+=((" ")*rowBuffer)
            for j in range(self.sl):
                if(len(l[1][j])<=i):
                    finalOutput+=("  ")
                else:
                    finalOutput+=(str(l[1][j][i])+" ")
                    
            finalOutput+="\n"
        
        

        for i in range(self.sl):
            tmpSTR=""
            for k in range(len(l[0][i])):
                tmpSTR+=(str(l[0][i][k])+(" "))
            finalOutput+=tmpSTR+(" ")*(rowBuffer-(len(tmpSTR)))
                              
            for j in range(self.sl):
                if self.pieces[i][j]==1:
                    finalOutput+=("\u25a0 ")
                else:
                    finalOutput+=("x ")
            finalOutput+="\n"
        
        print(finalOutput)

print("Hello this is a python program that generates a random nonogram board of side length n")

sideLength=int(input("Please enter a integer value for the side length (recommended 0-30)"))
b=Board(sideLength)
b.print_table()

