# Description

A rectangular cake of width W and length L gets split into N rectangular pieces each with width w_i and length l_i. 
w_i, l_i are given for each piece. The main width W is given. Task is to find L. 

The problem is that using conventional coding surpasses the time limit of 6 seconds. That is; using string to int conversion. 
The time complexity is O(N), where N is the length of the string. Since w_i, l_i ranges from integers in [1, 10000], 
each line of string has a maximum length of 11 (5 digits each number and 1 spacing inbetween). This means that 
the worst case is O(11*N) for the task. It simply takes "too long" time. 

To solve this we can instead use a dictionary to override the need for string to int conversion. We first create a
dictionary of length 10000, storing each integer as the value and the corresponding integer converted into string as the key. 
Due to the value range for w_i and l_i, creating the dictionary only takes O(10000 log(5)). We can then use the dictionary to 
access the key-value pairs. Since accessing elements in a dictionary is O(1) due to the nature of dictionaries (Hashtables). 
The time complexity is O(N) + O(10000 log(5)) << O(11 N) 
as N is large. 

The code solution allows it to complete under the 6 seconds mark. 
