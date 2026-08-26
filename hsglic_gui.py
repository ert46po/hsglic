import tkinter as tk
from tkinter import scrolledtext
import random

class HSGLICTouchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HSGLIC - Hacker GUI")
        self.root.geometry("450x650")
        self.root.config(bg="#0f0f0f")

        self.title_label = tk.Label(root, text="⚡ HSGLIC v1.0 [GUI Mode] ⚡", fg="#00ff66", bg="#0f0f0f", font=("Courier", 13, "bold"))
        self.title_label.pack(pady=10)

        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=48, height=18, bg="black", fg="#00ff66", insertbackground="green", font=("Courier", 10))
        self.text_area.pack(pady=5, padx=10)
        self.text_area.insert(tk.END, "[*] System Booted Successfully...\n[*] Tap the buttons below to execute hacker commands!\n\n")
        self.text_area.configure(state='disabled')

        self.btn_frame = tk.Frame(root, bg="#0f0f0f")
        self.btn_frame.pack(pady=15)

        self.create_touch_button(self.btn_frame, "🌐 Connect Target", self.connect_target, 0, 0, "#1a3300", "#00ff66")
        self.create_touch_button(self.btn_frame, "🔍 Scan Ports", self.scan_ports, 0, 1, "#00264d", "#3399ff")
        self.create_touch_button(self.btn_frame, "🛡️ Bypass Firewall", self.bypass_firewall, 1, 0, "#331a00", "#ff9933")
        self.create_touch_button(self.btn_frame, "⚡ Inject Payload", self.inject_payload, 1, 1, "#330000", "#ff4d4d")
        self.create_touch_button(self.btn_frame, "🧹 Clear Screen", self.clear_screen, 2, 0, "#262626", "#ffffff")
        self.create_touch_button(self.btn_frame, "❌ Exit Game", root.quit, 2, 1, "#262626", "#ff3333")

    def log_message(self, message):
        self.text_area.configure(state='normal')
        self.text_area.insert(tk.END, message + "\n")
        self.text_area.see(tk.END)
        self.text_area.configure(state='disabled')

    def connect_target(self):
        ip = f"192.168.{random.randint(1,255)}.{random.randint(1,255)}"
        self.log_message(f"[+] Connecting to secure node: {ip} ... [CONNECTED]")

    def scan_ports(self):
        self.log_message("[*] Scanning ports (80, 443, 8080)...")
        self.root.after(800, lambda: self.log_message("[!] Port 443 (HTTPS) is OPEN and vulnerable!"))

    def bypass_firewall(self):
        self.log_message("[*] Sending UDP packets to bypass firewall...")
        self.root.after(1000, lambda: self.log_message("[+] Firewall bypassed successfully!"))

    def inject_payload(self):
        self.log_message("[*] Uploading rootkit payload...")
        self.root.after(1200, lambda: self.log_message("[SUCCESS] ACCESS GRANTED! Welcome Admin."))

    def clear_screen(self):
        self.text_area.configure(state='normal')
        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.END, "[*] Screen wiped clean.\n\n")
        self.text_area.configure(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    app = HSGLICTouchApp(root)
    root.mainloop()
