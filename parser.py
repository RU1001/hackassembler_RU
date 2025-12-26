import cTables
class Parser:

    def parse_file_lines(self,filename):
        """Read a file and return lines without comments or whitespace."""
        parsedLines = []
        with open(filename) as f:
            for line in f:
                line = line.split('//')[0].strip()  # Remove inline comments
                if line:
                    parsedLines.append(line)                    
        return parsedLines
    

    
    def process_lines(self,lines):
        """Read a line and determine what type of instruction it is. Based on the instruction do something."""
        processedLines = []
        for line in lines:
            if line.startswith("@"):
                processedLines.append(self.a_instruction_handler(line))
            else:
                processedLines.append(self.c_instruction_handler(line))
        return processedLines




    def a_instruction_handler(self,aLine):
        address = aLine[1:]
        addressinBinary = self.dec_to_binary_translator(address)
        return  '0' + addressinBinary


    
    def c_instruction_handler(self,cLine):
        """Splitting parts of c instructions, finding them and tables putting together binary string. """
        #comp = dest + jmp
        if '=' in cLine:
            jump = 'null'
            splitLine = cLine.split('=')
            dest = splitLine[0]
            comp = splitLine[1]
        else:
            dest = 'null'
            splitLine = cLine.split(';')
            comp = splitLine[0]
            jump = splitLine[1]

        compDict = cTables.comp
        destDict = cTables.dest
        jumpDict = cTables.jump

        comp = compDict[comp] #retrieve matching comp, dest, and jump bits
        dest = destDict[dest]
        jump = jumpDict[jump]

        translatedCinstruction = '111' + comp + dest + jump
        return translatedCinstruction




    def dec_to_binary_translator(self,decValue):
        numOfBits = 15
        binOfVal = bin(int(decValue))[2:]
        pad = ''
        for i in range(numOfBits - len(binOfVal)):
            pad = '0' + pad
        return pad + binOfVal






    



