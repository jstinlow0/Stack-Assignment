from PostFix_Calculator import postfix
from StackedLinkedList import Stack

def test_postFix1():
    calcStack = Stack()
    testList = ["3","4","+"]
    testResult = postfix(testList, calcStack)
    assert testResult == 7

def test_postFix2():
    calcStack = Stack()
    testList = ["2", "3", "1", "*", "+", "9", "-"]
    testResult = postfix(testList, calcStack)
    assert testResult == -4

def test_postFix3():
    calcStack = Stack()
    testList = ["2", "3", "^", "5", "%", "4", "-"]
    testResult = postfix(testList, calcStack)
    assert testResult == -1.0

def test_postFix4():
    calcStack = Stack()
    testList = ["3", "2", "^", "2", "/"]
    testResult = postfix(testList, calcStack)
    assert testResult == 4.5

