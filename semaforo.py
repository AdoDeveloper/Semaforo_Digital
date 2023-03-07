import tkinter as tk

class TrafficLight:
    def __init__(self, master):
        self.master = master
        self.master.title("Semáforo")
        self.light_radius = 50
        self.canvas_width = self.light_radius * 4
        self.canvas_height = self.light_radius * 10
        self.canvas = tk.Canvas(self.master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.red_light = self.canvas.create_oval(
            self.light_radius, self.light_radius,
            self.light_radius*3, self.light_radius*3,
            fill="gray")
        self.yellow_light = self.canvas.create_oval(
            self.light_radius, self.light_radius*4,
            self.light_radius*3, self.light_radius*6,
            fill="gray")
        self.green_light = self.canvas.create_oval(
            self.light_radius, self.light_radius*7,
            self.light_radius*3, self.light_radius*9,
            fill="gray")
        self.current_color = "red"
        self.change_color()

    def change_color(self):
        if self.current_color == "red":
            self.canvas.itemconfigure(self.red_light, fill="red")
            self.canvas.itemconfigure(self.yellow_light, fill="gray")
            self.canvas.itemconfigure(self.green_light, fill="gray")
            self.current_color = "green"
            wait_time = 60000
        elif self.current_color == "green":
            self.canvas.itemconfigure(self.red_light, fill="gray")
            self.canvas.itemconfigure(self.yellow_light, fill="gray")
            self.canvas.itemconfigure(self.green_light, fill="green")
            self.current_color = "yellow"
            wait_time = 60000
        else:
            self.canvas.itemconfigure(self.red_light, fill="gray")
            self.canvas.itemconfigure(self.yellow_light, fill="yellow")
            self.canvas.itemconfigure(self.green_light, fill="gray")
            self.current_color = "red"
            wait_time = 3000
        self.master.after(wait_time, self.change_color)

if __name__ == "__main__":
    root = tk.Tk()
    tl = TrafficLight(root)
    root.mainloop()
