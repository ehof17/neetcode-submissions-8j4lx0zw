from collections import Counter, deque

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # every step
        # what CAN we do
        # after we do everything we can do, then wait
        # This wont work
        # AAAAAAAAAB
        # Could do 
        # Start with the one we have most of
        # then do them in decreasing frequesncy
        hm = Counter(tasks)
        neg = [-v for k,v in hm.items()]
        heapq.heapify(neg)
        print(neg)
        sorted_items = hm.most_common()
        queue = deque()
        time = 0
        while neg or queue:
            time+=1
            if neg:
                v = heapq.heappop(neg)
                v = v+1
                if v < 0:
                    queue.append((v, time+n))
            if queue:
                while queue and queue[0][1] == time:
                    pv, pt = queue.popleft()
                    heapq.heappush(neg, pv)


        return time
        # place the value in the queue
        # when it is ready we can pop it off
        # 
        # heap
        # process everything on the heap at least once
        # heap
        # popped_timer = {}
        # j,v = heapq.pop()
        # res+=1
        # popped_timer[j] = n
        # for k, in popped_timer.keys():
        # popped_timer[k]-=1

        # add it back after tho
        # dont want to process the same thing on the same row
        # i guess we can if the time allows
        # heapq.heappush(j,v-1)



            