# 单核与多核的区别
#理论上讲多核的计算机可以同时运行多个进程
import threading

def worker():
    print("I'm a threading")
    t = threading.current_thread()
    import time
    time.sleep(5)
    print(t.getName())
    t.setName("big girl thread")
    print(t.getName())

new_t = threading.Thread(target=worker)
new_t.start()

t = threading.current_thread()
print(t.getName())
'''
更加充分的利用CPU的资源， 也是一种异步编程
python 的GIL global interpreter lock 全局解释器锁 ，无论几核，同一时间只能运行一个线程
锁分为细粒度锁，和粗粒度锁 解释器上加了全局锁，一定程度上保证线程的安全 GIL是以bytecode为单位来加锁的
python只是一种语言规范， 关键是解释器， python解释器有两种 cpython, jpython, GIL是基于cpython里的，Jpython里并没有
python多线程到底是不是鸡肋？
程序分为 CPU密集型程序：大量使用CPU来计算 IO密集型程序：查询数据库，请求网络资源，读写文件， 主要的时间都在等待，这种时候就可以换成别的线程来运行
 '''
