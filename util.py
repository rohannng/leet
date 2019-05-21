class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list(lst):
    if not lst:
        return ListNode("")
    head = ListNode(lst[0])
    tail = head
    for n in lst[1:]:
        tail.next = ListNode(n)
        tail = tail.next
    return head


def print_list(lst):
    while lst is not None:
        print(lst.val)
        lst = lst.next


def arr_list(lst):
    ret = []
    while lst is not None:
        ret.append(lst.val)
        lst = lst.next
    return ret
