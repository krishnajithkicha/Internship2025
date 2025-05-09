#This program is to analysis data,plot data 
import pandas as pd
import matplotlib.pyplot as plt
class DataAnalysis:
    def __init__(self,file):
        self.file=file
        self.data=None

    def loadCSV(self):
        self.data=pd.read_csv(self.file)
        print("The file is loaded successfully")
        print(self.data)

    
    def processCSV(self):
        print("The contents in ",self.file ,"are:")
        print(self.data)
        
        print("Displaying the first 5 rows:\n",self.data.head())
        print("Displaying the last 5 rows: \n",self.data.tail())
        print("Displays the number of rows and columns in data:\n",self.data.shape)
        print("Displays whether any column in null or not:\n",self.data.info())
        print("Displays the details about the columns in the file:\n",self.data.columns)
        print("Displays the summary statistics of the csv file:\n",self.data.describe())
    
    def plotCSV(self,x,y):
        plt.bar(self.data[x],self.data[y],color="blue")
        plt.title("BarChart of: "+x+ " vs "+y)
        plt.xlabel(x)
        plt.ylabel(y)
        plt.savefig("sales.png")
        plt.show()
def main():
    file="Sales.csv"
    da=DataAnalysis(file)
    da.loadCSV()
    da.processCSV()
    da.plotCSV("Product","TotalPrice")
if __name__=="__main__":
    main()
