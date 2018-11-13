
def splitwindow(sequence, limit):
    split_seq = sequence.split()
    iterators = [iter(split_seq[index:]) for index in range(limit)]
    return zip(*iterators)
