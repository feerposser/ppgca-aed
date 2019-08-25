class Obj:
    content = int
    next = ""
    def __init__(self, content):
        self.content = content

def push(simple_list, content):
    obj = Obj(content)
    simple_list[len(simple_list)-2].next = obj
    obj.next = simple_list[len(simple_list)-1]
    simple_list.insert(len(simple_list)-1, obj)
    print("\nPUSH")
    for i in simple_list:
        print('\tConteúdo', i.content, "Próximo:", i.next.content)
    return simple_list

def pop(simple_list, content):
    for i in range(0, len(simple_list)-1):
        if simple_list[i].content == content:
            simple_list[i-1].next = simple_list[i+1]
            simple_list.pop(i)
    print("\nPOP")
    for i in simple_list:
        print('\tConteúdo', i.content, "Próximo:", i.next.content)
    return simple_list

tail = Obj("Tail")
head = Obj("Head")
tail.next = head
head.next = tail

simple_list = [tail, head]

simple_list = push(simple_list, 1)

simple_list = push(simple_list, 2)

simple_list = push(simple_list, 3)

simple_list = pop(simple_list, 1)

simple_list = pop(simple_list, 3)
