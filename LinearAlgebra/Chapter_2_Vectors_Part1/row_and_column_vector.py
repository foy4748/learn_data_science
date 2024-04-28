import numpy as np

# --------------------------------------------------
# CREATING AND VISUALIZING VECTOR USING NUMPY
# --------------------------------------------------

## Reliable Ways

# Example of Row vector 
row_vector = np.array([ [1,2,3,4,5] ])

# Each array within an array represents a different row

# Example of Column vector 
col_vector = np.array(
    [
        [1],
        [2],
        [3],
        [4],
        [5]
    ]
)

# Not because it is written like a column. 
# Because each array within an array represents different row
# In a column vector. Each element remains at different rows. 

# Sometimes Orientation of Vector (either column or row) really matters.
# These are the safest way to handle orientation of a vector

# Dimensions are always listed as (rows,columns).

print(f"shape of row vector: {np.shape(row_vector)}")
print(f"shape of column vector: {np.shape(col_vector)}")

# You may think that a vector encodes a geometric coordinate, 
# but vectors and coordinates are actually different things. 
# They are, however, concordant when the vector starts at the origin. 
# This is called the standard position

# --------------------------------------------------
# Operations on Vectors
# --------------------------------------------------
