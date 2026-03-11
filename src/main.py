import tkinter as tk

def GUI():
    root = tk.Tk()
    root.title("Scraper GUI")

    frame = tk.Frame(root, width=1280, height=720)
    frame.pack(padx=10, pady=10)    

    topFrame = tk.Frame(frame)
    topFrame.pack(pady=10)

    label = tk.Label(topFrame, text="Pull latest: ", font=("Arial", 16))
    label.pack(side='left', padx=(0, 5))

    pullButton = tk.Button(topFrame, text = "↓", command = Scrape)
    pullButton.pack(side='left')
    
    dataFrame = tk.Frame(frame, width=600, height=400, bg="lightgrey")
    dataFrame.pack(pady=10, padx=10)
    
    root.mainloop()

def Scrape():
    print("Scraping data...")

if __name__ == "__main__":
    GUI()