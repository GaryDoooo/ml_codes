import pickle
import bz2

with bz2.BZ2File("data/AAPL.p.bz2") as pfile_handle:
    df = pickle.load(pfile_handle)

print df.head(20)
