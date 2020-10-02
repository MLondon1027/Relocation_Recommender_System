
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def cosine_recommend_zip(zip_input, num, city, state):
    if len(num) == 0:
        num = '10'
    final = pd.read_csv('final_data.csv')
    final['index'] = final['index'].astype(str)
    for idx, i in enumerate(final['index']):
        if len(i) == 4:
            final.iloc[idx, 2] = '0' + i
    #final['index'] = final['index'].astype(int)
    final.drop('Unnamed: 0', axis=1, inplace=True)
    final.drop('level_0', axis=1, inplace=True)
    final.set_index('index', inplace=True)
    scaler = StandardScaler()
    scaled = scaler.fit_transform(final)
    scaled = pd.DataFrame(scaled, index=final.index, columns=final.columns)
    #print(scaled.head())
    cosine_matrix = cosine_similarity(scaled, scaled)
    mapping = pd.Series(scaled.reset_index().index, index = scaled.index)
    zip_location = pd.read_csv('us-zip-code-latitude-and-longitude.csv', sep = ';')
    zip_index = int(mapping[zip_input])
    #get similarity values with other zip codes
    #similarity_score is the list of index and similarity matrix
    similarity_score = list(enumerate(cosine_matrix[zip_index]))
    #sort in descending order the similarity score of zip inputted with all the other zip codes
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    # Get the scores of the n most similar zip codes. Ignore the first zip code, as it is itself.
    #return zip codes using the mapping series
    zip_indices = [i[0] for i in similarity_score]
    #similarity_score = similarity_score[1:num+1]
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
            merged = merged[merged['State']==state]
            merged = merged.reset_index(drop=True)
            recs = merged[0:int(num)+1]
            print(recs)
    else:
        if len(state) == 0:
            print('You must enter a state with a city.')
        else:
            merged = merged[merged['State']==state]
            merged = merged[merged['City']==city]
            merged = merged.reset_index(drop=True)
            recs = merged[0:int(num)+1]
            print(recs)
    return recs

if __name__ == "__main__":
    zip_input=input("Enter your zip code: ")
    num=input("Optional: Enter number of recommendations: ")
    city=input("Optional: Enter city: ")
    state=input("Optional: Enter state: ")
    cosine_recommend_zip(zip_input, num, city, state)