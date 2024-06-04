import tkinter as tk #Import dan Deklarasi Kelas
from tkinter import messagebox
from collections import deque

class DailyActivity: #Kelas DailyActivity Mewakili sebuah kegiatan harian dengan tiga atribut
    def __init__(self, name, time, place, user): #method Konstruktor yang menginisialisasi objek DailyActivity dengan atribut name, time, dan place.
        self.name = name #Variable bertipe string
        self.time = time #Variable bertipe string
        self.place = place #Variable bertipe string
        self.user = user 

class ActivityManager: #deque (double-ended queue) yang menyimpan daftar kegiatan. #Kelas ActivityManager: Mengelola daftar kegiatan
    def __init__(self):
        self.activities = deque() # Menggunakan deque sebagai queue

    def add_activity(self, activity):
        self.activities.append(activity)  # Menambahkan elemen ke ujung deque (akhir queue)

    def remove_activity(self): #pengkondisian  # Menghapus dan mengembalikan elemen dari awal deque (awal queue)
        if self.activities:
            return self.activities.popleft() 
        return None

    def get_all_activities(self):
        return list(self.activities) # Mengembalikan semua elemen dalam deque sebagai list

    def clear_activities(self):
        self.activities.clear()

class ActivityGUI: #gui #Method    
    def __init__(self, root, manager): #Konstruktor (__init__): Inisialisasi GUI dan mengatur layout dasar
        self.root = root
        self.manager = manager
        self.root.title("Daily Activities")
        
        # Set root background color
        self.root.configure(bg='lightblue')

        self.frame = tk.Frame(self.root, bg='lightblue')
        self.frame.pack(padx=10, pady=10)

        self.user_label = tk.Label(self.frame, text="Nama:", bg='lightblue', fg='darkblue') #Menambahkan Input untuk Nama Kegiatan
        self.user_label.grid(row=3, column=0, padx=5, pady=5)
        self.user_entry = tk.Entry(self.frame)
        self.user_entry.grid(row=3, column=1, padx=5, pady=5)

        self.name_label = tk.Label(self.frame, text="Nama Aktivitas:", bg='lightblue', fg='darkblue') #Menambahkan Input untuk Nama Kegiatan
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.frame, text="Waktu:", bg='lightblue', fg='darkblue') 
        self.time_label.grid(row=1, column=0, padx=5, pady=5)

        self.hours = [f"{i:02d}" for i in range(24)] #looping 
        self.minutes = [f"{i:02d}" for i in range(60)] #looping

        self.selected_hour = tk.StringVar(value=self.hours[0])
        self.selected_minute = tk.StringVar(value=self.minutes[0])

        self.hour_menu = tk.OptionMenu(self.frame, self.selected_hour, *self.hours)
        self.hour_menu.grid(row=1, column=1, padx=5, pady=5)

        self.minute_menu = tk.OptionMenu(self.frame, self.selected_minute, *self.minutes)
        self.minute_menu.grid(row=1, column=2, padx=5, pady=5)

        self.place_label = tk.Label(self.frame, text="Tempat:", bg='lightblue', fg='darkblue') #Menambahkan Input untuk Tempat
        self.place_label.grid(row=2, column=0, padx=5, pady=5)
        self.place_entry = tk.Entry(self.frame)
        self.place_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(self.frame, text="Tambahkan Aktivitas", command=self.add_activity, bg='green', fg='white') #Tombol untuk Menambahkan Kegiatan
        self.add_button.grid(row=4, column=0, pady=10)

        self.clear_button = tk.Button(self.frame, text="Clear", command=self.clear_list, bg='red', fg='white')
        self.clear_button.grid(row=4, column=1, pady=10)

        self.listbox = tk.Listbox(self.frame) #Listbox untuk Menampilkan Kegiatan
        self.listbox.grid(row=5, columnspan=3, pady=10, padx=5, sticky='we')

        self.show_activities()

    def add_activity(self): #Metode untuk Menambahkan Kegiatan
        name = self.name_entry.get()
        hour = self.selected_hour.get()
        minute = self.selected_minute.get()
        place = self.place_entry.get()
        user = self.user_entry.get()

        if name and hour and minute and place: #pengkondisian
            time = f"{hour}:{minute}"
            activity = DailyActivity(name, time, place, user)
            self.manager.add_activity(activity)
            messagebox.showinfo("Sukses", "Aktivitas Berhasil Ditambahkan!")
            self.clear_entries()
            self.show_activities()
        else:
            messagebox.showwarning("Input Error", "Tolong Isi semua Bagian")

    def show_activities(self): #Looping #Metode untuk Menampilkan Kegiatan
        self.listbox.delete(0, tk.END)
        activities = self.manager.get_all_activities()
        for act in activities:
            self.listbox.insert(tk.END, f"{act.user} memiliki kegiatan {act.name} pada jam {act.time} di {act.place}")

    def clear_entries(self): #Metode untuk Menghapus Input
        self.name_entry.delete(0, tk.END)
        self.selected_hour.set(self.hours[0])
        self.selected_minute.set(self.minutes[0])
        self.place_entry.delete(0, tk.END)
        self.user_entry.delete(0, tk.END)

    def clear_list(self):
        self.manager.clear_activities()
        self.show_activities()

def main(): #function menginisialisasi dan menjalankan aplikasi Tkinter # Fungsi Utama untuk Menjalankan Aplikasi
    root = tk.Tk()
    manager = ActivityManager()
    gui = ActivityGUI(root, manager)
    root.mainloop()

if __name__ == "__main__":
    main()

    #Variable dan tipe data
    #Functiom and Method
    #Looping
    #Pengkondisian
    #Stack and queue
    #gui
