#coding = utf-8
import re

def file_to_oneline(file_lines):
    lines = ""
    for line in file_lines:
        lines = lines + line
    return str(lines)

def decode(encode_f,result_f):
    txt = ""
    search_window_size = 10
    look_head_size = 600
    encoding = file_to_oneline(encode_f)
    result1 = re.finditer("\\(.+?\\)|\\(.+?\s\\)",encoding)
    for item in result1:
        tmp_code = item.group()[1:-1]
        tmp2_code = re.split(r"\,", tmp_code)
        if (len(txt) <= search_window_size):
            buff = txt
        else:
            buff = txt[-search_window_size:]
        offset = int(tmp2_code[0])
        length = int(tmp2_code[1])
        if (len(tmp2_code) == 4):
            next_char = ","
        else:
            next_char = tmp2_code[2]
        if(offset == 0 and length == 0):
            txt += next_char
        else:
            txt += (buff[offset:offset+length] + next_char)
    print txt
    result_f.write(txt)

if __name__ == "__main__":
    encode_f = open("encode","rU")
    decode_f = open("result","wb")
    decode(encode_f,decode_f)
    encode_f.close()
    decode_f.close()