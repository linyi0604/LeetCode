"""
编写一个程序，找到两个单链表相交的起始节点。



例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。



注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


#
# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         # 如果有一个链表是空的 那就没有交叉
#         if headA is None or headB is None:
#             return None
#         # 计算一下两个链表的长度
#         ca = headA
#         cb = headB
#         ta, tb = 1, 1
#         while ca.next is not None:
#             ta += 1
#             ca = ca.next
#         while cb.next is not None:
#             tb += 1
#             cb = cb.next
#         # 如果最后一个元素都不一样说明没有交叉
#         if ca.val != cb.val:
#             return None
#         # 如果两个链表长度不一样，将长得链表指针后移
#         ca = headA
#         cb = headB
#         while tb > ta:
#             tb -= 1
#             cb = cb.next
#         while ta > tb:
#             ta -= 1
#             ca = ca.next
#         # 从倒数长度相同的 短的链表的开头开始一位一位比较
#         while ca is not None and cb is not None:
#             if ca.val == cb.val:
#                 return ca
#             ca = ca.next
#             cb = cb.next


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 建立一个哈希表，把每个第一次遍历到的元素存进去
        # 如果发现之前存过当前元素说明交叉了
        dic = {}
        ca = headA
        cb = headB
        while ca is not None or cb is not None:
            if ca is not None:
                try:
                    dic[ca.val]
                    return ca
                except:
                    dic[ca.val] = True
                    ca = ca.next
            if cb is not None:
                try:
                    dic[cb.val]
                    return cb
                except:
                    dic[cb.val] = True
                    cb = cb.next
        return None

