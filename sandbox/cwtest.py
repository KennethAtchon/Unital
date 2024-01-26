from pycrossword import Crossword

crossword = Crossword(width=15, height=15)
crossword.add_word("python", 1, 1, "horizontal")
crossword.add_word("javascript", 5, 3, "vertical")
crossword.generate()
crossword.display()
# or
crossword.save("my_crossword.png")
