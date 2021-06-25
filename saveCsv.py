import csv
"""
-목적:
list of lists를 csv파일로 생성함.
list에 dict가 포함되어 있으면, csv.writer가 dict의 value가 아닌 key값을 저장함.
새 list(resultlines)로 만들어 value()만 문자열 list로 변경함(dict는 제거).  
"""
def saveCsv(filename,listoflists):
    csvfile = open(filename, 'w', encoding='utf-8', newline='')
    csvwriter = csv.writer(csvfile)

    resultlines = []
    line = []

    for list1 in listoflists:
        line.clear()
        if type(list1) ==list:
            for list2 in list1:
                if type(list2) == dict:
                    for dictVal in list2.values():
                        line.append(dictVal)
                elif type(list2) == str:
                    line.append(list2)
        # resultlines.append(resultline) , shallow copy
        # resultlines.append(list(resultline)) , deep copy
        resultlines.append(list(line))

    for line in resultlines:
        print(line)
        csvwriter.writerow(line)
    csvfile.close()


if __name__ == '__main__':
    var=[['list1','list2',{"dict1key":"dict1val","dict2key":"dict2val","dict3key":"dict3val"}],
                 [{"dict4key":"dict4val","dict5key":"dict5val","dict6key":"dict6val"},'list3','list4']]
    saveCsv("test.csv", var)

