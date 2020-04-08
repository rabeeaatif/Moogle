from document import *
from nltk import *
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import math

class Index:
    """An inverted index."""

    def __init__(self):
        """Creates the index.

        Args:
        - self: this index, the one to create. mandatory object reference.

        Returns:
        None.
        """
        self._dict = {}
        self._total_documents = 0

    def add_doc(self, doc: Document) -> None:
        """Adds doc to the index.

        Args:
        - self: this index, the one to add to. mandatory object reference.
        - doc: the document to add.

        Returns:
        None.
        """
        self._total_documents += 1
        # adding words to index
        for word, loc in doc.words():
            simplified_word = index_preprocess(word)
            if len(simplified_word) != 0:
                if simplified_word not in self._dict.keys():
                    self._dict[simplified_word] = [doc] # including the word along with doc_id term frequency
                else:
                    self._dict[simplified_word] = self._dict[simplified_word] + [doc]

    def query(self, query_string: str) -> [(str, float)]:
        """Returns a ranked list of document IDs from the index and their TF-IDF score
        for query_string. The ranking is from most similar (index 0) to least similar.

        Args:
        - self: this index, the one to search in. mandatory object reference.
        - query_string: contains space separated query words

        Returns:
        A list of pairs where each pair contains a document ID and the TF-IDF of
        the corresponding document with query_string. The list is sorted in
        order to decreasding similarity.
        """
        # function for sorting
        def doc_id_sort(tuples):
            return tuples[1]
        # adding documents which are relevant
        doc_lst = []
        final_lst = []
        query_lst = query_tokenize(query_string)
        for term in query_lst:
            if term in self._dict.keys():
                for doc in self._dict[term]:
                    if doc.doc_id in doc_lst:
                        doc_index = doc_lst.index(doc.doc_id)
                        final_lst[doc_index] = (final_lst[doc_index][0], (final_lst[doc_index][1] + ((len(doc._words[term]) / len(doc._words)) * math.log(self._total_documents / len(self._dict[term])))))
                    else:
                        doc_lst.append(doc.doc_id)
                        final_lst.append((doc.doc_id, ((len(doc._words[term]) / len(doc._words)) * math.log(self._total_documents / len(self._dict[term])))))
        final_lst.sort(key=doc_id_sort)
        return (final_lst)
 
# ------------------------- Helpers -------------------------


def index_preprocess(word: str) -> str:
    """Returns a processed version of word appropriate for adding to the index.

    Implement as you wish. The default returns word as is.
   
    Args:
    - word: the potential word to be processed for indexing.

    Returns:
    An appropriately processed version of word.
    """
    return word


def query_tokenize(query_string: str):
    """Returns a list of query words tokenized from query_string, appropriate
    for querying the index.

    Implement as you wish. The default splits query_string at whitespace.

    Args:
    - query_string: the string to tokenize.

    Returns:
    A list of query tokens appropriate for querying the index.
    """
    # using ntlk to tokenize and stem query words
    stop_words = set(stopwords.words('english'))
    # tokenization
    words = word_tokenize(query_string)
    words_lowered = [word_.lower() for word_ in words]
    # checking for stop and alpha numeric words
    words_tokenized = [word_ for word_ in words_lowered if not word_ in stop_words and word_.isalnum()]
    # stemming
    words_stemmed = [PorterStemmer().stem(word_) for word_ in words_tokenized]
    return words_stemmed
