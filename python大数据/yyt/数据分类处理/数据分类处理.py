import jieba
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier

# Step 1: 数据读取
print("正在读取数据...")
data_file = "toutiao_cat_data.txt"
columns = ["news_id", "category_code", "category_name", "news_title", "keywords"]
data = pd.read_csv(data_file, sep="_!_", names=columns, encoding="utf-8")
print("数据读取完成！")

# Step 2: 数据过滤 - 选择五个类别
print("正在过滤数据...")
selected_categories = [102, 103, 104, 109, 116]  # 娱乐、体育、财经、科技、游戏
filtered_data = data[data["category_code"].isin(selected_categories)]
print(f"数据过滤完成！选择了 {len(filtered_data)} 条数据。")

# Step 3: 文本预处理
print("正在进行文本预处理...")
stopwords = {"的", "是", "了", "我", "有", "在", "和", "也", "不", "就", "人", "都", "到", "一个", "说", "而", "很",
             "对", "要", "为", "上", "与", "这", "好"}  # 常见停用词


def preprocess_text(text):
    words = jieba.lcut(text)  # 分词
    return " ".join([word for word in words if word not in stopwords])


filtered_data["processed_title"] = filtered_data["news_title"].apply(preprocess_text)
print("文本预处理完成！")

# Step 4: 文本向量化 - 使用TF-IDF
print("正在进行文本向量化...")
# max_features为训练的数据量大小
vectorizer = TfidfVectorizer(max_features=3000)
X = vectorizer.fit_transform(filtered_data["processed_title"])
y = filtered_data["category_code"]
print("文本向量化完成！")

# Step 5: 数据集划分
print("正在划分训练集和测试集...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("数据集划分完成！")

# Step 6: 模型训练 - 使用朴素贝叶斯
print("正在训练朴素贝叶斯模型...")
nb_model = MultinomialNB()
nb_model.fit(X_train, y_train)
print("朴素贝叶斯模型训练完成！")

# Step 7: 模型训练 - 使用决策树
print("正在训练决策树模型...")
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)
print("决策树模型训练完成！")

# Step 8: 模型评估
print("正在评估模型...")
y_pred_nb = nb_model.predict(X_test)
y_pred_dt = dt_model.predict(X_test)


def evaluate_model(name, y_pred):
    print(f"模型: {name}")
    print("准确率:", accuracy_score(y_test, y_pred))
    print("分类报告:\n", classification_report(y_test, y_pred))
    print("混淆矩阵:\n", confusion_matrix(y_test, y_pred))
    print("=" * 50)


evaluate_model("朴素贝叶斯", y_pred_nb)
evaluate_model("决策树", y_pred_dt)
print("模型评估完成！")

# Step 9: 创新与可解释性
print("正在进行特征重要性分析（仅朴素贝叶斯模型）...")
feature_names = vectorizer.get_feature_names_out()
top_features = sorted(zip(nb_model.feature_log_prob_[0], feature_names), reverse=True)[:10]
for prob, word in top_features:
    print(f"词: {word}, 概率: {prob}")
print("特征重要性分析完成！")
