# train_model.py
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 模拟数据
texts = [
    "good",
    "great",
    "awesome",
    "excellent",
    "bad",
    "terrible",
    "awful",
    "horrible",
]
labels = [1, 1, 1, 1, 0, 0, 0, 0]  # 1=positive, 0=negative

# 训练 pipeline
pipe = Pipeline([("tfidf", TfidfVectorizer()), ("clf", LogisticRegression())])
pipe.fit(texts, labels)

# 保存模型
joblib.dump(pipe, "model.pkl")
print("✅ Model saved as model.pkl")
