#!/usr/bin/python
# -*- coding: utf-8 -*-


class a:

    var1 = 'adsasd'
    var2 = 342

    def const(self):
        print (self.var1, self.var2)

    @staticmethod
    def addBook():
      print ('this si address')

obj1a=a()
obj1a.const();
obj1a.addBook()
