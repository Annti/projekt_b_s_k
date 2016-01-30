__author__ = 'aneta_ochedowska'
from threading import Thread
from Utils import *
import hashlib


class Client(Thread):
    def __init__(self, server_input_queue,
                 server_output_queue,
                 name,
                 h_0,
                 K,
                 key,
                 secret):
        Thread.__init__(self)
        self.server_input_queue = server_input_queue
        self.server_output_queue = server_output_queue
        # identyfikator klienta
        self.name = name
        # sekret zerowy h_0
        self.h_0 = h_0
        # indeks poczatkowo 1
        self.i = 1
        # ograniczenie K
        self.K = K
        # punkt P ktory jest punktem nalezacym do wielomianu
        # znanego serwerowi
        self.P = None
        self.key = key
        self.secret = secret
        self.successfully_finished = None

    def run(self):
        try:
            new_h_0 = self.h_0
            for x in range(self.K - self.i):
                # print x
                m = hashlib.md5(new_h_0).hexdigest()
                # print m
                new_h_0 = m
                # print new_h_0

            code = Cipher(self.key)
            # klient tworzy parametr M
            M = str(self.name) + ":" + str(self.i) + ":" + str(new_h_0)
            # encM = code.encrypt(M)

            # tuple_to_server = (self.name, encM)
            # self.server_output_queue.put(tuple_to_server)

            # klient tworzy parametr M
            # M = str(self.name) + ":" + str(self.i) + ":" + str(new_h_0)

            self.successfully_finished = True
            return
        except:
            self.successfully_finished = False
            self.server_output_queue.put('ERROR')
