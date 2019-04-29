def distance(strand_a, strand_b):
    dna = zip(strand_a, strand_b)
    distance = abs(len(strand_a) - len(strand_b))
    if len(strand_a) != len(strand_b):
        raise ValueError("Wrong input!")
    else:
        for i, j in dna:
            if i !=j:
              distance += 1
        return distance
pass


#def distance(strand1, strand2):
   # return sum(i != j for i, j in zip(strand1, strand2))