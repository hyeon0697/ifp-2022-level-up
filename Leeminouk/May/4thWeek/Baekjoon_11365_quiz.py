# 당신은 길을 가다가 이상한 쪽지를 발견했다. 그 쪽지에는 암호가 적혀 있었는데, 똑똑한 당신은 암호가 뒤집으면 해독된다는 것을 발견했다.

# 이 암호를 해독하는 프로그램을 작성하시오.

# 입력
# 한 줄에 하나의 암호가 주어진다. 암호의 길이는 500을 넘지 않는다.

# 마지막 줄에는 "END"가 주어진다. (END는 해독하지 않는다.)

# 출력
# 각 암호가 해독된 것을 한 줄에 하나씩 출력한다

import sys
input = sys.stdin.readline

END = "END\n"
text = ""

while True:
    text = input()
    
    if text == END:
        break

    text = list(reversed(list(text)))
    text.pop(0)

    print("".join(text))