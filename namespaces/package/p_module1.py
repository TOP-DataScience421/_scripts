"""
Управляющий модуль.
"""

import package.subpackage.sp_module1 as sp


def main_func():
    return '-'.join(map(str, aux_func()))


def aux_func():
    return sorted(sp.var4, reverse=True)

