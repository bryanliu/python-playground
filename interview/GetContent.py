import os
import errno
import CSharp_Lib
import sys, getopt

def GetContentPy(Path:str, TotalCount = -1, Tail = None, ReadCount = 1):
    
    # TotalCount and Tail should not be specified at the same time.
    # Throw out terminating error if this is the case.
    if Tail != None and TotalCount != -1:
        raise Exception("TotalCount and Tail should not be specified at the same time")

    # Don't read anything 
    if TotalCount == 0:
        return None 

    try:
        openedFile = open(Path, "r")
    except:
        raise Exception("File Not Found")

    countRead = 0
    
    # If Tail is null, we are supposed to read all content out. This is same
    # as reading forwards. So we read forwards in this case.
    # If Tail is positive, we seek the right position. Or, if the seek failed
    # because of an unsupported encoding, we scan forward to get the tail content.
    if isinstance(Tail, int) and Tail > 0: 
        CSharp_Lib.SeekFromTail(openedFile, Tail)

    if isinstance(TotalCount, int) and TotalCount != 0: 
        countToRead = ReadCount       

        results = []
        while True:
            # Make sure we only ask for the amount the user wanted
            # I am using TotalCount - countToRead so that I don't
            # have to worry about overflow
            if TotalCount > 0 and (TotalCount - countToRead < countRead): 
                countToRead = TotalCount - countRead
            elif countToRead == 0:
                countToRead = TotalCount
  
            try:
                blockResult = CSharp_Lib.ReadLines(openedFile, countToRead)
            except:
                raise Exception("Read fail")

            countRead += len(blockResult)
            results += blockResult
            if len(blockResult) == 0 or (TotalCount >= 0 and countRead >= TotalCount):
                break

        openedFile.close()
        # if TotalCount > 0:
        #     results = results[:TotalCount]
        print(results)
        return results

if __name__ == "__main__":

    path, totalcount,readcount = None, -1, 1
    para = sys.argv[1:]
    for i in range(0, len(para), 2):
        print(para[i], para[i+1])
        if para[i] == '-path':
            path = para[i+1]
        elif para[i] == '-TotalCount':
            totalcount = int(para[i+1])
        elif para[i] == '-ReadCount':
            readcount = int(para[i+1])

    print(path, totalcount, readcount)
    # for opt, arg in opts:
    #     print(opt, arg)
    GetContentPy(path, totalcount, None, 1)