import math
import random
import hashlib


class Node:
    def __init__(self, item):
        self.item = item
        self.childl = None
        self.childr = None
        self.hash = None
        self.data = None

    def change_data(self, data):
        self.data = data
        self.hash = hashlib.md5(data.encode('utf-8')).hexdigest()[
                    8:-8]  # hexdigest()返回摘要，作为十六进制数据字符串值 [8:-8]将32位MD5转换为16进制
        #print("make_hash", self.hash, "size", len(self.hash), end=" ")
        return self.hash

class Tree:
    def __init__(self):
        self.root = None
    def add(self, item):  # 逐层添加子节点
        node = Node(item)
        end_str = make_data(item)
        if end_str != None and end_str != -1:
            node.change_data(end_str)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]
            while True:
                pop_node = q.pop(0)
                if pop_node.childl is None:
                    pop_node.childl = node
                    return
                elif pop_node.childr is None:
                    pop_node.childr = node
                    return
                else:
                    q.append(pop_node.childl)
                    q.append(pop_node.childr)

    def reload_hash(self):  # 层次遍历更新hash
        if self.root is None:
            return None
        q = [self.root]
        item = [(self.root.item, self.root.data, self.root.hash)]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.childl and pop_node.childr:
                if pop_node.childl.hash and pop_node.childr.hash:
                    end_str = pop_node.childl.hash + pop_node.childr.hash
                    end_hash = pop_node.change_data(end_str)

            if pop_node.childl is not None:
                q.append(pop_node.childl)

            if pop_node.childr is not None:
                q.append(pop_node.childr)
        return

    def traverse(self):  # 层次遍历
        q = [self.root]
        item = [(self.root.item, self.root.data, self.root.hash)]
        while q != []:
            pop_node = q.pop(0)
            if pop_node.childl is not None:
                q.append(pop_node.childl)
                item.append((pop_node.childl.item, pop_node.childl.data, pop_node.childl.hash))

            if pop_node.childr is not None:
                q.append(pop_node.childr)
                item.append((pop_node.childr.item, pop_node.childr.data, pop_node.childr.hash))

        return (item)


def make_data(i):
    if i > 6 and i < 15:
        raw_str = "caoshuhe1122334455"
        nums = math.floor(1e5 * random.random())
        nums = str(nums)
        nums = nums.zfill(5)
        end_str = raw_str + nums
        return end_str
    elif i >= 0 and i < 7:
        return None
    else:
        return -1

if __name__ == '__main__':
    t = Tree()
    for i in range(7):  # 基础节点
        t.add(i)

    for i in range(7, 15):  # 带数据的节点
        t.add(i)

print('前序遍历:\n节点名:数据：hash值', t.traverse())
