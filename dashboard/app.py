<<<<<<< HEAD
import customtkinter as ctk
from theme import COLORS, FONTS
from agent_control import is_agent_running, start_agent, stop_agent
from log_reader import read_last_logs

ctk.set_appearance_mode("dark")


class SHCSDashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Self-Healing Cybersecurity System")
        self.geometry("920x580")
        self.resizable(False, False)

        header = ctk.CTkLabel(
            self,
            text="Self-Healing Cybersecurity System",
            font=FONTS["title"],
            text_color=COLORS["accent"]
        )
        header.pack(pady=(20, 10))

        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Checking...",
            font=FONTS["subtitle"]
        )
        self.status_label.pack(pady=(0, 15))

        controls = ctk.CTkFrame(self, fg_color=COLORS["panel"])
        controls.pack(pady=10)

        ctk.CTkButton(
            controls,
            text="Start Agent",
            width=150,
            fg_color=COLORS["success"],
            command=self.start_agent
        ).grid(row=0, column=0, padx=15, pady=15)

        ctk.CTkButton(
            controls,
            text="Stop Agent",
            width=150,
            fg_color=COLORS["danger"],
            command=self.stop_agent
        ).grid(row=0, column=1, padx=15, pady=15)

        log_label = ctk.CTkLabel(
            self,
            text="Live Agent Logs",
            font=FONTS["subtitle"]
        )
        log_label.pack(pady=(20, 5))

        self.log_box = ctk.CTkTextbox(
            self,
            width=880,
            height=300,
            font=FONTS["small"],
            state="disabled" 
        )
        self.log_box.pack(pady=(0, 15))

        self.refresh()

    def start_agent(self):
        start_agent()
        self.refresh_status()

    def stop_agent(self):
        stop_agent()
        self.refresh_status()

    def refresh_status(self):
        if is_agent_running():
            self.status_label.configure(
                text="Status: RUNNING",
                text_color=COLORS["success"]
            )
        else:
            self.status_label.configure(
                text="Status: STOPPED",
                text_color=COLORS["danger"]
            )

    def refresh_logs(self):
        scroll_pos = self.log_box.yview()

        logs = read_last_logs()

        self.log_box.configure(state="normal")   # 🔓 unlock
        self.log_box.delete("1.0", "end")
        self.log_box.insert("1.0", logs)
        self.log_box.configure(state="disabled") # 🔒 lock again

        self.log_box.yview_moveto(scroll_pos[0])

    def refresh(self):
        self.refresh_status()
        self.refresh_logs()
        self.after(3000, self.refresh)


if __name__ == "__main__":
    app = SHCSDashboard()
    app.mainloop()
=======
import customtkinter as ctk
from theme import COLORS, FONTS
from agent_control import is_agent_running, start_agent, stop_agent
from log_reader import read_last_logs

ctk.set_appearance_mode("dark")


class SHCSDashboard(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Self-Healing Cybersecurity System")
        self.geometry("920x580")
        self.resizable(False, False)

        header = ctk.CTkLabel(
            self,
            text="Self-Healing Cybersecurity System",
            font=FONTS["title"],
            text_color=COLORS["accent"]
        )
        header.pack(pady=(20, 10))

        self.status_label = ctk.CTkLabel(
            self,
            text="Status: Checking...",
            font=FONTS["subtitle"]
        )
        self.status_label.pack(pady=(0, 15))

        controls = ctk.CTkFrame(self, fg_color=COLORS["panel"])
        controls.pack(pady=10)

        ctk.CTkButton(
            controls,
            text="Start Agent",
            width=150,
            fg_color=COLORS["success"],
            command=self.start_agent
        ).grid(row=0, column=0, padx=15, pady=15)

        ctk.CTkButton(
            controls,
            text="Stop Agent",
            width=150,
            fg_color=COLORS["danger"],
            command=self.stop_agent
        ).grid(row=0, column=1, padx=15, pady=15)

        log_label = ctk.CTkLabel(
            self,
            text="Live Agent Logs",
            font=FONTS["subtitle"]
        )
        log_label.pack(pady=(20, 5))

        self.log_box = ctk.CTkTextbox(
            self,
            width=880,
            height=300,
            font=FONTS["small"]
        )
        self.log_box.pack(pady=(0, 15))

        self.refresh()

    def start_agent(self):
        start_agent()
        self.refresh_status()

    def stop_agent(self):
        stop_agent()
        self.refresh_status()

    def refresh_status(self):
        if is_agent_running():
            self.status_label.configure(
                text="Status: RUNNING",
                text_color=COLORS["success"]
            )
        else:
            self.status_label.configure(
                text="Status: STOPPED",
                text_color=COLORS["danger"]
            )

    def refresh_logs(self):
        scroll_pos = self.log_box.yview()

        logs = read_last_logs()
        self.log_box.delete("1.0", "end")
        self.log_box.insert("1.0", logs)

        self.log_box.yview_moveto(scroll_pos[0])

    def refresh(self):
        self.refresh_status()
        self.refresh_logs()
        self.after(3000, self.refresh)


if __name__ == "__main__":
    app = SHCSDashboard()
    app.mainloop()
>>>>>>> ff48c825f9fd64ae919885467895d38972d81c36
