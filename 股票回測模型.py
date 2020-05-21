#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 22:41:40 2019

@author: oscar
"""

import pandas as pd

data = pd.read_csv('92db.csv')
name = input('Enter Your Name: ')
fund = float(input('Enter Your Fund: '))
fund1 = fund
ticker = input('Enter the Stock Name: (aapl, amd, amzn, or ebay) ')

ticker_list = data[ticker].tolist()
print(data)

# K, D initializer
K = 50
D = 50
k_value = []
d_value = []
count = 0


# Classify the data which we will use to calculate and analyze
for i in range(0, len(ticker_list)):
    if len(ticker_list[i:i+5]) >= 5:
        # print(ticker_list[i:i+5])
        last = float(ticker_list[i+4:i+5][0])
        fraction = last - min(ticker_list[i:i+5])
        denominator = max(ticker_list[i:i+5])-min(ticker_list[i:i+5])
        rsv = fraction / denominator * 100
        # print("RSV: ",rsv)
        K = 2/3 * K + 1/3 * rsv
        D = 2/3 * D + 1/3 * K
        k_value.append(K)
        d_value.append(D)

        # print('D Value: ',D)
        # print('K Value: ',K)
        if K < 20 or D < 20:
            if fund > last:
                count += 1
                fund -= last
                print('Buy in Price:', last)
                print('Avaiable Fund:', fund)
        elif K > 80 or D > 80:
            if count >= 1:
                fund += last
                count -= 1
                print('Sold out Price:',last)
                print('Avaiable Fund:', fund)


shareholding = count*ticker_list[-1]
profit = shareholding + fund - fund1 
perccentage = (profit / fund1) * 100
shareholding = int(count*ticker_list[-1])
shareholding = str(shareholding)

if count >= 1:
    position = ticker +' '+shareholding
else:
    position = "You do not have any positions!!"




# Final Recipt
print('')
print('RECEIPT') 
print('Investor:',name)
print('Initial Fund:', fund1)
print('Ticker:',ticker)
print('Positions:',position)
print('Total Gain/Loss: %.2f' %profit)
print('Total Gain/Loss Ratio: %.2f' %perccentage,'%')
print('Total Account Value: %.2f' %fund)
