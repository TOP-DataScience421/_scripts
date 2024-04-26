def track_info(
        *,
        title: str,
        artist: str,
        album: str,
        channels: int, 
        bit_depth: int, 
        sample_rate: int, 
):
    ...


# >>> track_info(
# ...     'Boom',
# ...     'Boomers',
# ...     'BOOM!',
# ...     6,
# ...     8,
# ...     48000
# ... )
# TypeError: track_info() takes 0 positional arguments but 6 were given

# >>> track_info(
# ...     title='Boom',
# ...     artist='Boomers',
# ...     album='BOOM!',
# ...     channels=6,
# ...     bit_depth=8,
# ...     sample_rate=48000
# ... )
# >>>


def func_general1(pos, /, pos_key1, *, key1, key2=False):
    ...


def func_general2(pos, *pos_args, key, **key_args):
    ...

