import queue

class BFS(object):
    def __init__(self,start_word,end_word):
        self.start = start_word # 开始单词
        self.end = end_word     # 结束单词
        self.current_queue = queue.Queue()  # 当前扩展要拿出来的node队列
        self.next_queue = queue.Queue()     # current队列扩展到的新node加入该队列
        self.found = False                  # 控制循环是否结束
        self.level = 0                      # 广度搜索的层数
        self.visited = set()                # 已访问的节点
        self.node_detail = {}               # 节点的步数、前驱
        self.node_change_logger = []        # 打印变化路径时用到的临时list

    def state_is_target(self,word):
        return word == self.end

    def state_extend(self,word):
        extend_result = set()
        for i in range(len(word)):
            for j in range(ord('a'),ord('z')+1):
                c = chr(j)
                if word[i]==c:
                    continue
                new_word = word[0:i]+c+word[i+1::]
                if new_word not in self.visited:
                    self.node_detail[new_word] = {'change_count':self.level+1,'pre_node':word}
                    extend_result.add(new_word)
                    self.visited.add(new_word)
        return extend_result

    def ladderLength(self):
        self.current_queue.put(self.start)
        self.visited.add(self.start)
        while not self.current_queue.empty() and not self.found:
            self.level += 1
            while not self.current_queue.empty() and not self.found:
                word = self.current_queue.get()
                new_states = self.state_extend(word)
                for state in new_states:
                    self.next_queue.put(state)
                    if self.state_is_target(state):
                        self.found = True
                        break
            self.next_queue,self.current_queue = self.current_queue,self.next_queue
        if self.found:
            self.node_change_search(self.end)
            print('-->'.join(self.node_change_logger[::-1]+[self.end]))
            return self.level +1
        else:
            return 0

    def node_change_search(self,word):
        if self.node_detail.get(word,None) is not None:
            pre_word = self.node_detail[word]['pre_node']
            self.node_change_logger.append(pre_word)
            self.node_change_search(pre_word)


topology = BFS('hity','coge')
print(topology.ladderLength())
