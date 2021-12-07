fail = open ("konto.txt", encoding="UTF-8")
for tehing in fail:
    if float(tehing) > 0:
        print(tehing[:-1])
fail.close()