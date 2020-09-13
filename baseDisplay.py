class baseDisplay:
    def __init__(self):
        self.bases=['O','O','O']

    def update(self, newBases):
        for x in range(3):
            self.bases[x] = 'x' if newBases[x] else 'O'
        self.render()
    def render(self):
        print("     " + self.bases[1])
        print("    / \\")
        print("   /   \\")
        print("  /     \\")
        print(" /       \\")
        print(self.bases[2] + "         " + self.bases[0])
        print(" \\       /")
        print("  \\     /")
        print("   \   /")
        print("    \\ /")
        print("     O")
