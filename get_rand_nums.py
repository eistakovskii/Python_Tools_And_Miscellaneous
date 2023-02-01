from random import randint

def get_n_randints(quant: int, t_list: list) -> list[int]:
    '''
    Use this function to generate N (quant) number of integers from the range of 0 to X (t_list - 1) numbers
    
    Input:
        quant: number of integers to generate
        t_list: list to define range of integers to draw from

    Output:
        _ : a list of with integers
    '''

    len_thr = len(t_list) - 1
    return [randint(0, len_thr) for _ in range(quant)]
