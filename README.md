# Soundbox-Algorithm 📦📚

The Soundex algorithm is a method commonly used in libraries and older census records for representing people’s names. (e.g., Example-1: Jurafsky, Jarofsky, Jarovsky, and Jarovski all map to J612; Example-2: Einstein E523, Example-3: Alex A420).

1. Keep the first letter of the name, and drop all occurrences of non-initial a, e, h, i, o, u, w, y.
   ```
    J) (E) (A)
   ```
3. Replace the remaining letters with the following numbers:
   - a, b, f, p, v → 1
   - c, g, j, k, q, s, x, z → 2
   - d, t → 3;  l → 4
   - m,  n → 5
   - R → 6
   ```
   (J6122) (E5235) (A42)
   ```
5. Replace any sequences of identical numbers, only if they derive from two or more letters that were adjacent in the original name, with a single number (e.g., 666 → 6).
   ```
   (J612) (E5235) (A42)
   ```
6. Convert to the form Letter Digit Digit Digit by dropping digits past the third (if necessary) or padding with trailing zeros (if necessary). 
   ```
   (J612) (E523) (A420)
   ```

## Screenshots 📷

![image](https://github.com/user-attachments/assets/0a7fe8a3-4a0b-428b-8c39-97f0c7a0f4bb)


## How to Run ⚙️
1. Clone the repository.
```
git clone https://github.com/SalwaSh/AI312-Soundbox-Algorithm.git
```
2. Run soundex.py file.
```
python soundex.py
```


## Contributor ✍️
- Salwa Shamma
