#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math


# In[2]:


def rice_encoder(S, M):
    # If sample value is negative, consider it positive
    # and store signs separately
    sign = "-" if S < 0 else "+"
    S = abs(S)
    
    # Compute K using equation, M = 2^K
    K = int(math.ceil(math.log(M, 2)))

    # For S, the number to be encoded, find q and r
    quotient = S // M
    remainder = S % M

    # Generate codeword for q
    q_code_str = "1" * quotient

    # Write out r in binary
    diff = 2 ** K - M
    r = remainder + diff if remainder >= diff else remainder
    
    # Convert r to binary using fixed length K
    r_code_str = format(r, 'b').zfill(K)

    # Encoded string
    code_word = f"{sign}{q_code_str}0{r_code_str}"
    
    return code_word


# In[3]:


def rice_decoder(S, M):
    # Separate the sign and K-bits binary
    sign = S[0]
    S = S[1:]

    # Compute K using equation, M = 2^K
    K = int(math.ceil(math.log(M, 2)))

    # Separate q and r by spliting at the first 0
    q_code_str, r_code_str = S.split('0', 1)

    # Get quotient, q, by counting number of 1s before the first 0
    q = len(q_code_str)

    # Get remainder, r, by converting the next K-bits binary to decimal
    r = int(r_code_str, 2)
    
    # Compute decoded number using q * M + r
    S_decoded = q * M + r

    # Change sign of the decoded bit
    if sign == '-':
        S_decoded = -S_decoded

    return S_decoded


# In[ ]:




