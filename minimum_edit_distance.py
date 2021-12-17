import numpy as np

def min_ed_dis(source, target):
    source = '#' + source
    target = '#' + target

    target = [k for k in target]
    source = [k for k in source]
    sol = np.zeros((len(source), len(target)))

    # first row and column
    sol[0] = [j for j in range(len(target))]
    sol[:,0] = [j for j in range(len(source))]

    # Add anchor value
    if target[1] != source[1]:
        sol[1,1] = 2

    # Fill in the rest of the numpy array
    for c in range(1,len(target)):
        # Through every row
        for r in range(1, len(source)):
            # Not same letter
            if target[c] != source[r]:
                sol[r,c] = min(sol[r-1,c], sol[r,c-1]) + 1
            
            # Same letter
            else:
                sol[r,c] = sol[r-1, c-1]
    
    
    array_length = len(sol)
    last_element = int(sol[array_length - 1][-1])

    return last_element

def readFile(fileName):
    fileObj = open(fileName, "r") #opens the file in read mode
    words = fileObj.read().splitlines() #puts the file into an array
    fileObj.close()
    return words

def create_multiple_dictionaries():
    with open ('word_dictionary.txt','r') as reader:
        for row in reader:
            row = row.replace('\n', '')
            if len(row) > 4:
                with open ('word_dictionary_'+ str(len(row)) +'.txt', 'a') as writer:
                    writer.write(row + '\n')

def main():

    # create_multiple_dictionaries()

    spell_check_result = ''
    final_output = ''
    source = 'piana'
    edit_distance = {}
    
    source_tokenizer = source.split(' ')

    for source_word in source_tokenizer:
        # print (source_word)
        if len(source_word) > 4:
            words = readFile('word_dictionary_'+ str(len(source_word)) +'.txt')
            print ('READING word_dictionary_'+ str(len(source_word)) +'.txt')
            for word in words:
                edit_distance[word] = min_ed_dis(source, word)
    
                # print (edit_distance)

                temp = min(edit_distance.values())
                result = [key for key in edit_distance if edit_distance[key] == temp]
                spell_check_result = source.replace(source, result[-1]) + ' '
        else:
            spell_check_result = source_word + ' '

        final_output += spell_check_result

    # print (result[0])
    print (edit_distance)
    print ('Original Text: {}'.format(source))
    print ('After spell check: {}'.format(final_output))

if __name__ == '__main__':
    main()
