import glob
import pandas as pd
import os
from sentence_transformers import SentenceTransformer, util


def create_embedding(food_carbon_df):
    


    # Load the sentence transformer model 
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

    # Compute embeddings for food categories
    embeddings = food_carbon_df['FOOD COMMODITY ITEM'].apply(lambda x: model.encode(x, convert_to_tensor=True,show_progress_bar = False)).to_numpy()

    return embeddings


