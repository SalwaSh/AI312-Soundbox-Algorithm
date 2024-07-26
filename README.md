# Soundbox-Algorithm

The Soundex algorithm is a method commonly used in libraries and older census records for representing people’s names. (e.g., Example-1: Jurafsky, Jarofsky, Jarovsky, and Jarovski all map to J612; Example-2: Einstein E523, Example-3: Alex A420).

1. Keep the first letter of the name, and drop all occurrences of non-initial a, e, h, i, o, u, w, y.
  a. (J) (E) (A)
2. Replace the remaining letters with the following numbers:
  a. b, f, p, v → 1; c, g, j, k, q, s, x, z → 2; d, t → 3; l → 4; m, n → 5; R → 6
  b. (J6122) (E5235) (A42)
3. Replace any sequences of identical numbers, only if they derive from two or more letters that were adjacent in the original name, with a single number (e.g., 666 → 6).
  a. (J612) (E5235) (A42)
4. Convert to the form Letter Digit Digit Digit by dropping digits past the third (if necessary) or padding with trailing zeros (if necessary). 
  a. (J612) (E523) (A420)

The exercise: write an (Finite State Transducers) FST to implement the Soundex algorithm.
