import random as R
import time as T

# CONFIGURATION
Sec = 5        # Seconds before change SteamGuard
L = 5          # Length SteamGuard

# Symbols of SG
S = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
     'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'O', 'P', 'A',
     'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
     'C', 'V', 'B', 'N', 'M']

def Gen(Length = 5):         # Main Function
     pwd = ''
     for i in range(Length):
          pwd = pwd + R.choice(S)
     return pwd

while True:              # Cycle of changes
     print(Gen(L))
     T.sleep(Sec)
     continue

#    NeWulla's SteamGuard
#    Created by NeWulla
#    (c) Copyright by NeWulla
#    02.03.2022