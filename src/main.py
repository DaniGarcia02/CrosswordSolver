import numpy as np
import time
from copy import deepcopy

from gap import Gap


def read_file(file_name):
    file = np.loadtxt(file_name, dtype='str', comments=None, delimiter='\t')
    return file        
             
# Returns an array of Gap with the gaps that finds on the rows of the board
def getGaps(board,  ident):
    gaps = []
    gap = ''
    position = []
    
    # Searching for gaps in rows
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == '0':
                gap = gap + '0'
                position.append([i, j])               
            else:
                if gap != '' and gap != '0':
                    gaps.append(Gap(ident, gap, position))
                    ident += 1
                gap = ''
                position = []

        # End of the row
        if gap != '' and gap != '0':
            gaps.append(Gap(ident, gap, position))
            ident += 1
                        
        gap = ''
        position = []
    
    return gaps

# Updates the intersection variable of Gap with the intersections found with other gaps
def update_intersections(gapsH, gapsV):
    for gap1 in gapsH:
        for gap2 in gapsV:
            for pos in gap1.position:
                if pos in gap2.position:
                    gap1.intersections.append(pos)
                    gap2.intersections.append(pos)


def update_possible_words(words, gaps):
    word_dict = {}

    for gap in gaps:
        if len(gap.word) not in word_dict.keys():
            word_list = []
            for word in words:
                if len(word) == len(gap.word):
                    word_list.append(word)
            word_dict[len(gap.word)] = np.array(word_list)

    print(word_dict.keys())
        
    for gap in gaps:
        gap.possible_words = word_dict[len(gap.word)]


def main():
    board = read_file("txt/crossword_CB_v3.txt")
    words = read_file("txt/diccionari_CB_v3.txt")
    
    gaps_h = getGaps(board, 0)
    gaps_v = getGaps(board.T, len(gaps_h)) # We use board.T to search the columns

    for gap in gaps_v: # Since we used board.T we have to invert the position values
        for i in gap.position:
            aux = i[0]
            i[0] = i[1]
            i[1] = aux
    
    update_intersections(gaps_h, gaps_v)            
    
    gaps = gaps_h + gaps_v   
    np.array(gaps)
   
    update_possible_words(words, gaps)

    print(board, "\n")
    for gap in gaps:
        print(gap.id, "inter:", gap.intersections, "words:", gap.possible_words)

    
    
if __name__ == "__main__":
    main()