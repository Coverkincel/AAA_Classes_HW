class CountVectorizer:
    """
    Векторизатор, который подсчитывает частоту слов в текстах.

    Методы
    ------
    fit_transform(corpus: List[str]) -> List[List[int]]:
        Преобразует корпус текстов в матрицу частот слов.

    get_feature_names() -> List[str]:
        Возвращает список уникальных слов.

    Примеры
    --------
    >>> corpus = [
    ... 'Crock Pot Pasta Never boil pasta again',
    ... 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ... ]
    >>> vectorizer = CountVectorizer()
    >>> count_matrix = vectorizer.fit_transform(corpus)
    >>> vectorizer.get_feature_names()
    ['again', 'boil', 'crock', 'fresh', 'ingredients', 'never', 'parmesan', 'pasta', 'pomodoro', 'pot', 'taste', 'to']
    >>> count_matrix
    [[1, 1, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1]]
    """

    def __init__(self):
        self.feature_names = []

    def fit_transform(self, corpus):
        word_count = {}
        for text in corpus:
            words = text.lower().split()
            for word in words:
                if word not in word_count:
                    word_count[word] = 0

        self.feature_names = sorted(word_count)

        matrix = []
        for text in corpus:
            words = text.lower().split()
            row = [words.count(word) for word in self.feature_names]
            matrix.append(row)

        return matrix

    def get_feature_names(self):
        return self.feature_names


# Для проведения тестов с помощью doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
