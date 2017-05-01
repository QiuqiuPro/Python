# 線形代数

# 4.1
# ベクトル
# Pythonのリストはベクトルではないため演算できない。作ってみよう。
def vector_add(v,w):
    ''' v1([1,2])+v2([2,1])=v3([1+2,2+1]) '''
    return [v_i + w_i for v_i, w_i in zip(v,w)]

def vector_substract(v,w):
    ''' v1([1,2])-v2([2,1])=v3([1-2,2-1]) '''
    return [v_i - w_i for v_i, w_i in zip(v,w)]

def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(vector, result)
    return result
