from SymbolsTable import symbolTable
from parser import Parser
class SymbolHandler:
    def __init__(self, lines):
        self.lines = lines
        self.p = Parser()
        self.symbolTable = symbolTable.copy()
        self.n = 16


    def translate_predefined_Symbols(self, line):
        """look up predefined symbols if they exist and translate their value pair."""
        symbol = line[1:]
        if line.startswith('@') and symbol in self.symbolTable:
            pdl_value = self.symbolTable[symbol]
            translated_label = self.p.dec_to_binary_translator(pdl_value)
            return '0' + translated_label
        return None  

            


    def find_label_symbols(self):
        """First pass through all lines in file to find label symbols, assign them the running instruction counter value, and store them in symbols table. """
        instruction_counter = 0
        for line in self.lines:
            if line.startswith('('):
                label_name = line[1:-1]
                self.symbolTable[label_name] = instruction_counter
            else:
                instruction_counter += 1



    def translate_var_symbols(self, line):
        """Translated and store variables in symbol table. This is the second pass"""
        var_name = line[1:]
        if line.startswith('@') and var_name not in self.symbolTable and not var_name.isdigit():
            self.symbolTable[var_name] = self.n
            translated_var = self.p.dec_to_binary_translator(self.symbolTable[var_name])
            self.n += 1
            return '0' + translated_var
        return None



        


