From_file = open("allafromtestforurl.txt")
for each_line in From_file:
    if "http" in each_line:
        pass
    else :
        if "javascript:void(0)" in each_line:
            pass
        else:
            fq = open("allurl.txt", "a+", encoding='utf-8')
            fq.write("https://docs.ucloud.cn" + each_line)
            print(each_line)