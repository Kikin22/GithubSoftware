from threading import Thread
from random import randint
from time import sleep

class Producer(Thread):
    """
	Appends integers to a queue.
	"""
    def __init__(self, t, q, a, b, p):
        """
        Thread t to add integers in [a,b] to q, sleeping between 1 and p seconds.
        """
        Thread.__init__(self, name=t)
        self.queue = q
        self.begin = a
        self.end = b
        self.pace = p 
        
    def run(self):
        """
		produces integers at some pace.
		"""
        print (self.getName() + " starts...")
        for i in range(self.begin, self.end+1):
            rnd = randint(1, self.pace)
            print (self.getName() + \
				"sleeps %d seconds" % rnd)
            sleep(rnd)
            print ("appending %d to queue" % i)
            self.queue.append(i)
        print ("production terminated")
		
def main():
	"""
	creates a producer object.
	"""
	que = []
	prd = Producer('producer', que, 3, 9, 10)
	prd.start()
	prd.join()
if __name__=="__main__":
	main()

		