my_file = open("um-server-01HW1.log")

for line in my_file:
    line = line.rstrip()

    #index below refers to first three characters in line
    day = line[0:3]
    if day == "Mon":
        print line
