from sentence_transformers import SentenceTransformer, util
import glob
import pandas as pd
import os
import sys
import numpy as np

def compute_similarity(input_text, food_carbon_df, embeddings_np):
    
    #Input text
    input_text = input_text['Food_Name'].iloc[0]
    
    # Load the sentence transformer model 
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')

    # Create embedding of the input text
    input_embedding = model.encode(input_text, convert_to_tensor=True,show_progress_bar = False)
    
    # Compute similarity scores of input with food categories
    similarity_scores = [float(util.cos_sim(input_embedding, x).numpy()[0]) for x in embeddings]
    food_carbon_df['Similarity'] = similarity_scores

    # Take the food category as the one with max similarity score
    max_idx = food_carbon_df['Similarity'].idxmax()
    food_category = food_carbon_df['FOOD COMMODITY ITEM'].iloc[max_idx]    
    
    
    return food_category
