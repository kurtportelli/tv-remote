def tv_remote(word):
    #define the starting conditions
    keyboard = ('abcde123',
                'fghij456',
                'klmno789',
                'pqrst.@0',
                'uvwxyz_/')
    previous_x, previous_y = 0, 0
    presses = 0
    
    for char in word:
        #find the coordinates of the current character
        for row in range(len(keyboard)):
            if char in keyboard[row]:
                y = row
                x = keyboard[row].index(char)
                break
        
        presses += abs(x - previous_x) + abs(y - previous_y) + 1
        previous_x, previous_y = x, y
    
    return presses
