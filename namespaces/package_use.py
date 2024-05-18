import package

user_objects = {
    k: v 
    for k, v in package.__dict__.items() 
    if not k.startswith('_')
}
print(*user_objects.items(), sep='\n')

# ('subpackage', <module 'package.subpackage' from '...\\package\\subpackage\\__init__.py'>)
# ('p_module1', <module 'package.p_module1' from '...\\package\\p_module1.py'>)
# ('main_func', <function main_func at 0x00000249945C22A0>)
# ('sp_module1', <module 'package.subpackage.sp_module1' from '...\\package\\subpackage\\sp_module1.py'>)
# ('var1', 267)
# ('var3', False)

# >>> package
# <module 'package' from '...\\package\\__init__.py'>
# >>>
# >>> type(package)
# <class 'module'>

# >>> package.__package__
# 'package'
# >>>
# >>> package.p_module1.__package__
# 'package'
# >>>
# >>> package.subpackage.__package__
# 'package.subpackage'
# >>>
# >>> package.subpackage.sp_module1.__package__
# 'package.subpackage'

