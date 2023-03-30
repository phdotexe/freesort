import random

class SortingGame:
    def __init__(self):
        self.lst = []
        self.size = 7
        self.generate()

    def generate(self):
        self.lst = random.sample(range(1, 101), self.size)
        self.show()

    def show(self):
        print(self.lst)

    def swap(self, a, b):
        self.lst[a], self.lst[b] = self.lst[b], self.lst[a]

    def merge_sort(self, lst, start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        self.merge_sort(lst, start, mid)
        self.merge_sort(lst, mid+1, end)
        self.merge(lst, start, mid, end)

    def merge(self, lst, start, mid, end):
        i = start
        j = mid + 1
        merged = []
        while i <= mid and j <= end:
            if lst[i] <= lst[j]:
                merged.append(lst[i])
                i += 1
            else:
                merged.append(lst[j])
                j += 1
        while i <= mid:
            merged.append(lst[i])
            i += 1
        while j <= end:
            merged.append(lst[j])
            j += 1
        for k in range(len(merged)):
            lst[start + k] = merged[k]

def main():
    game = SortingGame()
    while True:
        print("Enter 'sort' to sort the list, 'swap' to swap the indices or 'done' to finish:")
        choice = input().lower()
        if choice == "done":
            if game.lst == sorted(game.lst):
                print("Congratulations, you sorted the list!")
            else:
                print("Sorry, the list is not sorted yet.")
            break
        elif choice == "sort":
            game.merge_sort(game.lst, 0, len(game.lst)-1)
            game.show()
        elif choice == "swap":
            try:
                a = int(input("Enter the index of the first element to swap: "))
                b = int(input("Enter the index of the second element to swap: "))
                game.swap(a, b)
                game.show()
            except ValueError:
                print("Invalid input. Please enter integer indices.")
        else:
            print("Invalid input. Please enter 'sort', 'swap', or 'done'.")

if __name__ == "__main__":
    main()
