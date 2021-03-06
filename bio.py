from collections import Counter


def base_count_dna(dna):
    '''Returns the count of each base appearing in the given DNA sequence.'''
    base_count = Counter(dna)
    return [base_count[base] for base in 'ACGT']


def main():
    '''Main call. Parses, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_dna.txt') as input_data:
        dna = input_data.read().strip()

    # Get the count of each base appearing in the DNA sequence.
    base_count = map(str, base_count_dna(dna))

    # Print and save the answer.
    #print (' '.join(base_count))
    with open('001_DNA.txt', 'w') as output_data:
        output_data.write(' '.join(base_count))

if __name__ == '__main__':
    main()