import re


def passlistchecker():
    with open('passlist.txt', 'r') as file:
        for line in file:
            Bigcheck = (re.findall('[A-ZА-Я]', line))
            Speccheck = (re.findall('[.,:;!_*-+()/#¤%&)]', line))
            Numbercheck = (re.findall('[0123456789]', line))

            if len(Bigcheck) <= 0:
                pass
            elif len(Speccheck) <= 0:
                pass
            elif len(Numbercheck) <= 0:
                pass
            elif len(line) < 8:
                pass
            else:
                print("Пароль соответствует требованиям: ",line)

passlistchecker()
