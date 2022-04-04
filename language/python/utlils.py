
# 合并两个json对象
def merge_json(t0: {}, t1: {}) -> {}:
    return {i: j for x in [t0, t1] for i, j in x.items()}

