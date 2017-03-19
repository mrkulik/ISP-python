import tempfile

# split file


def sort_first(file_input, buffer_size, arg_reverse, line_separator, field_separator, key):
    def key_sort(string):
        list_sort = string.split(field_separator)
        return list_sort[key - 1]
    array = list()
    buf_ar = list()
    buffer_count = 0
    temp = tempfile.TemporaryFile()
    f = open(file_input, 'r+')
    while True:
        s = f.readline()
        if not s:
            if buffer_count > 0:
                if key == 0:
                    buf_ar.sort(reverse=arg_reverse)
                else:
                    buf_ar.sort(key=key_sort, reverse=arg_reverse)
                for e in buf_ar:
                    temp.write(e)
                array.append(temp)
                temp = tempfile.TemporaryFile()
            break
        else:
            buffer_count += len(s)
            if buffer_count <= buffer_size:
                buf_ar.append(s)
            else:
                f.seek(f.tell() - len(s))
                if key == 0:
                    buf_ar.sort(reverse=arg_reverse)
                else:
                    buf_ar.sort(key=key_sort, reverse=arg_reverse)
                for e in buf_ar:
                    temp.write(e)
                buf_ar = []
                array.append(temp)
                buffer_count = 0
                temp = tempfile.TemporaryFile()
    f.close()
    temp.close()
    return array

# merge


def combine(left, right, arg_reverse, line_separator, field_separator, key):
    temp = tempfile.TemporaryFile()
    left.seek(0)
    right.seek(0)
    flag_l = True
    flag_r = True
    str_l = left.readline()
    if not str_l:
        flag_l = False
    str_r = right.readline()
    if not str_r:
        flag_r = False
    str_l_cmp = str_l
    str_r_cmp = str_r
    while flag_l and flag_r:
        str_l_cmp = str_l
        str_r_cmp = str_r
        if key > 0:
            str_l_cmp = str_l.split(field_separator)[key - 1]
            str_r_cmp = str_r.split(field_separator)[key - 1]

        if arg_reverse:
            if str_l_cmp > str_r_cmp:
                temp.write(str_l)
                str_l = left.readline()
                if not str_l:
                    flag_l = False
            else:
                temp.write(str_r)
                str_r = right.readline()
                if not str_r:
                    flag_r = False
        else:
            if str_l_cmp < str_r_cmp:
                temp.write(str_l)
                str_l = left.readline()
                if not str_l:
                    flag_l = False
            else:
                temp.write(str_r)
                str_r = right.readline()
                if not str_r:
                    flag_r = False
    if not flag_r:
        left.seek(left.tell() - len(str_l))
        for strr in left:
            temp.write(strr)
    elif not flag_l:
        right.seek(right.tell() - len(str_r))
        for strr in right:
            temp.write(strr)
    return temp

# call combine for merge


def marge(file_output, array_file, arg_reverse, line_separator, field_separator, key):
    buf_ar = []
    array = array_file
    while len(array) > 1:
        if len(array) % 2 != 0:
            for i in range(0, len(array) - 2, 2):
                buf_ar.append(combine(array[i], array[i + 1], arg_reverse, line_separator, field_separator, key))
            buf_ar.append(array[len(array) - 1])
        else:
            for i in range(0, len(array) - 1, 2):
                buf_ar.append(combine(array[i], array[i + 1], arg_reverse, line_separator, field_separator, key))
        array = buf_ar
        buf_ar = []
    array[0].seek(0)
    f = open(file_output, 'w')
    for item in array[0]:
        f.write(item)
    f.close()


def check(file_name):  #check parametres
    f = open(file_name, 'r')
    s = f.readline()
    s1 = f.readline()
    if s > s1:
        while True:
            s = s1
            s1 = f.readline()
            if not s1:
                print 'sorted reverse'
                break
            if s < s1:
                print "non sorted"
                break
    else:
        while True:
            s = s1
            s1 = f.readline()
            if not s1:
                print 'sorted'
                break
            if s > s1:
                print "non sorted"
                break


def sort(file_input, file_output, buffer_size, arg_reverse, line_separator, field_separator, key):
    marge(file_output, sort_first(file_input, buffer_size, arg_reverse, line_separator, field_separator, key),
          arg_reverse, line_separator, field_separator, key)

if __name__ == '__main__':
    sort('file_input.txt', 'mas_sort.txt', 45, True, '\n', '\t', 2)
