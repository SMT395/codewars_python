class VigenereCipher(object):
    def __init__(self, key, alphabet):
        ratio=len(alphabet)/len(key)
        rest=ratio-int(ratio)
        if rest>0:
            charac=list(key)[:int(len(list(key))*rest)]
            key=key*int(ratio)+"".join(charac)
        else:
            key=key*int(ratio)

        self.key=key
        self.alphabet=alphabet
        
        
    def encode(self, text):
        list_abc=list(self.alphabet)
        list_key=list(self.key)
        output=[]
        for lter_w,lter_k in zip(text,self.key):
            if lter_w not in list_abc: output.append(lter_w)
            else:
                i_lter=list_abc.index(lter_w)
                new_alpbet=list_abc[list_abc.index(lter_k):]+list_abc[:list_abc.index(lter_k)]
                output.append(new_alpbet[i_lter])
        return ''.join(output)
    
    def decode(self, text):
        list_abc=list(self.alphabet)
        list_key=list(self.key)
        output_2=[]
        for lter_w2,lter_k2 in zip(text,self.key):
            if lter_w2 not in list_abc: output_2.append(lter_w2)
            else:
                new_alpbet2=list_abc[list_abc.index(lter_k2):]+list_abc[:list_abc.index(lter_k2)]
                i_lter2=new_alpbet2.index(lter_w2)
                output_2.append(list_abc[i_lter2])
        return ''.join(output_2)
