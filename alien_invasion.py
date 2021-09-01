import sys, pygame

class AlienInvasion:
    def __init__(self):
        #initialize game & Resources
        pygame.init()
        

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("datadenn's Alien Invasion!")

        self.bg_color = (230, 230, 230)

    def run_game(self):
        #main loop to run the game
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == "__main__":
    #create instance
    ai = AlienInvasion()
    ai.run_game()