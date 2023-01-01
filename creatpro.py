import os
import sys


def creatP(num):
    dirPath = "./problem" + num + "/"
    fileName = "pro" + num + ".py"
    os.makedirs(dirPath)
    with open(dirPath + fileName, 'w') as f:
        head = '''import sympy\nimport numpy as np\nimport sys\nsys.path.append("D:\Documents\codePractice\eulerProject")\n\n'''
        f.write(head)
    print(dirPath + fileName + " is created")
    return


num = sys.argv[1]
creatP(num)
