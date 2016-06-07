from collections import defaultdict
#gets the sequence of a cds based of the protein id.
class getTranscriptSequence(object):
    def __init__(self):
        #path to the cds file.
        self.path = "/home/rutgero/Desktop/RatCDSFastaKoe.fasta"
        #new dictionary containing strings
        self.refSeqDict = defaultdict(str)
        self.getSequences()
    #creates a dictionary of protein ids and sequences as value.
    def getSequences(self):
        ID = ""
        seq = ""
        #for each line in the fastafile.
        for line in open(self.path,"r"):
            #if the line starts with >
            if line.startswith(">"):
                #and ID and seq are not empty
                if ID != "" and seq != "":
                    #split the ID
                    splittedID = ID.split(" ")
                    #and add the id and the sequence to the dictionary
                    self.refSeqDict[splittedID[0]] = seq
                #if the line starts with > set the line as ID and empty sequence
                ID = line.strip(">")
                seq = ""
            #if the line does not start with > add it to the seq.
            else:
                seq += line.strip("\n")
        #once everything is done the last ID and sequence have not been added so they are added here.
        self.refSeqDict[ID] = seq
    #checks if the given reference is in the dict and if so returns the sequences that belongs to it.
    def checkRef(self, reference):
        if reference in self.refSeqDict:
            return self.refSeqDict[reference]
