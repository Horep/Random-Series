import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
# Number of terms to add
n = 10**2
# Define the random variables t_n
t_n = np.random.uniform(0, 1, n)
# Put the random variables into the exponential
weights = np.exp(2*np.pi*1j*t_n)
# Produce list (1,2,3,...,n)
integer_list = np.arange(1, n+1)
# Produce list (1,1/2,1/3,...,1/n)
s = 2
recip = 1/(integer_list**s)
# Multiply each 1/n by exp(2 pi i t_n)
terms = weights*recip
sum_seq = []
# Add up terms of the sequence
for m in range(1, n+1):
    sum_seq.append(np.sum(terms[0:m]))
# Define an iterator i
i = 1
# Plot the sum sequence points, scaled down further down the sequence
for z in sum_seq:
    ax.plot(np.real(z), np.imag(z), 'bo', markersize=2*i**(-1/2))
    i += 1
# Split the sum sequence into real and imaginary parts
real_val = np.real(sum_seq)
imag_val = np.imag(sum_seq)
# ax.plot(real_val, imag_val)
# Plot "limit"
ax.plot(real_val[n-1], imag_val[n-1], 'rx')
# Draw arrows between points
arrow_width = 0.00001
ax.arrow(0, 0, real_val[0], imag_val[0],
         length_includes_head=True, width=arrow_width)
for m in range(0, n-1):
    ax.arrow(real_val[m], imag_val[m],
             real_val[m+1] - real_val[m],
             imag_val[m+1] - imag_val[m],
             width=arrow_width,
             length_includes_head=True)
plt.grid()
fig.savefig("Complex_Random_Harmonic_Series3.pdf")
