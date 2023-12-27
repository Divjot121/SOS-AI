import tkinter as tk
import random
import time

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.master.geometry("420x500")

        self.canvas = tk.Canvas(self.master, bg="black", width=400, height=400)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 400, 400, outline="white")

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.is_paused = False

        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", fg="white", bg="black")
        self.score_label.pack()

        self.high_score_label = tk.Label(self.master, text=f"High Score: {self.get_high_score()}", fg="white", bg="black")
        self.high_score_label.pack()

        self.start_time = time.time()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

        self.pause_button = tk.Button(self.master, text="Pause/Resume", command=self.toggle_pause)
        self.pause_button.pack()

        self.master.bind("<Key>", self.change_direction)

        self.update()

    def create_food(self):
        x = random.randrange(1, 39) * 10
        y = random.randrange(1, 39) * 10
        return self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="red")

    def move(self):
        if not self.is_paused:
            head = list(self.snake[0])

            if self.direction == "Up":
                head[1] -= 10
            elif self.direction == "Down":
                head[1] += 10
            elif self.direction == "Left":
                head[0] -= 10
            elif self.direction == "Right":
                head[0] += 10

            self.snake.insert(0, tuple(head))

            if self.snake[0] == (self.canvas.coords(self.food)[0], self.canvas.coords(self.food)[1]):
                self.canvas.delete(self.food)
                self.food = self.create_food()
                self.score += 1
                self.update_score()
            else:
                self.canvas.delete(self.snake[-1])
                self.snake.pop()

            if self.is_game_over():
                self.game_over()

            self.draw_snake()

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(
                segment[0], segment[1], segment[0] + 10, segment[1] + 10, fill="green", tags="snake"
            )

    def change_direction(self, event):
        if event.keysym in ["Up", "Down", "Left", "Right"]:
            if (
                (event.keysym == "Up" and self.direction != "Down")
                or (event.keysym == "Down" and self.direction != "Up")
                or (event.keysym == "Left" and self.direction != "Right")
                or (event.keysym == "Right" and self.direction != "Left")
            ):
                self.direction = event.keysym

    def update(self):
        self.move()
        if not self.is_game_over() and not self.is_paused:
            self.master.after(100, self.update)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")
        high_score = self.get_high_score()
        self.high_score_label.config(text=f"High Score: {high_score}")

    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
            self.update()

    def restart_game(self):
        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.create_food()
        self.direction = "Right"
        self.score = 0
        self.is_paused = False
        self.start_time = time.time()
        self.update_score()
        self.update()

    def game_over(self):
        end_time = time.time()
        play_time = round(end_time - self.start_time, 2)
        high_score = self.get_high_score()

        if self.score > high_score:
            self.set_high_score(self.score)
            self.canvas.create_text(
                200, 240, text=f"Congratulations!\nNew High Score: {self.score}", font=("Helvetica", 16), fill="white"
            )
        else:
            self.canvas.create_text(
                200, 240, text=f"High Score: {high_score}", font=("Helvetica", 16), fill="white"
            )

        self.canvas.create_text(
            200, 180, text=f"Game Over\nScore: {self.score}\nTime: {play_time} seconds", font=("Helvetica", 16), fill="white"
        )

        self.master.after_cancel(self.update)

    def is_game_over(self):
        if any(
            [
                self.snake[0][0] < 0,
                self.snake[0][0] >= 400,
                self.snake[0][1] < 0,
                self.snake[0][1] >= 400,
                self.snake[0] in self.snake[1:],
            ]
        ):
            return True
        return False

    def get_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                high_score = int(file.read())
        except FileNotFoundError:
            high_score = 0
        return high_score

    def set_high_score(self, score):
        with open("high_score.txt", "w") as file:
            file.write(str(score))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
