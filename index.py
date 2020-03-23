from document import *


class Index:
    """An inverted index."""

    def __init__(self):
        """Creates the index.

        Args:
        - self: this index, the one to create. mandatory object reference.

        Returns:
        None.
        """
        pass

    def add_doc(self, doc: Document) -> None:
        """Adds doc to the index.

        Args:
        - self: this index, the one to add to. mandatory object reference.
        - doc: the document to add.

        Returns:
        None.
        """
        pass

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
        pass

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
    return query_string.split()
