import sys

def encodeString(stringVal):
    encodedList = []
    prevChar = stringVal[0]
    count = 0
    # Parse through String given as argument
    for char in stringVal:
        # If current character is different from previous character append character to list with the number of occurences of previous character
        if prevChar != char:
            encodedList.append((prevChar, count))
            count = 0
        # If previous and current characters are the same iterate the character and increase count
        prevChar = char
        count = count + 1
    
    # If last charcter has been completed append remaining data held
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedString = ''
    
    for item in encodedList:
        decodedString = decodedString + item[0] * item[1]
    
    return decodedString

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''

art2 = '''

    a@@@@@@@@a  a@@@@@@a  a@@@@@@@a a@@@@@@@@a a@@a.  .a@@a  a@@a 
    @@@@  @@@@ @@@@  @@@@ @@@@  @@@ @@@@@@@@@@ @@@@a  a@@@@  @@@@ 
    @@@@  @@@@ @@@@  @@@@ @@@@  @@@    @@@@    `@@@@  @@@@'  @@@@ 
    @@@@@@@@@@ @@@@@@@@@@ @@@@@@@@'    @@@@      `@@@@@@'    @@@@ 
    @@@@@@@@@' @@@@@@@@@@ @@@@@@@@a    @@@@        @@@@      `@@' 
    @@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@ 
    @@@@       @@@@  @@@@ @@@@ @@@@    @@@@        @@@@       @@

'''


encodedString = encodeString(art)

print(encodedString)

print(decodeString(encodedString))

encodedString2 = encodeString(art2)

print(encodedString2)

print(decodeString(encodedString2))