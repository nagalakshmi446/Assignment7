#!/usr/bin/env python
# coding: utf-8

# In[6]:


ls = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
window_size = 3
i = 0
moving_avg = []
while i <len(ls) - window_size+1:
    block = ls[i:i+window_size]
    window_average = sum(block)/window_size
    moving_avg.append(window_average)
    i = i+1
print(moving_avg)
    


# In[ ]:




