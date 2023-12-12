class Answer:
    def __init__(self, answer):
        self.answer = answer

    def __str__(self):
        return f"The Definitive Answer to what is the Meaning of the universe is... 42"


class Supercomputer(Answer):
    def __init__(self, answer, rank):
        super().__init__(answer)
        self.rank = rank

    def __str__(self):
        return f"{self.name} is the {self.rank} ranked computer in the galaxy!"
    
deepthought = Supercomputer("Deep Thought", 1)
print(deepthought)