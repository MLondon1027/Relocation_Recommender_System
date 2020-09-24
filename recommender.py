
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def cosine_recommend_zip(zip_input=input("Enter your zip code: "), num=input("Optional: Enter number of recommendations: "), city=input("Optional: Enter city: "), state=input("Optional: Enter state: ")):
    final = pd.read_csv('data/final.csv')
    scaler = StandardScaler()
    scaled = scaler.fit_transform(final)
    scaled = pd.DataFrame(scaled, index=final.index, columns=final.columns)
    cosine_matrix = cosine_similarity(scaled, scaled)
    mapping = pd.Series(scaled.reset_index().index, index = scaled.index)
    zip_location = pd.read_csv('data/us-zip-code-latitude-and-longitude.csv', sep = ';')
    zip_index = int(mapping[zip_input])
    #get similarity values with other zip codes
    #similarity_score is the list of index and similarity matrix
    similarity_score = list(enumerate(cosine_matrix[zip_index]))
    #sort in descending order the similarity score of zip inputted with all the other zip codes
    similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
    # Get the scores of the 15 most similar zip codes. Ignore the first zip code.
    #return zip codes using the mapping series
    zip_indices = [i[0] for i in similarity_score]
    #similarity_score = similarity_score[1:num+1]
    best = []
    for i in zip_indices:
        best.append(int(final.reset_index().iloc[i][0]))
    df = pd.DataFrame(data = best, columns = ['Zip'])
    merged = pd.merge(df,zip_location,on='Zip',how='inner')
    merged = merged[['Zip', 'City', 'State']]
    if city==None:
        if state==None:
            print(merged[1:num+1])
        else:
            merged = merged[merged['State']==state]
            print(merged[0:num+1])
    else:
        if state==None:
            print('You must enter a state with a city.')
        else:
            merged = merged[merged['State']==state]
            merged = merged[merged['City']==city]
            print(merged[0:num+1])

if __name__ == "__main__":
    cosine_recommend_zip(zip_input=zip_input, num=num, city=city, state=state)