# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 01:15:19 2020

@author: prade
"""

class Protocol:
    
    num_of_processors = 4
    
    number_of_cache = num_of_processors
    
    size_of_memory = 4
    
    bus = ""
    
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
                "memory_block": {"W":None, "X":None, "Y": None, "Z":None}
                }},
        
        {"processor1": {
                "cache_status": "I",
                "memory_block": {"W":None, "X":None, "Y": None, "Z":None}
                }},
                
        {"processor2": {
                "cache_status": "I",
                "memory_block": {"W":None, "X":None, "Y": None, "Z":None}
                }},
                
        {"processor3": {
                "cache_status": "I",
                "memory_block": {"W":None, "X":None, "Y": None, "Z":None}
                }}
        ]
    
    def print_status(current_indexing_var, processor_value):
    
        print("Processor: {} Cache Status: {} Memory Location: {}".format(processor_value, current_indexing_var['cache_status'], current_indexing_var['memory_block']))
            
    arry = ['processor0', 'processor1', 'processor2', 'processor3']
    
    #Method is used to show the user the values of Memory and Processors
    def values(option):
        
        if(option == 'memory'):
            
            print("memory values are: ", [i for i in Protocol.memory])
            
        elif(option == 'processor'):
            
            print("procesor values are: ", [i for i in Protocol.arry])
    
    def __init__(self, operator):
        
        self.operator = operator
        
        Protocol.values('memory')

        if operator == 'read':
            
            read_memory_block = input("Enter memory block to read data from: ")
            
            while(True):
                
                if(read_memory_block not in Protocol.memory):

                    print("Please refer to the values: ", Protocol.values('memory'))                    
                    
                    read_memory_block = input("Please re-enter memory block to read data from: ")
                
                else:
                    
                    break
                
            
            print("procesor values are: ", Protocol.arry)
            
            processor = input("Enter processor to read data from: ")
            temp_bool = True
            while(temp_bool):
                
                if(processor not in Protocol.arry):

                    print("Please refer to the values: ", Protocol.values('processor'))
                    
                    processor = input("Please enter proper value of processor to read: ")
                    
                
                else:
                    temp_bool = False
                    
                    self.read(read_memory_block, processor)
                    
                    return None
                    
                
        elif(operator == 'write'):
            
            processor = input("Enter the processor to write: ")
            memory_block =  input("Enter the memory block for cache: ")
            value = input("Enter value to be changed in {}: ".format(memory_block))
            self.write(processor, memory_block, value)
            
        elif(operator == "status"):
            
            self.check_memory_status()
        

    #------ READING FROM A MEMORY BLOCK -------
    def read(self, read_memory_block, processor):
        
        if Protocol.data_structure[Protocol.arry.index(processor)][processor]['memory_block'][read_memory_block] == None:
            
            Protocol.bus = 'Read Miss'
            
            Protocol.data_structure[Protocol.arry.index(processor)][processor]['memory_block'] = Protocol.memory
            
            Protocol.data_structure[Protocol.arry.index(processor)][processor]['cache_status'] = Protocol.states['Shared']
            
            print(Protocol.data_structure[Protocol.arry.index(processor)][processor])
            
            return Protocol.data_structure[Protocol.arry.index(processor)][processor]['memory_block']
        
        print(Protocol.data_structure[Protocol.arry.index(processor)][processor])
        return("No memory block exists")
            
    def write(self, processor, memory_block, value):
        
        if(Protocol.data_structure[Protocol.arry.index(processor)][processor]['cache_status']) == 'I':
            
            #first write the data to cache block of processor
            Protocol.data_structure[Protocol.arry.index(processor)][processor]['memory_block'] = Protocol.memory
            
            Protocol.data_structure[Protocol.arry.index(processor)][processor]['cache_status'] = Protocol.states['Modified']
            
            #changing the value of cache block based on user input
            Protocol.data_structure[Protocol.arry.index(processor)][processor]['memory_block'][memory_block] = value
            
            j = 0
            
            for i in Protocol.data_structure:
                temp_processor_value = Protocol.arry[j]
                if(i[temp_processor_value]['cache_status'] == 'S'):
                    Protocol.data_structure[j][temp_processor_value]['cache_status'] = 'I'
                j = j + 1
                
            
        
        print("For Processor {} the value changed to: {}".format(processor, value))
        
        #self.read(key)
        
        return(' ')
        
        
    def check_memory_status(self):
        
        for i in Protocol.data_structure:
            
            print(i)
    
    
    
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
        
    elif(instruction == 'check status'):
        
        
        protocol = Protocol("status")
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




