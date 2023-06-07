import pandas as pd
import matplotlib.pyplot as plt

import json


class Drawing_plots:
    def __init__(self):
        pass
    def draw_plots(self):
        json_string = open("plots.json", "r")
        df = pd.read_json(json_string)
        inp = int(input('choose 1-1347: '))-1
        df_by_row = df.iloc[inp]

        df_json = df_by_row.to_json()
        df_dict = json.loads(df_json)

        xAxis = []
        yAxis = []
        for i in df_dict:
            if i == 'name':
                xAxis.append(str(0))
                yAxis.append(str(0))
                continue
            xAxis.append(str(i))
            yAxis.append(str(df_dict[i]))

        fig = plt.figure(figsize=(15, 5))
        yAxis2 = [float(k) for k in yAxis]
        plt.bar(xAxis, yAxis2, width=0.3)
        plt.title(str(df_dict['name']))
        plt.savefig('plots/plot_{}.png'.format(df_dict['name']))
        plt.show()


if __name__ == '__main__':
    Plot_object = Drawing_plots()
    Plot_object.draw_plots()