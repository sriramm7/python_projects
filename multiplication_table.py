for i in range(1, 11):  # Numbers 1 through 10
    print(f"\nMultiplication Table for {i}:")
    print("-" * 30)
    for j in range(1, 21):  # Multiples 1 through 20
        result = i * j
        print(f"{i} x {j:2} = {result}")