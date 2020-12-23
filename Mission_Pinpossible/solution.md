# HTB Hardware: Mission Pinpossible

We are given with a logic data and a photo of what looks like a I2C backpack with LED. Hmmmmmm...

Use Salae 1.2.18 (Some CTF writeup advised this because during one of the CTF i used 2.x and the interface wasn't the same) to open the file. We can tell it's I2C. 
Use Salae logic analyzer and export the analyzer data (not decoded data or the original data) into csv.

At this point onwards it's just noticing pattern in the high nibble and lower nibble of the data portion in each packet 
We notice the lower nibble is a recurring 282 and D9 with repeating high nibble for each pattern, so we just gonna grab and extract the corresponding high nibble for these pattern

Decoding partially, we noticed that the 282 is just noise, but D9 contains ascii characters 

This led to extracting just the D9 portion and cleaning it up, and extracting the message out

the flag is : Flag is: HTB{84d_d3519n_c4n_134d_70_134k5!d@} 
