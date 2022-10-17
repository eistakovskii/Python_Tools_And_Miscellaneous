
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from tqdm import tqdm

def pull_from_reverso(path_driver, path_target_words, verbose=False):
    driver = webdriver.Chrome(executable_path=path_driver)

    with open(path_target_words, mode='r', encoding='utf-8') as f:
        target_words = f.readlines()
        target_words = [i.strip('\n') for i in target_words]

    if verbose: print('\n')

    to_save_text = list()
    broken = list()
    counter_1 = 0
    
    for i in tqdm(target_words):
        counter_1 += 1
        if verbose: print(f'\n\t TEXTS {counter_1}/{len(target_words)}\n')
        try:
            driver.get(f"https://context.reverso.net/translation/german-english/{i}")
            if verbose: print('\nTEXT START')
            for i in range(1, 11):
                out_t = driver.find_element(By.XPATH, 
                f'/html/body/div[3]/section[1]/div[2]/section[4]/div[{i}]/div[1]').text
                if len(out_t) <= 5 or out_t == None:
                    if verbose: print('NONE')
                    if verbose: print('\nTEXT END')
                else:
                    if verbose: print(out_t)
                    to_save_text.append(str(out_t))
                    if verbose: print(f'\n\tLEN of OUT TEXTS: {len(to_save_text)}\n')
                    if verbose: print('\nTEXT END')
                if verbose: print('\n')
        except:
            if verbose: print(str(out_t))
            broken.append(str(out_t))
            continue

    if verbose: print(f'BROKEN: {broken} LEN{len(broken)}')

    if verbose: print(f'READY: {len(to_save_text)}')

    with open('texts_zeros_de.txt', mode='w', encoding='utf-8') as f2:
        for i in to_save_text:
            f2.write(i+'\n')

    if verbose: print('\n')
    driver.close()
    pass

