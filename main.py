tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidths = [0] * len(list)
    for i in range(len(list)):
        for j in range(len(list[0])):
            colWidths[i] = len(list[i][j])
            if colWidths[i] < len(list[i][j-1]):
                colWidths[i] = len(list[i][j-1])
        
    for j in range(len(list[0])):
        for i in range(len(list)):
            print(list[i][j].rjust(colWidths[i]),end= ' ')
        print('')
printTable(tableData)
