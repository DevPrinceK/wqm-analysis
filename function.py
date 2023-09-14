import pandas as pd
import numpy as np
import io


def clean_data(file: str, min_value: int, max_value: int):
    '''
    file: data/filename.xlsx, filename.xlsx, etc
    min_value: 0, 1, etc
    max_value: 50, 100, 150
    '''
    # read file
    df =  pd.read_excel(file)
    print(f"Data read - {file}")
    
    # seed value
    # np.random.seed(0)
    
    # get records with updated values
    good_records = df[(df['Value'] >= min_value) & (df['Value'] <= max_value)]
    bad_records = df[(df['Value'] < min_value) | (df['Value'] > max_value)]
    print("Good and bad records extracted")
    
    # get mean and mode values from good records
    mean_of_good = int(good_records['Value'].mean())
    mode_of_good = int(good_records['Value'].mode())
    print("Mean and mode extracted")
    
    # check for which is greater
    first = mean_of_good if mean_of_good <= mode_of_good else mode_of_good
    second = mode_of_good if mode_of_good >= mean_of_good else mean_of_good
    print("First and seconds values obtained")
    
    # fill missing/outliers with values between mean and mode
    bad_records['Value'] = np.random.uniform(first, second, size=len(bad_records))
    print("Bad values replaced")
    
    # update and sort the data
    updated_df = pd.concat([good_records, bad_records]).sort_values(by=['Reading Date', 'Reading Time'])
    print("Data merged and sorted")
    
    # save file
    updated_name = f'cleaned_{file.split("/")[1].split(".")[0]}.csv'
    updated_df.to_csv(updated_name, index=False)
    print("Data saved as csv")
    
    print(f"Data Cleaned and Saved At: {updated_name}")
    return


files = [
    {
        "file": 'data/calcium.xlsx',
        "min": 0,
        "max": 100
    }, 
    {
        "file": 'data/fluoride.xlsx',
        "min": 1,
        "max": 25
    }, 
    {
        "file": 'data/oxidation.xlsx',
        "min": -1999,
        "max": 1999
    }, 
    {
        "file": 'data/oxygen.xlsx',
        "min": 4,
        "max": 13
    }, 
    {
        "file": 'data/ph.xlsx',
        "min": 0,
        "max": 14
    }, 
   ]

for file in files:
    try:
        clean_data(file['file'], file['min'], file['max'])
    except Exception as er:
        print(f'An Error Occured: {er}')
    finally:
        print("---------------------------------------------------")
        print("---------------------------------------------------")
    
    