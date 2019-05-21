from .color_utils import to_hex, to_sint


def to_string(contents_dict):
    result = ""
    for k, v in contents_dict.items():
        result += "{}={}\n".format(k, v)
    return result


def to_dict(contents):
    result_dict = {}
    pairs = contents.split('\n')
    for pair in pairs:
        if pair != '':
            kvpair = pair.split('=')
            result_dict[kvpair[0]] = kvpair[1]
    return result_dict


def transform_dict(contents_dict, fn):
    result = {}
    for k, v in contents_dict.items():
        result[k] = fn(v)
    return result


def to_human_readable(contents_dict):
    return transform_dict(
        contents_dict,
        lambda x: to_hex(int(x))
    )


def to_telegram_readable(contents_dict):
    return transform_dict(
        contents_dict,
        lambda x: to_sint(x)
    )


def hstr_to_tgstr(contents):
    return to_string(to_telegram_readable(to_dict(contents)))


def tgstr_to_hstr(contents):
    return to_string(to_human_readable(to_dict(contents)))


def hdict_to_tgdict(cdict):
    return to_dict(hstr_to_tgstr(to_string(cdict)))


def tgdict_to_hdict(cdict):
    return to_dict(tgstr_to_hstr(to_string(cdict)))
