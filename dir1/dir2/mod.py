print('in mod.py')
z = 3


'''
>>> import dir1.dir2.mod
dir1 init
dir2 init
in mod.py
>>> 
>>> import dir1.dir2.mod
>>> 
>>> reload(dir1)
dir1 init
<module 'dir1' from 'D:\\prog\\Lutz_1\\dir1\\__init__.py'>
>>> reload(dir1.dir2)
dir2 init
<module 'dir1.dir2' from 'D:\\prog\\Lutz_1\\dir1\\dir2\\__init__.py'>
>>> 
>>> dir1.x
1
>>> 
>>> dir1.dir2.y
2
>>> dir1.dir2.mod.z
3
>>> 
'''