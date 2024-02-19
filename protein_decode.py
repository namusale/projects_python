'''Ths program works to decode the codons present in the protein RNA. The stages involved are segmenting the
protein in strings of length 3. Once the strings are identified as stops, sequencing ceases.The 3 lengthed strings are
 looked up to a dictionary after which they are protein list is updated arccodingly. '''

RNA = "AUGUUUUCUUAAAUG" # Protein sequence

# Dictionary for looking up the codorns to their corresponding proteins(Extract)

codons =  {
            "AUG": "Methionine",
            "UUU": "Phenylalanine" ,
            "UUC": "Phenylalanine",
            "UCU": "Serine",
            "UUA": "Leucine ",
            "UAA": "stop",
            "UAG":"stop",
              "UGA":"stop",
            "UCU": "Serine",
            "UCC": "Serine",
            "UCA": "Serine",
            "UCG": "Serine",
            "UGU":"Cysteine",
              "UGC":"Cysteine",
               "UAU":"Tyrosine", 
               "UAC":	"Tyrosine"
            }

#Lists to hold data
seg = []
protein_list =[]


'''The decode function decodes the received codon (as an argument) by looking up the dictionary and updates
   the protein list with corresponding proteins found in the sequence.'''

def decode(codon):
    for item in codons:
        if (codon == item):
            protein_list.append(codons[item])
           

'''The segment function  receives the sequence and segments it into lists of length 3 (codons). The stop cordon 
is identified and codon segmentation stops. The function then calls on 
the decode function that looks up the codons for the corresponding proteins.'''

def segment(RNA):
    seg_holder = []

    for i in range(0,len(RNA)):
       seg.append(RNA[i])
       if (len(seg) == 3):
           #print(seg)
           new_cordon = str("".join(seg))
           if new_cordon != "UAA":
            #print(new_cordon)
                seg.clear()
                decode(new_cordon)
            
           else:
                break
           


# The translator function prints the RNA sequence and its corresponding proteins by calling the segment function for detail
           
def translator():
    segment(RNA)
    print('')  
    print('')  
    print("===================================================================================================") 
    print('')  
    print('')  
    print('')  
    print("                            PROTEIN TRANSLATOR")
    print('')
    print('') 
    print('====================================================================================================')
    print('') 
    print('') 
    print(f"  RNA Sequence: {RNA} has  {' '.join(protein_list)} proteins ")
    print('')  
    print('')  
    print('')    

translator()




    

        
            


