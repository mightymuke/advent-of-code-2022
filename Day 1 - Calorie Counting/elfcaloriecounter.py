class ElfCalorieCounter:
    def __init__(self):
        self.elfdata = []

    def load(self, elfdata):
        self.elfdata = []
        if len(elfdata) < 1:
            return

        calories = 0
        for x in elfdata:
            cleaned = x.strip()
            if len(cleaned) > 0:
                calories += int(cleaned)
            else:
                self.elfdata.append(calories)
                calories = 0
        if (calories > 0):
            self.elfdata.append(calories)

        self.elfdata.sort(reverse=True)

    def topCalories(self, count):
        return self.elfdata[:count]