from faker import Faker
from mondrian_art import generate


fake = Faker()

for i in range(20):
    print(fake.name())



plt = generate()
plt.show()
