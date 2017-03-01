VALUE_KEY = "*VALUE*"

class Trie:
    """A Trie - Prefix tree"""

    def __init__(self):
        self.root = {}

    def insert(self, item, value=True):
        """Insert an item into the Trie, or raise KeyError if there is already an item"""
        characters = list(item)
        current = self.root

        # Traverse through the trie
        for character in characters:
            if character not in current:
                current[character] = {}
            current = current[character]

        # # Already a value there
        # if current.get("*VALUE*", None):
        #     raise KeyError("Cannot add duplicate items to the Trie")

        # Add the value
        current["*VALUE*"] = value

    def modify(self, item, value):
        """Modify an item's value in the Trie if present, or raise KeyError"""
        characters = list(item)
        current = self.root

        # Traverse through the trie
        for character in characters:
            if character not in current:
                raise KeyError("The item is not in the Trie")
            current = current[character]

        # Modify the value
        current["*VALUE*"] = value

    def retrieve(self, item):
        """Return the value for the given item if present, else return None"""
        characters = list(item)
        current = self.root

        # Traverse through the trie
        for character in characters:
            if character not in current:
                return None
            current = current[character]

        # Get value
        return current.get("*VALUE*", None)

    def retrieve_closest(self, item):
        """Return the value from the given item if closest"""
        characters = list(item)
        current = self.root
        matching_value = None

        # Traverse through the trie
        for character in characters:
            # max_value = current.get("*VALUE*", None) if current.get("*VALUE*", None) > max_value else max_value
            # max_value = max(current.get("*VALUE*", None), max_value)

            # if current.get("*VALUE*", None) is not None:
            #     matching_value = current["*VALUE*"]
            if VALUE_KEY in current:
                matching_value = current[VALUE_KEY]

            current = current[character]


def scenario1(entries, phone_number):

    entries = {"123": 1}
    phone_number = "123456"

    while phone_number:
        if phone_number in entries:
            return entries[phone_number]
        phone_number = phone_number[:-1]

def scenario2():
    entries = {}
    phone_numbers = ["123456", "1234566"]
    costs = []

    for phone_number in phone_numbers:
        while phone_number:
            if phone_number in entries:
                costs.append(entries[phone_number])
            phone_number = phone_number[:-1]

    return costs

def scenario3(entries, phone_numbers):

    # Create Trie of entries
    trie = Trie()
    for key, value in entries:
        print(key)
        print(value)
        print('\n')
        trie.insert(key, value)

    costs = []
    for phone_number in phone_numbers:
        costs.append(trie.retrieve_closest(phone_number))

    return costs

def scenario4():

    # Just run scenario 3
    return None

def scenario5():
    
    # Just run scenario 3. Allow carriers to modify through trie.modify(item, new_value)
    return None


# File Helpers
def get_list_from_file(filename):
    """Return a list from the newlines on the file"""

    # Open file and read lines
    file = open(filename)
    return_list = file.readlines()

    # Strip whitespace
    return_list = [i.strip() for i in return_list]

    return return_list

def main():

    # Get phone numbers
    phone_numbers = get_list_from_file("phone-numbers-10000.txt")

    # Get entries
    entries = get_list_from_file("route-costs-10000000.txt")
    for index, entry in enumerate(entries):
        new_entry = tuple(entry.split(','))
        print(new_entry)
        entries[index] = new_entry

    print(scenario3(entries, phone_numbers))


if __name__ == '__main__':
    main()
