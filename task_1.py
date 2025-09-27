class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ") 
            current = current.next
        print("None") 

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sorted_merge_nodes(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge_nodes(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge_nodes(a, b.next)

        return result    
    def merge_sort_nodes(self, h):
        if not h or not h.next:
            return h
        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_nodes(h)
        right = self.merge_sort_nodes(next_to_middle)

        sorted_list = self.sorted_merge_nodes(left, right)
        return sorted_list


    # def sorted_merge(self, other):
    #     dummy = Node(0)
    #     tail = dummy
    #     a, b = self.head, other.head

    #     while a and b:
    #         if a.data <= b.data:
    #             tail.next = aa = a. next
    #         else:
    #             tail.next = b
    #             b = b.next
    #             tail = tail.next

    #         tail.next = a if a else b

    #         merged =LinkedList()
    #         merged.head = dummy.next
    #         return merged

    def merge_sort(self):
        self.head = self.merge_sort_nodes(self.head)

        # if not self.head or not self.head.next:
        #     return self
        
        # middle = self.get_middle()
        # next_to_middle = middle.next
        # middle.next = None

        # left = LinkedList()
        # left.head = self.head

        # right = LinkedList()
        # right.head = next_to_middle

        # left = left.merge_sort()
        # right = right.merge_sort()

        # return left.sorted_merge(right)
    
    def get_middle(self, head):
        if not head:
            return head
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow 
    
    def merge_two_sorted(self, other):
        merged = LinkedList()
        merged.head = self.sorted_merge_nodes(self.head, other.head)
        return merged

if __name__ == "__main__":
    ll = LinkedList()
    for val in [4, 2, 5, 1, 3, 7]:
        ll.append(val)

    print("Initial list:")
    ll.print_list()

    ll.reverse()
    print("After reverse:")
    ll.print_list()

    ll.merge_sort()
    print("Sorted list:")
    ll.print_list()

    ll_two = LinkedList()
    for val in [0, 6, 7, 9]:
        ll_two.append(val)

    ll_two.merge_sort()
    print("Second sorted list:")
    ll_two.print_list()

    merged = ll.merge_two_sorted(ll_two)
    print("Merged sorted list:")
    merged.print_list()   