#coding:utf-8
import lz77_decode

def encode(lines):
    anchor = -1 #全局参考位置
    search_window_size = 10 #字典窗口大小
    lookhead_window_size = 10 #缓冲区大小
    f = file("encode","wb")
    file_length = len(lines)
    lookhead_buffer = ""
    search_buffer = ""
    while(anchor <= file_length):
        if(anchor<search_window_size):
            search_buffer = lines[0:anchor+1]
            lookhead_buffer = lines[anchor+1:anchor+2+lookhead_window_size]
        else:
            search_buffer = lines[anchor-search_window_size+1:anchor+1]
            if(anchor+lookhead_window_size > file_length):
                lookhead_buffer = lines[anchor+1:]
            else:
                lookhead_buffer = lines[anchor+1:anchor+lookhead_window_size]
        #print "search_buffer",search_buffer
        #print "lookhead_buffer",lookhead_buffer
        head_char = ""
        next_char = ""
        head_char_length = 0
        for each_char in lookhead_buffer:
            head_char = head_char + each_char
            if head_char in search_buffer:pass
            else:break
        head_char_length = len(head_char)

        try:
            next_char = head_char[-1]
        except IndexError:
            break
        head_char = head_char[0:-1]
        #返回最长匹配字符串第一个字母的索引
        try:
            head_index = search_buffer.index(head_char)
        except ValueError:
            f.write(str((0,0,next_char)))
            #print (0,0,next_char)
            anchor += 1
        else:
            f.write("(%d,%d,%s)" %(head_index,head_char_length-1,next_char))
            #f.write(str(head_index)+str(head_char_length-1)+str(next_char))
            print (head_index,head_char_length-1,next_char)
            anchor = anchor + head_char_length
        #print "anchor",anchor
    f.close()

if __name__ == "__main__":
    example = lz77_decode.file_to_oneline(file("example","rU").readlines())
    encode(example)