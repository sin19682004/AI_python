
import imp

foo = imp.load_source('A', 'B/a.py')
#foo.A()


a=foo.A()
a.P(6)




