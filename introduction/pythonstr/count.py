# coding:utf-8

info = '''
    Python now uses the same ABI whether it’s built in release or debug mode. 
    On Unix, when Python is built in debug mode, it is now possible to load C 
    extensions built in release mode and C extensions built using the stable 
    ABI.

    Release builds and debug builds are now ABI compatible: 
    defining the Py_DEBUG macro no longer implies the Py_TRACE_REFS macro, 
    which introduces the only ABI incompatibility. The Py_TRACE_REFS macro, 
    which adds the sys.getobjects() function and the PYTHONDUMPREFS 
    environment variable, can be set using the new 
    ./configure --with-trace-refs build option. 
    (Contributed by Victor Stinner in bpo-36465.)
'''

a = info.count('a')
b = info.count('b')
c = info.count('c')
d = info.count('d')
e = info.count('e')
f = info.count('f')

print(a, b, c, d, e, f)
number_list = [a, b, c, d, e, f]
print(number_list)
print('在列表中，最大的数值：', max(number_list))


number_dict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f
}
print('每个成员对应的数值分别是：', number_dict)
