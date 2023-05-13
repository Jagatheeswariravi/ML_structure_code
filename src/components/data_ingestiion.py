import sys
import os
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split


train_data_path = os.path.join("artifact","train.csv")
test_data_path = os.path.join("artifact","test.csv")
raw_data_path  = os.path.join("artifact","raw_data.csv")


class DataIngestion:
    def __init__(self,train_data_path,test_data_path,raw_data_path):
        self.train_data_path = train_data_path
        self.test_data_path = test_data_path
        self.raw_data_path  = raw_data_path
        
    
    def intiate_data_ingestion(self):
        logging.info("Entered to the data collection class")


        
        try:
            df = pd.read_csv("C:\\Users\\jagar\\codestruc\\data\\StudentsPerformance.csv") 

            os.makedirs(os.path.dirname(self.train_data_path),exist_ok=True)

            df.to_csv(self.raw_data_path,index=False,header=True)

            logging.info("train_test is initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=102)

            train_set.to_csv(self.train_data_path,index=False,header=True)

            test_set.to_csv(self.test_data_path,index=False,header=True)

            logging.info("train_test split is finished")
        
            return (
            self.raw_data_path,
            self.train_data_path,
            self.test_data_path
        
        )



        except Exception as e:
            raise CustomException(e,sys)
        



if __name__ == "__main__":
    obj=DataIngestion()
    raw,train,test = obj.intiate_data_ingestion()

    






 