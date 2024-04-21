def line():
    print('—'*40)


# >>> line
# <function line at 0x00000224428C8A40>
# >>>
# >>> type(line)
# <class 'function'>
# >>>
# >>> line.__name__
# 'line'
# >>>
# >>> line.__doc__
# >>>
# >>> line()
# ————————————————————————————————————————
# >>>
# >>> other = line
# >>> other
# <function line at 0x00000224428C8A40>
# >>>
# >>> type(other)
# <class 'function'>
# >>>
# >>> other.__name__
# 'line'
# >>>
# >>> other()
# ————————————————————————————————————————
# >>>
# >>> del line
# >>> line
# NameError: name 'line' is not defined. Did you mean: 'slice'?
# >>>
# >>> other()
# ————————————————————————————————————————

