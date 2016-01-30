__author__ = 'aneta_ochedowska'
from threading import Thread


class Server(Thread):
    def __init__(self, input_queue,
                 output_queue,
                 p,
                 passwords,
                 polynomial,
                 keys):
        Thread.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        # p - wedlug zalozen zadania ten argument ma poprawna wartosc
        self.p = p
        self.passwords = passwords
        self.polynomial = polynomial
        self.keys = polynomial
        self.successfully_finished = None

    def run(self):
        try:
            while self.input_queue.get() != "theend":
                self.successfully_finished = True
            return
        except:
            self.successfully_finished = False
            self.output_queue.put("ERROR")

    def finish(self):
        self.input_queue.put("theend")
