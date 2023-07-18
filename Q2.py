"""
Q. Counting the frequencies in a list using dictionary in python
Input = [1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]
"""


def countFrequency(my_list):
    # creating an empty dictionary
    freq = {}
    for item in my_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    
    for key,value in freq.items():
        print("%d:%d" %(key,value))  
        
              
# Driver function
if __name__ == "__main__":
    my_list=[1,1,1,5,5,3,1,3,3,1,4,4,4,2,2,2,2]   
    countFrequency(my_list)         
    