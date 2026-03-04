from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd

class RecommenderSystem:
    def __init__(self, data_path="data/ethical_data.csv"):
        self.data_path = data_path
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.model = KMeans(n_clusters=3, random_state=42)
        try:
            self.df = pd.read_csv(self.data_path)
            self.fit()
        except FileNotFoundError:
            print("Data file not found. Initialize with synthetic data.")
            self.df = pd.DataFrame(columns=["dilemma", "recommendation"])

    def fit(self):
        if not self.df.empty:
            self.vectors = self.vectorizer.fit_transform(self.df['dilemma'])
            self.model.fit(self.vectors)

    def recommend(self, text):
        if self.df.empty:
            return ["No past data available."]
        
        vec = self.vectorizer.transform([text])
        cluster = self.model.predict(vec)[0]
        
        # Get simplified recommendation from the cluster
        similar_indices = [i for i, c in enumerate(self.model.labels_) if c == cluster]
        
        recs = self.df.iloc[similar_indices]['recommendation'].value_counts().head(3).index.tolist()
        return recs
