# Name: Shweta Vilas Shete ,      Red id: 825897742

# The Program below is the implementation of Trie Datastructure 

# Class TrieNode defines the structure of node for trie

class TrieNode:
    # constructor for trie node
    def __init__(self, trie_character):
        self.data = trie_character
        self.isEndOfTrie = False
        self.children = {}  # dictionary for trie nodes


# Class Trie implements the trie structure

class Trie:
    # Initialized a root node for trie
    def __init__(self):
        self.root = TrieNode('')

    # Method to insert nodes in trie

    # checks if word is present in trie, if not inserts it into the trie and 
    # marks the end of word for trie as true

    def insert(self, word):
        if self.search(word):
            print(word + " is already in trie.")
            return
        node = self.root
        # Checks if the word is present in child node of trie or else creates
        #  a trie node for that word.

        for character in word:
            if character not in node.children:
                node.children[character] = TrieNode(character)
            node = node.children[character]
        node.isEndOfTrie = True

    # Search a word in trie

    # method searches for search_word in the trie and gives the words which
    # matched the search_word

    def search(self, search_word):
        node = self.root
        trie_word_list = []
        trie_words = self.print_helper(node, trie_word_list, "")
        for word in trie_words:
            if search_word in word:
                print(search_word + " present in words \n" + word)
            else:
                print("word not present in trie")
        return

    # Function to Print all words in  trie

    def print_all_trie_words(self):
        trie_word_list = []
        self.print_helper(self.root, trie_word_list,'')
        print(trie_word_list)

    # Recursive function to help print_all_trie_words, 
    # which traverses the trie and creates a list of nodes.

    def print_helper(self, node, trie_word_list, prefix):
        if node.isEndOfTrie:
            trie_word_list.append(prefix + node.data)
        for child in node.children.values():
            self.print_helper(child, trie_word_list, prefix + node.data)
        return trie_word_list

    # Trie object creating and calling the insert, 
    # search and print_all_words functions.


trie = Trie()
insert_words = input("Enter words to be inserted in trie\n")
trie.insert(insert_words)
trie.print_all_trie_words()
search_word = input("Enter the word to be searched \n")
trie.search(search_word)
