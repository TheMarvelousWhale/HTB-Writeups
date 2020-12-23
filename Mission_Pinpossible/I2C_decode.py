# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 08:44:52 2020

@author: hoang
"""

import pandas as pd

df = pd.read_csv("./I2C_report.csv")
df['hex_data'] = df['Data'].map(lambda x: x[2:])  #Remove the 0x in data field
#print(df.head(100))
#df['RW_bit']=df['Address'].map(lambda x: hex(int(x,16) & 1))   # last bit of lambda
#df['Actual_add'] = df['Address'].map(lambda x: hex((int(x,16)>>1)))
#Print(df.iloc[100:200])
#Splitting the data into its 4bits
df['high_nibble'] = df['hex_data'].map(lambda x: x[0])
df['low_nibble'] = df['hex_data'].map(lambda x: x[1])
print(df['high_nibble'].value_counts())
print(df['low_nibble'].value_counts())
#We notice that the first 4bit is repeating 3 or 2 times while the last 4 bit is in a recurring pattern of 8 C D 9
#Let's extract the corresponding high nibble when low_nibble's in a pattern of 8C8 and D9 
#msg_hex = "".join([df['high_nibble'].iloc[i] for i in range(len(df)-1) if df['low_nibble'].iloc[i] is in ['C','D']])
#We notice that '8C8' bit pattern is just junk -> discard

#Reextract
msg_hex = "".join([df['high_nibble'].iloc[i] for i in range(len(df)-1) if df['low_nibble'].iloc[i]=='D'])
msg_bytes = bytes.fromhex(msg_hex)
print(msg_bytes)

#Reconstruction of messages
msg_parts = [i for i in msg_bytes.decode('utf8').split(" ") if len(i)]
msg_parts = [msg_parts[i]+' '+msg_parts[i+1] for i in range(len(msg_parts)) if i < len(msg_parts)-2 and i%2 == 0]
print(list(enumerate(msg_parts)))

print('Flag is: ',end='')
for i,msg in enumerate(msg_parts):
    print(msg[int(i+14)],end='')
    if msg[int(i+14)] == '}':
           break