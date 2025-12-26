from parser import Parser
from SymbolHandler import SymbolHandler

def main():
    p = Parser()
    lines = p.parse_file_lines("MaxL.asm")
    
    # First pass: find all labels
    sh = SymbolHandler(lines)
    sh.find_label_symbols()
    
    # Second pass: translate everything to binary
    binaryLines = []
    for line in lines:
        # Skip labels because they are like pseudo code do not produce output
        if line.startswith('('):
            continue
        
        # Try predefined symbols
        result = sh.translate_predefined_Symbols(line)
        if result:
            binaryLines.append(result)
            continue
        
        # Try variables
        result = sh.translate_var_symbols(line)
        if result:
            binaryLines.append(result)
            continue
        
        # Must be numeric A-instruction or C-instruction
        if line.startswith('@'):
            # Numeric A-instruction like @5
            result = p.a_instruction_handler(line)
            binaryLines.append(result)
        else:
            # C-instruction like D=A or D;JMP
            result = p.c_instruction_handler(line)
            binaryLines.append(result)
    
    # Write to .hack file
    outputFilename = "MaxL.hack"
    with open(outputFilename, 'w') as f:
        f.write('\n'.join(binaryLines))
    
    print(f"Assembly complete! Output written to {outputFilename}")

if __name__ == '__main__': 
    main()


