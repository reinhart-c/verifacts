# Verifacts
Fake news detector


# Skills and Tools
|   |   |   |
|---|---|---|
| HTML | scikit-learn (sklearn) | Imbalanced-learn |
| CSS | Pandas | Seaborn |  |
| JavaScript | Numpy |  |
| Python | nltk |  |
| Django | fastText |  |
| Sastrawi | Matplotlib |  |


# Problem
In recent years, the pervasive spread of fake news has become a critical issue, affecting societies globally. Fake news, defined as false or misleading information presented as news, has the potential to influence public opinion, disrupt political processes, and create widespread misinformation on crucial issues such as health, environment, and security. The rise of social media and digital platforms has exacerbated this problem, enabling rapid and far-reaching dissemination of unverified and often sensational content.

The implications of unchecked fake news are profound. It can lead to the erosion of trust in legitimate news sources, polarize communities, and even incite violence. In democratic societies, the spread of fake news can undermine electoral integrity and democratic processes, while in public health, it can contribute to the spread of harmful misinformation, as seen during the COVID-19 pandemic. Given these significant impacts, developing effective methods for detecting and mitigating fake news is of paramount importance.


# Solution
We explore advanced machine learning techniques to address this challenge. Our focus is on two key algorithms: Support Vector Machine (SVM) and Random Forest, which are evaluated using two distinct text representation methods: Term Frequency-Inverse Document Frequency (TF-IDF) and FastText embeddings. By comparing the performance of SVM and Random Forest classifiers with TF-IDF and FastText embeddings, we aims to identify the most effective approach for fake news detection. Our research provides valuable insights into the strengths and limitations of these techniques, contributing to the broader effort of combating the spread of misinformation.


# Method
Our approach to fake news detection involves several key steps. First, we preprocess the textual data by removing stopwords, punctuation, and performing stemming. We then convert the cleaned text into numerical features using TF-IDF and FastText embeddings. These features serve as input to our machine learning models: SVM and Random Forest. SVM is known for its effectiveness in high-dimensional spaces, while Random Forest provides robust classification through an ensemble of decision trees. We train and evaluate these models using a labeled dataset, optimizing their hyperparameters to enhance performance.
