import pandas as pd
import json 
import numpy as np
import ast

class data_analysis:
    def __init__(self, df) -> None:
        self.df = df
        self.row_num = len(df)
        self.ndf = 0
        self.remove_str()
        print('init complete')

    def remove_str_per_row(self, data_per_row):
        frame_list = ast.literal_eval(data_per_row)
        frame_dic_list = []
        for index in range(len(frame_list)):
            frame_dic_list.append(json.loads(frame_list[index])) 
        return frame_dic_list

    def remove_str(self):
        ndf_ans_8_list = []
        for i in range(self.row_num):
            ndf_ans_8_list.append(self.remove_str_per_row(self.df.iloc[i,8]))
        return ndf_ans_8_list

if __name__ == '__main__':
    df = pd.read_excel('./data/data.xlsx')  
    data_entity = data_analysis(df)
    print(data_entity.df)
    print(data_entity.remove_str())
    print(len(data_entity.remove_str()))