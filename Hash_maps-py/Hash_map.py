class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        # Arrange an empty array
        self.array = [None for item in range(array_size)]

    # Hash function (chaning key to easier format(byte))
    def hash(self, key, count_collisions=0):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    # Get index value from hash code
    def compressor(self, hash_code):
        return hash_code % self.array_size

    # Assignment function (pushing key attached value into an array using index value)
    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

    # Collision resolution
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # Collision
        number_collisions = 1

        # Iterate until it finds empty index
        while(current_array_value[0] != key):
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            # if given index's key is different (the index is already stored by other key-value hash map)    
            number_collisions += 1

            return

    # Retriving value by inserting key 
    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        if possible_return_value is None:
            return None

        if possible_return_value[0] == key:
            return possible_return_value[1]

        retrieval_collisions = 1

        while (possible_return_value != key):
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

            return

hash_map = HashMap(15)
hash_map.assign('gabbro', 'igneous')
hash_map.assign('sandstone', 'sedimentary')
hash_map.assign('gneiss', 'metamorphic')

a = hash_map.retrieve('gabbro')
b = hash_map.retrieve('sandstone')
c = hash_map.retrieve('gneiss')

print(a)
print(b)
print(c)
