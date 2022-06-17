# -*- coding: utf-8 -*-
# @Time : 2022/6/16 19:55
# @Author : zhouzhou
# @FileName: 有限状态机.py
# @Email : 630551760@qq.com
# @Software: PyCharm

class State:
    def __init__(self,state):
        self.state = state



class Token:
    def __init__(self):
        self.type = ""
        self.text = ""

    def getType(self):
        return self.type

    def getText(self):
        return self.text

#保存所有token
tokens = []

#存放临时的token
tempToken = ""

#正在解析的token
token = Token()



#设置初始状态
def initialState(ch):
    #如果已经解析完了token，则保存下来
    global tempToken,token
    if len(tempToken) > 0:
        token.text = tempToken
        tokens.append(token)

        #生成新的tempToken和token
        tempToken = ""
        token = Token()


    #根据第一个字符确定状态
    newState = State("initial")
    #第一个是数字，进入Int状态
    if ch.isdigit():
        newState = State("Int")
        token.type = newState.state
        tempToken += ch
    #第一个是字母，进入id状态
    elif ch.isalpha():
        newState = State("Id")
        token.type = newState.state
        tempToken += ch

    elif ch == ">":
        newState = State("GT")
        token.type = newState.state
        tempToken += ch


    else:
        newState = State("initial")

    return newState


#设置有限状态机

def tokenize(strings):
    global token,tempToken
    #初始化token,tempToken,tokens
    token = Token()
    tempToken = ""


    #初始化状态
    newState = State("initial")
    #开始遍历strings
    for s in strings:
        if newState.state == "initial":
            #确定第一个字符的状态
            newState = initialState(s)


        elif newState.state == "Id":
            if s.isdigit() or s.isalpha():
                #继续添加该字符到临时token里
                tempToken += s
            else:
                #退出Id状态，保存token
                newState = initialState(s)


        elif newState.state == "Int":
            if s.isdigit():
                tempToken += s
            else:
                # 退出Id状态，保存token
                newState = initialState(s)

        elif newState.state == "GT":
            #如果后面遇到了=，则需要将类型改为GE
            if s == "=":
                newState = State("GE")
                token.type = newState.state
                tempToken += s
            else:
                newState = initialState(s)

        elif newState.state == "GE":
            newState = initialState(s)

        #将最后一个tempToken加入到tokens中

    if len(tempToken) > 0 :
        token.text = tempToken
        tokens.append(token)

        # 生成新的tempToken和token
        tempToken = ""
        token = Token()





if __name__ == "__main__":
    tokenize("age >= 100")
    for token in tokens:
        print(token.type,token.text)

















