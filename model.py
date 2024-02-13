import pandas as pd
from sentence_transformers import CrossEncoder, SentenceTransformer

# Load pre-trained models
class Model:
    bi_encoder = SentenceTransformer('multi-qa-MiniLM-L6-cos-v1')
    cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
    # Load Fry's answers dataset
    df = pd.read_csv('data/fry.csv')
    df = df.loc[df['Character'] == 'Fry']
    questions = df['Line'].tolist()
    # Encode all answers
    question_embeddings = bi_encoder.encode(questions, convert_to_tensor=True)
