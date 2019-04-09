import queue
queue_count = int(input())
queue_list = queue.Queue()
for i in range(queue_count) :
    n=input().split()
    if(n[0] == "push") :
        queue_list.put(n[1])
    elif(n[0] == "pop") :
        if(queue_list.qsize() == 0) :
            print(-1)
        else :
            print(queue_list.get())
    elif(n[0] == "size") :
        print(queue_list.qsize())
    elif(n[0] == "empty") :
        if(queue_list.qsize() == 0) :
            print(1)
        else :
            print(0)
    elif(n[0] == "front") :
        if(queue_list.qsize() == 0) :
            print(-1)
        else :
            print(queue_list.queue[0])
    elif(n[0] == "back") :
        if(queue_list.qsize() == 0) :
            print(-1)
        else :
            print(queue_list.queue[-1])
        
