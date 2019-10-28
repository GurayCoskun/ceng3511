from constraint import *
def load_data():
    '''
    kullanıcıdan input alıp,yazdırmak
    a=input()
    b=input()
    c=input()
    d=input()
    e=input()
    f=input()


    valueTxt = open("futoshiki_input.txt", "w")
    valueTxt.write(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f)'''


    value=open("futoshiki_input.txt","r")
    valueList = []
    for i in value:
        valueList.append(i.strip().split(", "))
    return valueList
def main():
    valueList=load_data()
    futoshiki= Problem()

    futoshiki.addVariables(["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4","C1", "C2", "C3", "C4", "D1", "D2" ,"D3", "D4"], [1, 2, 3, 4])

    futoshiki.addConstraint(AllDifferentConstraint(), ["A1", "A2", "A3", "A4"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["B1", "B2", "B3", "B4"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["C1", "C2", "C3", "C4"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["D1", "D2", "D3", "D4"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["A1", "B1", "C1", "D1"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["A2", "B2", "C2", "D2"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["A3", "B3", "C3", "D3"])
    futoshiki.addConstraint(AllDifferentConstraint(), ["A4", "B4", "C4", "D4"])


    for k in valueList:
        a = k[0]
        b = k[1]
        if b.startswith(("1", "2", "3", "4")):
            b = int(b)
            futoshiki.addConstraint(ExactSumConstraint(b), [a])
        else:
            futoshiki.addConstraint(lambda a, b : a > b, [a, b])

    solutionSet = futoshiki.getSolutions()[0]

    output = str(solutionSet["A1"]) + ", " + str(solutionSet["A2"]) + ", " + str(solutionSet["A3"]) + ", " + str(solutionSet["A4"]) + "\n" + \
             str(solutionSet["B1"]) + ", " + str(solutionSet["B2"]) + ", " + str(solutionSet["B3"]) + ", " + str(solutionSet["B4"]) + "\n" + \
             str(solutionSet["C1"]) + ", " + str(solutionSet["C2"]) + ", " + str(solutionSet["C3"]) + ", " + str(solutionSet["C4"]) + "\n" + \
             str(solutionSet["D1"]) + ", " + str(solutionSet["D2"]) + ", " + str(solutionSet["D3"]) + ", " + str(solutionSet["D4"])

    futoshiki_output = open("futoshiki_output.txt", "w")
    futoshiki_output.write(output)
if __name__=="__main__":
    main()