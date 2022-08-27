Origin=input()
Origin=Origin.lower()

SymbolCount={}
for char in Origin:
    SymbolCount[char]=SymbolCount.get(char,0)+1

Output=""
for char in Origin:
    if SymbolCount.get(char)>1:
        NextSymbol=')'
    else:
        NextSymbol='('
        
    Output+=NextSymbol

print(Output)
