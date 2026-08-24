import math

print("Anna ympyrän säde niin lasken sen pinta-alan kahden desimailin tarkkuudella!")
r=float(input())

P= r * r
A= P * math.pi

print("Ympyrän pinta-ala on:")
print(round(A, 2))