import numpy as np

def bits_to_int(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def bitfield_n(n, gridsize):
    bits = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
    bits = np.append(np.zeros(gridsize**2-len(bits)), bits)
    return np.asarray(bits, dtype=int).reshape(gridsize,gridsize)

def bitfield(n):
    bits = [1 if digit=='1' else 0 for digit in bin(n)[2:]]
    bits = np.append(np.zeros(9-len(bits)), bits)
    return np.asarray(bits, dtype=int).reshape(3,3)

def generate(gridsize, alive_percentage = .5):
    GRID = np.random.randint(10, size=(gridsize,gridsize), dtype=int)
    GRID = np.multiply(GRID >= (1-alive_percentage) * 10, np.ones((gridsize, gridsize)))
    return GRID.astype(dtype=int)

def life_step_standard_rules(bf):
    nbrs_count = np.sum(np.roll(np.roll(bf, i, 0), j, 1)
                     for i in (-1, 0, 1) for j in (-1, 0, 1)
                     if (i != 0 or j != 0))
    return ((nbrs_count == 3) | (bf & (nbrs_count == 2)))
