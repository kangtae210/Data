# 자료구조 Stack

#1. 개요
# - 후입선출의 자료구조이다.
# - 입력연산을 push, 출력연산을 pop이라고 한다.
# - 탑 포인터(메모리 말단)가 가리키는 데이터를 조회하는 peek 메서드가 있다.
#     탑의 인덱스는 변화시키지 않는다.
#  - pop은 출력한 후 데이터를 삭제하지만, peek은 삭제하지 않는다.

class Stack:
    my_stack = []
    
    def pop(self):
        if self.isEmpty():
            print("스택이 비어있음")
        else:
            print("스택의 마지막 원소는 =>", self.my_stack[-1])
            del self.my_stack[-1]
            print("pop되었습니다.")



    def push(self, item):
        self.my_stack.append(item)

    def peek(self):
        if self.isEmpty():
            print("스택이 비어있음")
        else:
            print("스택의 마지막 원소는 =>", self.my_stack[-1])

    def isEmpty(self):
        if len(self.my_stack) == 0:
            return True
        else :
            return False

class Manager:
    def manage(self):
        my_stack = Stack()
        while True:
            print("***************")
            print("1. pop")
            print("2. push")
            print("3. peek")
            print("4. STOP")
            answer = int(input("선택하세요=>"))
            print("***************")

            if answer == 1:
                my_stack.pop()
            elif answer == 2:
                item = input("추가할 데이터=>")
                my_stack.push(item)
            elif answer == 3:
                my_stack.peek()
            elif answer == 4:
                break
        print("종료되었습니다.")
        print("*********************")
        


man = Manager()
man.manage()