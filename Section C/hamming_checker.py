#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hamming_checker(h_bi):
	#Read Input Into Empty List
	h_b =[]
	for i in h_bi:
		h_b.append(i)		
	reg_1 = reg_2 = reg_3 = reg_4 = 0
	
	#Check Regions
	for elem in range(1,16,2):
		reg_1 += int(h_b[elem])    
	for elem in range(2,16,4):
		reg_2 += int(h_b[elem]) + int(h_b[elem+1])
	for elem_1, elem_2 in zip(range(4, 8), range(12, 16)):
		reg_3 += int(h_b[elem_1]) + int(h_b[elem_2])
	for elem in range(8,16):
		reg_4 += int(h_b[elem])
    
	#Store Binary Equivalent of Redundant Bit Location
	redundantPosition_bin = [reg_1%2, reg_2%2, reg_3%2, reg_4%2]
    
	#Convert from Binary to Decimal
	exp = 0
	pos = 0
	for p in redundantPosition_bin:
		pos += (2 ** exp)*p
		exp += 1
	print("Redundant bit position: ", pos)        

	#Flip the Redundant Bit
	result = ""
	if(pos > 0):
		if(h_b[pos] == '0'):
			h_b[pos] = '1'
		else:
			h_b[pos] = '0'
		for e in h_b:
			result += str(e)
		return result	
	else:
		for e in h_b:
			result += str(e)
		return result
	


# In[ ]:




