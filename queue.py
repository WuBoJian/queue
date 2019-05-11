# coding:utf-8


class Queue(object):
    """队列"""
    def __init__(self):
        self.__queue = []

    def enqueue(self, item):
        '''往队列中添加元素'''
        self.__queue.append(item)

    def get_item(self):
        '''从队列中取元素'''
        return self.__queue.pop(0)

    def is_empty(self):
        '''判断是否为空'''
        return not self.__queue

    def length(self):
        '''队列大小'''
        return len(self.__queue)

if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(8)
    print(q.get_item())
    print(q.is_empty())
    print(q.length())