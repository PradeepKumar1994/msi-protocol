# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 01:15:19 2020

@author: prade
"""

class Protocol:
    
    num_of_processors = 4
    
    number_of_cache = num_of_processors
    
    size_of_memory = 4
    
    states = {
            "Modified": "M",
              "Shared": "S",
              "Invalid":"I"
              }
    
    print("Initializing in-memory values..")
    memory = {"W":"Data0", "X":"Data1", "Y":"Data2", "Z":"Data3"}
    print("Initialization complete!")
    
    data_structure = [
        {"processor0": {
                "cache_status": "I",
                "shared": False,
                "memory_block": "None"
                }},
        
        {"processor1": {
                "cache_status": "I",
                "shared": False,
                "memory_block": "None"
                }},
                
        {"processor2": {
                "cache_status": "I",
                "shared": False,
                "memory_block": "None"
                }},
                
        {"processor3": {
                "cache_status": "I",
                "shared": False,
                "memory_block": "None"
                }}
        ]
    
    def print_status(current_indexing_var, processor_value):
    
        print("Processor: {} Cache Status: {} Memory Location: {}".format(processor_value, current_indexing_var['cache_status'], current_indexing_var['memory_block']))
            
    arry = ['processor0', 'processor1', 'processor2', 'processor3']
    
    def __init__(self, operator):
        
        self.operator = operator
        
        if operator == 'read':
            
            read_memory_block = input("Enter memory block to read data from: ")
            self.read(read_memory_block, func='read')
            
        else:
            
            key = input("Enter the memory block key: ")
            value = input("Value to be written in memory block: ")
            self.write(key, value)
        
    
    def initial_state(self):
        
        return("All states are in invalid position since nothing in the memory\
               to verify check memory status by running function check_memory_status")
        
        
    #------ READING FROM A MEMORY BLOCK -------
    def read(self, read_memory_block, func = "read"):
        
        #read_memory_block = 'W'
        #the exception block will handle invalid memory read blocks
        try:
            
            Protocol.memory[read_memory_block]
        
        except:
            
            print("Invalid memory location")
            
            return 1
            
        
        #checking if any processor's cache has already read the block
        for j in Protocol.arry:
            
            current_indexing_var = Protocol.data_structure[Protocol.arry.index(j)][j]['memory_block']
            
            if(current_indexing_var == read_memory_block):
                
                found_or_not_found = "Found"
                
                Protocol.print_status(Protocol.data_structure[Protocol.arry.index(j)][j], j)
                
                return("Found ")
                
            found_or_not_found = "Not Found"
        
        #if none found - processor's cache then look for any cache which is available
        if(found_or_not_found == "Not Found"):
            
            for j in Protocol.arry:
                
                if(not Protocol.data_structure[Protocol.arry.index(j)][j]['shared']):
                    
                    Protocol.data_structure[Protocol.arry.index(j)][j]['shared'] = True
                    
                    if(func == 'read'):
                        
                        Protocol.data_structure[Protocol.arry.index(j)][j]['cache_status'] = 'S'
                    
                    else:
                    
                        Protocol.data_structure[Protocol.arry.index(j)][j]['cache_status'] = 'M'
                    
                    Protocol.data_structure[Protocol.arry.index(j)][j]['memory_block'] = read_memory_block
                    
                    print(Protocol.data_structure[Protocol.arry.index(j)])
                    
                    return("--------------------------------------------------")
                
        return("No memory block exists")
            
    def write(self, key, value):
        
        Protocol.memory[key] = value
        
        print("For Key {} the value changed to: {}".format(key, value))
        
        self.read(key)
        
        return(' ')
        
        
    def check_memory_status(self):
        
        pass
    
    
    
#protocol = Protocol()
print("-------Instructions: ------- \n \
      \n \
      For read hit read \n \
      For write enter write")

instruction = input("Instruction: ")
while(True):
    
    if(instruction == 'read'):
        
        protocol = Protocol("read")
        instruction = input("Instruction: ")
    
    elif(instruction == 'write'):
    
        protocol = Protocol("write")
        instruction = input("Instruction: ")
        
    
    elif(instruction == 'exit'):
        
        print('end of the program')
        break
        
    else:
        
        instruction = input("Instruction: ")
        
print("-------------------------")
#operation = input("Read or write to the memory block: ")
#
#
#
#protocol = Protocol("read")
#
#protocol.read('Z', func='read')
#
#protocol.write('Z', 'GLS')
#
#protocol.write('Z', 'GLS1')
#
#protocol = Protocol("write")
#

#protocol.write("W", "ttt")

#if(operation == "exit"):
    
    #print("---------MSI Protocol ended---------")
    
#while(operation):
    
 #   print("\n Executing", operation, " request")
    
    #MSI Protocol




