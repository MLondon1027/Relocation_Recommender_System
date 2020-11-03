
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import sys
#from flask import Flask # Nov 3
#app = Flask (__name__) # Nov 3

#@app.route('/') # Nov 3
def cosine_recommend_zip(zip_input, num, city, state):
    if len(state) > 0:
        state = state.upper()
    if len(city) > 0:
        city = city.capitalize()
    if len(num) == 0:
        num = '10'
    final = pd.read_csv('final_data.csv')
    final['index'] = final['index'].astype(str)
    for idx, i in enumerate(final['index']):
        if len(i) == 4:
            final.iloc[idx, 2] = '0' + i
    final.drop('Unnamed: 0', axis=1, inplace=True)
    final.drop('level_0', axis=1, inplace=True)
    final.set_index('index', inplace=True)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(final)
    scaled = pd.DataFrame(scaled, index=final.index, columns=final.columns)
    cosine_matrix = cosine_similarity(scaled, scaled)
    mapping = pd.Series(scaled.reset_index().index, index = scaled.index)
    zip_location = pd.read_csv('us-zip-code-latitude-and-longitude.csv', sep = ';')
    try:
        zip_index = int(mapping[zip_input])
    except:
        print('Please enter a valid zip code.')
        sys.exit(1)
    #get similarity values with other zip codes
    #similarity_score is the list of index and similarity matrix
    similarity_score = list(enumerate(cosine_matrix[zip_index]))
    #sort in descending order the similarity score of zip inputted with all the other zip codes
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    # Get the scores of the n most similar zip codes. Ignore the first zip code, as it is itself.
    #return zip codes using the mapping series
    zip_indices = [i[0] for i in similarity_score]
    best = []
    for i in zip_indices:
        best.append(int(final.reset_index().iloc[i][0]))
    df = pd.DataFrame(data = best, columns = ['Zip'])
    merged = pd.merge(df,zip_location,on='Zip',how='inner')
    merged = merged[['Zip', 'City', 'State']]
    if len(city) == 0:
        if len(state) == 0:
            merged = merged.reset_index(drop=True)
            recs = merged[1:int(num)+1]
            print(recs)
        else:
            if len(merged['State'].where(merged['State'] == state)) > 0:
            #if state in merged['State']:
                merged = merged[merged['State']==state]
                merged = merged.reset_index(drop=True)
                recs = merged[1:int(num)+1]
                print(recs)
            else:
                print('Please enter a valid state abbreviation.')
                sys.exit(1)
    else:
        if len(state) == 0:
            print('You must enter a state with a city.')
        else:
            merged = merged[merged['State']==state]
            merged = merged[merged['City']==city]
            merged = merged.reset_index(drop=True)
            recs = merged[0:int(num)]
            if len(recs) != 0:
                print(recs)
            else:
                print('Please enter a valid city.')
                sys.exit(1)
    
    

if __name__ == "__main__":
    zip_input=input("Enter your zip code: ")
    num=input("Optional: Enter number of recommendations: ")
    city=input("Optional: Enter city: ")
    state=input("Optional: Enter state abbreviation: ")
    cosine_recommend_zip(zip_input, num, city, state)
    #app.run() # Nov 3