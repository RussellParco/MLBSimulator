class baseDisplay:
    def __init__(self):
        self.bases=['o','o','o']

    def update(self, newBases):
        for x in range(3):
            self.bases[x] = 'x' if newBases[x] else 'o'
        self.render()
    def render(self):
        print("    "),
        print(self.bases[1])
        print("    / \\")
        print("   /   \\")
        print("  /     \\")
        print(" /       \\")
        print(self.bases[2]),
        print("       "),
        print(self.bases[0])
        print(" \\       /")
        print("  \\     /")
        print("   \   /")
        print("    \\ /")
        print("     O")
