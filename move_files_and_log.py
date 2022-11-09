from pathlib import Path

from os import listdir
from os.path import isfile, join
from os import remove

import time

import logging
import datetime

import argparse

def move_files_every_x_sec(from_dir: str, to_dir: str, every_x = 10, verbose = False, log_every_x = 60):
    '''
    The function checks for files and moves all files if any found from the specified origin folder
    to a target folder.
    
    The function runs indefinitely unless stopped via KeyboardInterrupt
    
    Input:
        from_dir: path to the origin folder
        to_dir: path to the target folder, i.e. where you want to move files
        every_x: how to often to check for new files in the origin folder; default = every 10 secs
        verbose: accompany with comments - Yes/No
        log_every_x: log the number of files in the target directory every x seconds 
    Output:
        No output
    
    '''
    when_log_counter = 0

    ct = datetime.datetime.now()
    ct = str(ct)[:16].replace(' ','_').replace('-', '_').replace(':','_')
    
    logging.basicConfig(filename='{}.log'.format(ct), filemode='w', 
                        format='%(asctime)s - %(levelname)s - %(message)s', 
                        datefmt='%H:%M:%S', 
                        level=logging.DEBUG, encoding='utf-8')
    
    starttime = time.time()

    
    if verbose:
        print('\nRUNNING')
        print(f'The folder being checked every {every_x} secs\n')

    logging.debug(f'Started running... FROM: {from_dir} TO: {to_dir} TIMING: {every_x} LOG_EVERY: {log_every_x}')
    
    while True:
        if verbose:print('CHECKING FOR FILES...', end = ' ')

        onlyfiles = [f for f in listdir(from_dir) if isfile(join(from_dir, f))]
        
        if len(onlyfiles) != 0:
            for i in onlyfiles:
                try:
                    Path(str(from_dir+'\\'+i)).rename(to_dir+'\\'+i)
                except:
                    if verbose:
                        print(f'File {i} already exists')
                        print(f'Deleting file {i}...')
                    logging.warning(f'File {i} already exists in {to_dir} -> Deleting it from {from_dir}...')
                    remove(Path(str(from_dir+'\\'+i)))
                    
            if verbose:print('=> ALL FILES TRANSFERRED!')
        else:
            if verbose:print('=> NO NEW FILES FOUND!')
        
        onlyfiles2 = [f for f in listdir(to_dir) if isfile(join(to_dir, f))]
        
        if verbose:print(f'Current number of files in the target folder: {len(onlyfiles2)} \n')
        
        when_log_counter += every_x

        if when_log_counter % log_every_x == 0:
            logging.info(f'Number of files in the target folder: {len(onlyfiles2)}')

        time.sleep(float(every_x) - ((time.time() - starttime) % float(every_x)))
    pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--from_dir", type=str, help="your origin folder", required=True
    )
    parser.add_argument(
        "--to_dir", type=str, help="your target folder", required=True
    )
    parser.add_argument(
        "--every_x", type=int, default=10, help="how often to check the folder for new files"
    )
    
    parser.add_argument(
        "--verbose", type=bool, default=True, help="give comments"
    )
    
    args = parser.parse_args()

    move_files_every_x_sec(args.from_dir, args.to_dir, args.every_x, args.verbose)
