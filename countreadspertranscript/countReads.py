import pysam
from collections import defaultdict
from getTranscriptSequence import getTranscriptSequence

class CountReadsPerTranscript(object):
    path = ""
    #a dictionary containing dictionaries with str as key and and int as a value.
    transcriptDict = defaultdict(lambda : defaultdict(int))

    def __init__(self):
        self.path = open("/home/rutgero/Desktop/BN_fasta_files/ERR653341.sam", "r")
        self.newPath = open("/home/rutgero/Desktop/referenceReadsCountedFull.txt","w")
    #reads through the ribo-seq file and saves the content in a dictionary.
    def readFile(self):
        count = 0
        for line in self.path:
            count += 1
            if count%1000000 == 0:
                print(count)
            #skips the headerLines.
            if line.startswith("@"):
                pass
            else:
                splitted = line.split("\t")
                #checks if the sam read does not have a flag of 4 meaning the read did not map.
                if splitted[1] != "4":
                    self.transcriptDict[splitted[2]][splitted[3]] += 1

    #creates a output file with the transcriptDict which is a dictionary containing dictionaries
    def createOutputFile(self):
        getSeq = getTranscriptSequence()
        print("File writing started!")
        #for each reference in the dict
        for reference in self.transcriptDict:
            #number of items in the dictionary that is linked to the reference
            totalRefReadsMapped = 0
            for location in self.transcriptDict[reference]:
                totalRefReadsMapped += int(self.transcriptDict[reference][location])
            #for each startLocation in the dict that is the value of the reference
            for start in self.transcriptDict[reference]:
                if self.transcriptDict[reference][start] <= 4:
                    pass
                else:
                    sequence = getSeq.checkRef(reference)
                    self.newPath.write(reference + "\t" + str(totalRefReadsMapped) + "\t" + str(start) + "\t" +str(self.transcriptDict[reference][start]) + "\t" + sequence + "\n")


A = CountReadsPerTranscript()
A.readFile()
A.createOutputFile()
