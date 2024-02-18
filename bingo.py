import random
from datetime import datetime

class bingo:
    def __init__(self):
        pass

    def generate_unique_numbers(self,n):
        numbers = list(range(1, 76))
        random.shuffle(numbers)
        return numbers[:n]
    
    def create_bingo_content(self):
        content = ["| B | I | N | G | O |"]
        content.append("| --- | --- | --- | --- | --- |")

        numbers = self.generate_unique_numbers(24)
        numbers.insert(12,"FREE")

        for i in range(5):
            start = i*5
            end = start +5
            content.append(f"|{' | '.join([str(n) for n in numbers[start:end]])} |")
        return content

    def create_bingo_md(self,n):
        for i in range(n):
            timestamp = datetime.now().strftime("%Y-%m-%d %H%M%S")

            with open(f"bingo_{timestamp}.md","w") as f:
                f.write("\n".join(self.create_bingo_content()))

    def get_next_bingo():
        return random.randint(1,75)