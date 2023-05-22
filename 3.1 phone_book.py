class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(self.size)]
    
    
    def insert(self, key, value):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        found = False
        
        for data in bucket:
            if key == data[0]:
                found = True
                data[1] = value
        
        if not found:
            bucket.append([key, value])
    
    
    def find(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        
        for data in bucket:
            if key == data[0]:
                return data[1]
        
        return None
    
    
    def delete(self, key):
        hashed_key = hash(key) % self.size
        bucket = self.hash_table[hashed_key]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                return bucket.pop(i)


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


def read_queries():
    n = int(input())
    return [Query(input().split()) for _ in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    ht = HashTable(20000)
    for cur_query in queries:
        if cur_query.type == 'add':
            ht.insert(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            ht.delete(cur_query.number)
        else:
            response = ht.find(cur_query.number)
            if not response:
                response = 'not found'
            result.append(response)
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

