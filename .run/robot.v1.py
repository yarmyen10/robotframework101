import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

def browse_file():
    file_path = filedialog.askopenfilename(
        title="เลือกไฟล์",
        filetypes=[
            ("CSV Files", "*.csv"),
            ("Excel Files", "*.xlsx *.xls"),
            ("All Files", "*.*")
        ]
    )
    if file_path:
        filename_entry.config(state=tk.NORMAL)
        filename_entry.delete(0, tk.END)
        filename_entry.insert(0, os.path.basename(file_path))
        filename_entry.config(state='readonly')

        venv_robot = os.path.abspath("../.venv/Scripts/robot.exe")
        pg_robot = os.path.abspath("../projects/.main/hard-working.robot")
        command = f'"{venv_robot}" --variable PATH_FILE:"{file_path}" {pg_robot}'

        command_robot.config(state=tk.NORMAL)
        command_robot.delete("1.0", tk.END)
        command_robot.insert("1.0", command)
        command_robot.config(state='normal', wrap='word')  # แก้ได้

def run_command():
    cmd = command_robot.get("1.0", tk.END).strip()
    if not cmd:
        messagebox.showerror("Error", "กรุณาใส่คำสั่ง Robot Framework ก่อน")
        return
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("สำเร็จ", result.stdout)
        else:
            messagebox.showerror("เกิดข้อผิดพลาด", result.stderr)
    except Exception as e:
        messagebox.showerror("Exception", str(e))

# GUI setup
root = tk.Tk()
root.title("Robot Framework Command Runner")
root.geometry("600x250")

# frame สำหรับชื่อไฟล์ + ปุ่ม
file_frame = tk.Frame(root)
file_frame.pack(pady=10)

filename_entry = tk.Entry(file_frame, width=70, state='readonly')
filename_entry.pack(side=tk.LEFT, padx=(0, 5))
filename_entry.insert(0, "เลือกไฟล์ CSV / Excel / อื่น ๆ")

browse_button = tk.Button(file_frame, text="เลือกไฟล์", command=browse_file)
browse_button.pack(side=tk.LEFT)

# label + กล่อง path เต็ม
tk.Label(root, text="Command Robot:").pack(anchor="w", padx=10)
command_robot = tk.Text(root, width=70, height=4, wrap="none")
command_robot.pack(padx=10)
# command_robot.config(state='disabled')  # ให้แก้ไม่ได้

# ปุ่มรัน
run_button = tk.Button(root, text="รัน/ทำงานกับไฟล์", command=run_command)
run_button.pack(pady=10)

root.mainloop()
