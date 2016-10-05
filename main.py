#coding = utf-8

from lz77 import lz77_decode, lz77_encode
import sys
__author__ = "zyj356a"

def main():
    raw_file = open("example","rb")
    lines = lz77_decode.file_to_oneline(raw_file.readlines())
    print lines
    lz77_encode.encode(lines)
    raw_file.close()
    encoded_file = open("encode","rb")
    result = open("result","wb")
    lz77_decode.decode(encoded_file,result)
    result.close()
    encoded_file.close()
    command = raw_input("Please enter q to exit this app. \n")
    if(command == 'q' ):
        sys.exit()

if __name__ == "__main__":
    main()