
def read_resource(filename):
    with open(filename, 'r') as f:
        list_of_sentences=f.readlines()
    return list_of_sentences
