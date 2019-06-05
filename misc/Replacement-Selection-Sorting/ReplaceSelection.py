#!/usr/bin/env python

# Filename: ReplaceSelection.py


# ---------------------------------Data Struct----------------------------------
from time import ctime


class RSNode:
    '''The struct of the Replace_Selection method'''

    def __init__(self, rowNum, value):
        self.rowNum = rowNum
        self.value = value
# ---------------------------------Loser Tree-----------------------------------


def createLoserTree(loserTree, dataArray, n):
    for i in range(n):
        loserTree.append(0)
        dataArray.append(RSNode(1, i-n))

    for i in range(n):
        adjust(loserTree, dataArray, n, n-1-i)


def adjust(loserTree, dataArray, n, s):
    t = (s + n) / 2
    while t > 0:
        # rowNum has a higher Priority than value.
        if dataArray[s].rowNum > dataArray[loserTree[t]].rowNum:
            s, loserTree[t] = loserTree[t], s
        elif dataArray[s].rowNum == dataArray[loserTree[t]].rowNum and dataArray[s].value > dataArray[loserTree[t]].value:
            s, loserTree[t] = loserTree[t], s
        t /= 2
    loserTree[0] = s
# -------------------------------------Use---------------------------------------


# A method to write file.


def writeFile(tarDir, tmp):
    file_writer = open(tarDir, 'a+')
    file_writer.writelines(tmp)
    file_writer.close()
    # Clear the array tmp.
    while tmp:
        tmp.pop()


def splitFile(fileLocation, tarDirectory, n):
    file_reader = open(fileLocation, 'r')
    loserTree = []
    dataArray = []
    n = int(n)
    createLoserTree(loserTree, dataArray, n)
    line = file_reader.readline()
    # First, read file, fill the data array with front items of the file.
    for i in range(n):
        dataArray[i] = RSNode(1, line)
        # Adjust the loser tree after every change of the data array.
        adjust(loserTree, dataArray, n, i)
        line = file_reader.readline()
    lastRowNum = 1  # Used to name the new little files.
    lastSmall = dataArray[loserTree[0]]  # lastSmall is a mark...
    # You know, it's a temporary array to storage sorted ips.
    tmp = [lastSmall.value]
    dataArray[loserTree[0]] = RSNode(lastRowNum, line)
    while True:
        # Write tmp into file if it's size reach the Maximum we defined.
        if len(tmp) == n:
            writeFile(tarDirectory + 'file' + str(lastRowNum) + '.txt', tmp)

        # Adjust the loser tree after every change of the data array.
        adjust(loserTree, dataArray, n, loserTree[0])

        # Finish one trip of search and finish one file.
        if dataArray[loserTree[0]].rowNum > lastRowNum:
            writeFile(tarDirectory + 'file' + str(lastRowNum) + '.txt', tmp)
            lastRowNum += 1

            lastSmall = dataArray[loserTree[0]]
            tmp.append(lastSmall.value)
            line = file_reader.readline()
            if line:  # Reach the end of the file
                dataArray[loserTree[0]] = RSNode(lastRowNum, line)
            else:
                break
        else:
            # Can add new item into the tmp.
            if dataArray[loserTree[0]].value > lastSmall.value:
                lastSmall = dataArray[loserTree[0]]
                tmp.append(lastSmall.value)
                line = file_reader.readline()
                if line:  # Reach the end of the file
                    dataArray[loserTree[0]] = RSNode(lastRowNum, line)
                else:
                    break
            else:
                # rowNum + 1 and return to adjust.
                dataArray[loserTree[0]].rowNum += 1

    # Don't forget to write the items in the loser tree into the file.
    dataArray[loserTree[0]] = RSNode(lastRowNum+10, 'F')
    while True:  # This loop almost like the one above.
        if len(tmp) == n:
            writeFile(tarDirectory + 'file' + str(lastRowNum) + '.txt', tmp)

        adjust(loserTree, dataArray, n, loserTree[0])
        if dataArray[loserTree[0]].value == 'F':
            break

        if dataArray[loserTree[0]].rowNum > lastRowNum:
            writeFile(tarDirectory + 'file' + str(lastRowNum) + '.txt', tmp)
            lastRowNum += 1

            lastSmall = dataArray[loserTree[0]]
            tmp.append(lastSmall.value)

            dataArray[loserTree[0]] = RSNode(lastRowNum+10, 'F')
        else:
            if dataArray[loserTree[0]].value > lastSmall.value:
                lastSmall = dataArray[loserTree[0]]
                tmp.append(lastSmall.value)

                dataArray[loserTree[0]] = RSNode(lastRowNum+10, 'F')
            else:
                dataArray[loserTree[0]].rowNum += 1

    # And don't forget tmp. If tmp is not empty, write it into file.
    if tmp:
        writeFile(tarDirectory + 'file' + str(lastRowNum) + '.txt', tmp)

    file_reader.close()


# ----------------------------Test-------------------------------------
if __name__ == '__main__':
    import sys
    from time import ctime
    try:
        fileLocation = sys.argv[1]
        tarDir = sys.argv[2]
        n = sys.argv[3]
    except:
        print 'Wrong Arguments!'
        print '''You neew 3 Parameters in total.
	1. The path of your file.
	2. The path of the target files.
	3. The size of the LoserTree.
You should do like this:
	python ReplaceSelect.py /root/hehe.txt /root/hehe/ 6'''
        sys.exit()
    timeNow = ctime()
    print 'Now the time is ' + str(timeNow) + ','
    print 'and the work is coming, please to wait...'
    splitFile(fileLocation, tarDir, n)
    print 'Work Over!'
    print 'Now the time is ' + str(ctime())

# ---------------------
# Author: Hippie
# Via: CSDN
# Origin: https://blog.csdn.net/u010439949/article/details/8910769
