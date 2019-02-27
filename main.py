tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    colWidths = [0] * len(list)

    # Αποθηκεύω το width της κάθε λέξης σε μεταβλητές, τις περνάω σε μια λίστα, τη σορτάρω και παίρνω την υψηλότερη τιμή.
    #Παράδειγμα για την πρώτη γραμμή του tableData. (Πιο εύκολος τρόπος να συγκρίνω μεταβλητές και να πάρω τη μεγαλύτερη;)
    a0 = len(list[0][0])
    b0 = len(list[0][1])
    c0 = len(list[0][2])
    d0 = len(list[0][3])
    sumList = [a0, b0, c0, d0]
    sumList.sort()
    colWidths[0] = sumList[-1]
    print(colWidths[0])

    #Δεύτερη γραμμή:
    a1 = len(list[1][0])
    b1 = len(list[1][1])
    c1 = len(list[1][2])
    d1 = len(list[1][3])
    sumList = [a1, b1, c1, d1]
    sumList.sort()
    colWidths[1] = sumList[-1]
    print(colWidths[1])

    #Τρίτη γραμμή:
    a2 = len(list[2][0])
    b2 = len(list[2][1])
    c2 = len(list[2][2])
    d2 = len(list[2][3])
    sumList = [a2, b2, c2, d2]
    sumList.sort()
    colWidths[2] = sumList[-1]
    print(colWidths[2])

    #Αυτό πρέπει να γίνει αυτόματα για κάθε γραμμή του tableData.
    #Το πρόβλημά μου είναι ότι σε loop αντικαθίστανται οι μεταβλητές συνεχώς και δεν αποθηκεύονται εκτός loop αυτές που θέλω.

    # for i in range(len(list)):
        # colWidths = [i] * len(list)       πώς το κάνω αυτό σε loop ;
        # for j in range(len(list[0])):
        #     ai = len(list[i][j])
        #     bi = len(list[i][j])
        #     ci = len(list[i][j])
        #     di = len(list[i][j])
        #     sumList = [ai, bi, ci, di]
        #     sumList.sort()
        #     colWidths[i] = sumList[-1]
        #     print(colWidths[i])
    for j in range(len(list[0])):
        for i in range(len(list)):
            print(list[i][j].rjust(colWidths[i]),end= ' ')
        print('')
printTable(tableData)
