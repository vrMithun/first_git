T = True
F = False
not_raining_or_umbrella = T  # ¬R ∨ U
not_umbrella_or_not_wet = T  # ¬U ∨ ¬W
raining_or_not_wet = T       # R ∨ ¬W
grumpy_implies_wet = T       # G → W

for R in [T, F]:
    for U in [T, F]:
        for W in [T, F]:
            for G in [T, F]:
                premise1 = (not R or U)
                premise2 = (not U or not W)
                premise3 = (R or not W)
                premise4 = (not G or W)

                if premise1 and premise2 and premise3 and premise4:
                    if G and not W:
                        print("Contradiction found with: ")
                        print(f"R: {R}, U: {U}, W: {W}, G: {G}")
                        print(f"¬R ∨ U: {premise1}, ¬U ∨ ¬W: {premise2}, R ∨ ¬W: {premise3}, G → W: {premise4}\n")
                        continue

                    if G and W:
                        print("Contradiction found with: ")
                        print(f"R: {R}, U: {U}, W: {W}, G: {G}")
                        print(f"¬R ∨ U: {premise1}, ¬U ∨ ¬W: {premise2}, R ∨ ¬W: {premise3}, G → W: {premise4}\n")
                        continue
    
                    if not G:
                        print("Conclusion derived: Kate is not grumpy.")
                        print(f"R: {R}, U: {U}, W: {W}, G: {G}")
                        print(f"¬R ∨ U: {premise1}, ¬U ∨ ¬W: {premise2}, R ∨ ¬W: {premise3}, G → W: {premise4}\n")
