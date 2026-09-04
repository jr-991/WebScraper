import tkinter as tk
import scraper

def GUI():
    root = tk.Tk()
    root.title("Real Estate Viewer")
    root.geometry("1280x720")

    frame = tk.Frame(root, width=1280, height=720)
    frame.pack(padx=10, pady=10)    

    topFrame = tk.Frame(frame)
    topFrame.pack(pady=10)

    label = tk.Label(topFrame, text="Pull latest: ", font=("Arial", 16))
    label.pack(side='left', padx=(0, 5))

    pullButton = tk.Button(topFrame, text = "↓", command = pullLatest)
    pullButton.pack(side='left')
    
    dataFrame = tk.Frame(frame, bg="lightgrey", width=1280, height=720)
    dataFrame.pack(fill='both', expand=True, pady=10, padx=10)
    
    root.mainloop()

def pullLatest():
    scraper.fetch()

if __name__ == "__main__":
    GUI()