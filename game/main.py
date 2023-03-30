#Authors: Ukeme Etuk, Biobele Harry, Clinton Quaye
import pygame
import random

pygame.init()

# Set up the display
DIM = pygame.display.get_desktop_sizes()
WIDTH = DIM[0][0]-100
HEIGHT = DIM[0][1]-100
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Game")

# Set up the fonts
FONT = pygame.font.SysFont("", 64)
FONT2 = pygame.font.SysFont("", 24)

# Set up the colors
# Define some colors
BLACK = (50, 50, 50)
WHITE = (255, 255, 255)
PURPLE = (174, 105, 215)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SortingGame:
    # Initialize the variables
    def __init__(self):
        self.lst = []
        self.size = 7
        self.generate()
        self.selected = None
        self.sorted = False

    # Generate a new random list
    def generate(self):
        self.lst = random.sample(range(1, 100), self.size)
        self.selected = None
        self.sorted = False

    # Sort the list using merge sort algorithm
    def sort(self):
        if not self.sorted:
            self.merge_sort(self.lst, 0, len(self.lst)-1)
            self.sorted = True

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

    def swap(self, a, b):
        self.lst[a], self.lst[b] = self.lst[b], self.lst[a]
        self.selected = None

    #Dictates what happens when a selection is made
    def select(self, index):
        if self.selected is None:
            self.selected = index
        elif self.selected == index:
            self.selected = None
        else:
            self.swap(self.selected, index)

    #Draws the screen with the numbers on it
    def draw(self):
        gap = WIDTH // (self.size + 1)

        for i in range(self.size):
            color = BLACK
            if self.selected == i:
                color = PURPLE
            label = FONT.render(str(self.lst[i]), 1, WHITE)

            pygame.draw.rect(screen, color, (gap*(i+1) + gap//2 - label.get_width()//2 -18, 130, 90, 80), 0, 20)
            screen.blit(label, (gap*(i+1) + gap//2 - label.get_width()//2, 150))

    # A congratulation message that shows when the sort is finished
    def congrats(self):
        congrats = FONT.render("Congratulations, you won!!!", 1, PURPLE)
        screen.blit(congrats, (WIDTH//2 - 220, 60))

    #checks if a game is won
    def checkWin(self):
        mylist = self.lst
        for i in range(self.size - 1):
            if mylist[i] > mylist[i+1]:
                return False
        return True

    #Writes the instructions on the screen
    def writeInstructions(self):
        instr = FONT2.render("Instructions: ", 1, PURPLE)
        screen.blit(instr, (250, 300))

        instr = FONT2.render("1. To sort the list, press the SPACE key.", 1, PURPLE)
        screen.blit(instr, (250, 350))

        instr = FONT2.render("2. To generate a new random list, press the R key.", 1, PURPLE)
        screen.blit(instr, (250, 400))
    
        instr = FONT2.render("3. To quit the game, press the ESCAPE key or click the X button in the top right corner of the window.", 1, PURPLE)
        screen.blit(instr, (250, 450))

        instr = FONT2.render("4. To select a number to swap, click on it. The selected number will be highlighted in purple.", 1, PURPLE)
        screen.blit(instr, (250, 500))

        instr = FONT2.render("5. To swap the selected number with the adjacent number to the right, click on the right side of the selected number.", 1, PURPLE)
        screen.blit(instr, (250, 550))

        instr = FONT2.render("6. To swap the selected number with the adjacent number to the left, click on the left side of the selected number.", 1, PURPLE)
        screen.blit(instr, (250, 600))
    
def main():
    game = SortingGame()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        screen.fill(BLACK)
        game.draw()
        game.writeInstructions()
        if game.checkWin():
            game.congrats()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.sort()
                elif event.key == pygame.K_r:
                    game.generate()
                elif event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(game.size):
                    gap = WIDTH // (game.size + 1)
                    if x > gap*(i+1) and x < gap*(i+1) + gap:
                        game.select(i)
                        if game.checkWin():
                            game.congrats()
                            break
        pygame.display.update()

if __name__ == "__main__":
    main()
    pygame.quit()