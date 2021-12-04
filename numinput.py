import random
import time

import pyinputplus as pyip


def addsUptoTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
        if sum(numbersList) != 10:
            raise Exception('The digits must add up to 10,not %s' %(sum(numbersList)))
        return int(numbers)
# input 10
# response = pyip.inputCustom(addsUptoTen)

# input = 4
# num = pyip.inputNum('Enter num:',min=4)

#break
# notempty = pyip.inputNum('Enter num:')
# empty = pyip.inputNum(blank=True)

# limit
# limit = pyip.inputNum(limit=2)
#
# timeout = pyip.inputNum(timeout=10)

#Regexes
# text = pyip.inputNum(allowRegexes=[r'i|ι|ρ|θ', r'zero'])

numberOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numberOfQuestions):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
    except pyip.TimeoutException:
        print('Out of time')
    except pyip.RetryLimitException:
        print('Out of tries')
    else:
        print('Correct!')
        correctAnswers += 1
    time.sleep(1)
print('Score: %s / %s ' % (correctAnswers, numberOfQuestions))