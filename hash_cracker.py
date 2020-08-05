import crypt
import sys

if __name__ == "__main__":
    reader = open(sys.argv[1], "r")
    dict_file = open(sys.argv[2], "r")
    writer = open("results.txt", "w")
    #writer = open("user_pass", "w")
    try:
        entries = [[i.split(":")[0], i.split(":")[1].split("$")[2], i.split(":")[1].split("$")[3]] for i in list(reader)]
        w = [p.rstrip() for p in list(dict_file)]
        results = []
        p = ""
        counter_yes = 0
        counter_no = 0
        for i in entries:
            flag = True
            for x in w:
                
                p = crypt.crypt(x, "$6$"+i[1]) 
                if p == "$6$"+i[1]+"$"+i[2] :
                    flag = False
                    s = "[+] Password Found! User: {} || Password: {}\n".format(i[0], x)
                    print(s)
                    counter_yes += 1
            if flag:
                s = "[-] Password not found for User: {}\n".format(i[0])
                print(s)
                counter_no += 1
            results.append(s)

        end = "\n Passwords found: {} Uncracked passwords: {}\n".format(counter_yes, counter_no)
        print(end)
        results.append(end)
        writer.writelines(results)

    finally:
        reader.close()
        writer.close()
