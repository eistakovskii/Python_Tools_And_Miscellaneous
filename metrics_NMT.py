def jaccard_similarity(candidate, reference):
    """Returns the Jaccard similarity between two token lists

    Args:
        candidate (list of int): tokenized version of the candidate translation
        reference (list of int): tokenized version of the reference translation

    Returns:
        float: overlap between the two token lists
    """
    
    # convert the lists to a set to get the unique tokens
    can_unigram_set, ref_unigram_set = set(candidate), set(reference)  
    
    # get the set of tokens common to both candidate and reference
    joint_elems = can_unigram_set.intersection(ref_unigram_set)
    
    # get the set of all tokens found in either candidate or reference
    all_elems = can_unigram_set.union(ref_unigram_set)
    
    # divide the number of joint elements by the number of all elements
    overlap = len(joint_elems) / len(all_elems)
    
    return overlap

# for making a frequency table easily
from collections import Counter

def similarouge1rity(system, reference):
    """Returns the ROUGE-1 score between two token lists

    Args:
        system (list of int): tokenized version of the system translation
        reference (list of int): tokenized version of the reference translation

    Returns:
        float: overlap between the two token lists
    """    
    
    ### START CODE HERE (REPLACE INSTANCES OF `None` WITH YOUR CODE) ###
    
    # make a frequency table of the system tokens (hint: use the Counter class)
    sys_counter = None
    
    # make a frequency table of the reference tokens (hint: use the Counter class)
    ref_counter = None
    
    # initialize overlap to 0
    overlap = None
    
    # run a for loop over the sys_counter object (can be treated as a dictionary)
    for token in sys_counter:
        
        # lookup the value of the token in the sys_counter dictionary (hint: use the get() method)
        token_count_sys = None
        
        # lookup the value of the token in the ref_counter dictionary (hint: use the get() method)
        token_count_ref = None
        
        # update the overlap by getting the smaller number between the two token counts above
        overlap += None
    
    # get the precision (i.e. number of overlapping tokens / number of system tokens)
    precision = None
    
    # get the recall (i.e. number of overlapping tokens / number of reference tokens)
    recall = None
    
    if precision + recall != 0:
        # compute the f1-score
        rouge1_score = None
    else:
        rouge1_score = 0 
    ### END CODE HERE ###
    
    return rouge1_score
