def generate_data():
    for i in range(10):
        yield i

# Using the generator
data_generator = generate_data()

# Iterating over the generated data
for value in data_generator:
    print(value)
