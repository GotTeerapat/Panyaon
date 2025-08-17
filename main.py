import tkinter as tk 
from tkinter import messagebox
from DataBase import * 

version = 'v1.0.0'
global_id = int
global_room_name = str
global_user_name = str
global_answer = int
global_number = int

def Login_UI(): 
    root = tk.Tk() 
    root.title("Login user") 

    labelframe1 = tk.LabelFrame(text="Creater")
    labelframe1.grid(row=0, column=0)
    create_room1 = tk.Label(labelframe1, text="Room name:", font=("Arial",12)) 
    create_room1.grid(row=0, column=0, sticky='e') 
    entry_room1 = tk.Entry(labelframe1, font=("Arial",12)) 
    entry_room1.grid(row=0, column=1) 
    create_room1 = tk.Label(labelframe1, text="User number:", font=("Arial",12)) 
    create_room1.grid(row=1, column=0, sticky='e') 
    spinbox_room1 = tk.Spinbox(labelframe1, from_=0, to=4, width=18, font=("Arial",12), state='readonly') 
    spinbox_room1.grid(row=1, column=1) 
    label_user1 = tk.Label(labelframe1, text="User name:", font=("Arial",12)) 
    label_user1.grid(row=2, column=0, sticky='e') 
    entry_user1 = tk.Entry(labelframe1, font=("Arial",12)) 
    entry_user1.grid(row=2, column=1) 
    label_answer1 = tk.Label(labelframe1, text="Answer:", font=("Arial",12)) 
    label_answer1.grid(row=3, column=0, sticky='e') 
    entrl_answer1 = tk.Entry(labelframe1, font=("Arial",12)) 
    entrl_answer1.grid(row=3, column=1) 

    intVar1 = tk.IntVar() 
    radio1_1 = tk.Radiobutton(labelframe1, text='User1', font=("Arial",12), value=1, variable=intVar1) 
    radio1_1.grid(row=5, column=0) 
    radio2_1 = tk.Radiobutton(labelframe1, text='User2', font=("Arial",12), value=2, variable=intVar1) 
    radio2_1.grid(row=6, column=0) 
    radio3_1 = tk.Radiobutton(labelframe1, text='User3', font=("Arial",12), value=3, variable=intVar1) 
    radio3_1.grid(row=7, column=0) 
    radio4_1 = tk.Radiobutton(labelframe1, text='User4', font=("Arial",12), value=4, variable=intVar1) 
    radio4_1.grid(row=8, column=0) 

    labelframe2 = tk.LabelFrame(text="Users")
    labelframe2.grid(row=0, column=1)
    create_room2 = tk.Label(labelframe2, text="Room name:", font=("Arial",12)) 
    create_room2.grid(row=0, column=0, sticky='e') 
    entry_room2 = tk.Entry(labelframe2, font=("Arial",12)) 
    entry_room2.grid(row=0, column=1) 
    label_user2 = tk.Label(labelframe2, text="User name:", font=("Arial",12)) 
    label_user2.grid(row=1, column=0, sticky='e') 
    entry_user2 = tk.Entry(labelframe2, font=("Arial",12)) 
    entry_user2.grid(row=1, column=1) 
    label_answer2 = tk.Label(labelframe2, text="Answer:", font=("Arial",12)) 
    label_answer2.grid(row=2, column=0, sticky='e') 
    entrl_answer2 = tk.Entry(labelframe2, font=("Arial",12)) 
    entrl_answer2.grid(row=2, column=1) 

    intVar2 = tk.IntVar() 
    radio1_2 = tk.Radiobutton(labelframe2, text='User1', font=("Arial",12), value=1, variable=intVar2) 
    radio1_2.grid(row=3, column=0) 
    radio2_2 = tk.Radiobutton(labelframe2, text='User2', font=("Arial",12), value=2, variable=intVar2) 
    radio2_2.grid(row=4, column=0) 
    radio3_2 = tk.Radiobutton(labelframe2, text='User3', font=("Arial",12), value=3, variable=intVar2) 
    radio3_2.grid(row=5, column=0) 
    radio4_2 = tk.Radiobutton(labelframe2, text='User4', font=("Arial",12), value=4, variable=intVar2) 
    radio4_2.grid(row=6, column=0) 

    def click_enter():
        global global_id
        global global_room_name
        global global_user_name
        global global_answer
        global global_number

        if entry_room1.get() != '':
            table_name : str
            table_name = entry_room1.get()
            global_room_name = table_name
            if table_name.isnumeric():
                table_name = f"\"{table_name}\""
            
            global_number = spinbox_room1.get()
            # create table
            db = DataBase(table_name)
            db.create_table()
            db.closeDataBase()
            # insert user
            id_name = int(intVar1.get())
            global_id = id_name
            user_name = entry_user1.get ()
            global_user_name = user_name
            answer = int(entrl_answer1.get())
            global_answer = answer
            insert = insertDatabase(table_name, param_one=(id_name, user_name, answer, global_number))
            insert.executeOneApply()
            insert.closeDataBase()
            root.destroy()
        else:
            try:
                table_name = entry_room2.get()
                global_room_name = table_name
                # insert user
                id_name = int(intVar2.get())
                global_id = id_name
                user_name = entry_user2.get()
                global_user_name = user_name
                answer = int(entrl_answer2.get())
                global_answer = answer
                insert = insertDatabase(table_name, param_one=(id_name, user_name, answer, None))
                insert.executeOneApply()
                insert.closeDataBase()
                root.destroy()
            except Exception:
                messagebox.showerror("Error", "This User unaviable")

    butt = tk.Button(root, text="Enter", font=("Arial",12), command=click_enter) 
    butt.grid(row=6, column=0, columnspan=2) 
    root.mainloop() 



class Panyaon: 
    def __init__(self, master): 
        self.master = master 
        self.master.title(f"Panyaon by Got SW {version}") 
        self.collecting_obj_user = []
        self.collecting_answer = [None]
        self.insert_to_table = ''
        self.continute_count = 3
        self.list_input = ''
        #อ่าน data base
        db = DataBase(global_room_name)
        # self.all_user= db.fetchAllData()
        main_user = db.fetchOne(global_id)
        self.other_users = db.fetchAllExcept(global_id)
        db.closeDataBase()

        frame_0 = tk.Frame(self.master)
        frame_0.grid(row=0, column=0)

        frame_1 = tk.Frame(self.master)
        frame_1.grid(row=1, column=0)

        self.frame_2 = tk.Frame(self.master)
        self.frame_2.grid(row=1, column=1)

        # Main User
        labelframe_user1 = tk.LabelFrame(frame_1, text=f"{global_user_name}")
        labelframe_user1.grid(row=0, column=0)
        answer_user_label = tk.Label(labelframe_user1, text='Answer:', font=("Arial",12))
        answer_user_label.grid(row=0, column=0, sticky='w')
        int_var_user1 = tk.IntVar()
        int_var_user1.set(global_answer)
        answer_user_number1 = tk.Label(labelframe_user1, textvariable=int_var_user1, font=("Arial",12))
        answer_user_number1.grid(row=0, column=0, sticky='w', padx=60)
        paper_butt1 = tk.Button(labelframe_user1, text='Paper', font=("Arial",12), command=self.paper_note)
        paper_butt1.grid(row=0, column=0, sticky='e')
        self.text_user1 = tk.Text(labelframe_user1, height=30, width=50, font=("Arial",12), state='disabled')
        self.text_user1.grid(row=1, column=0)
        self.entry_user1 = tk.Entry(labelframe_user1, font=("Arial",12))
        self.entry_user1.grid(row=2, column=0, sticky='w')

        end_butt1 = tk.Button(labelframe_user1, text='End Game', font=("Arial",12), command=self.end_game)
        end_butt1.grid(row=2, column=0, sticky='e')

        self.entry_user1.bind("<Return>", self.user_one_update)
        self.other_user()
        self.master.after(1000, self.update_other)

    def paper_note(self):
        root = tk.Toplevel()
        tk.Text(root, height=30, width=50, font=("Arial",12), state='normal').grid(row=1, column=0)


    def end_game(self):
        db = updateDatabase(table_name=global_room_name, param_field=global_id, param_update=True)
        db.UpdateEndGame()
        db.closeDataBase()

    def other_user(self):
        # ลบ widget เดิมก่อนสร้างใหม่
        for widget in self.frame_2.winfo_children():
            widget.destroy()
        self.collecting_obj_user.clear()
        if self.other_users:
            for idx, user in enumerate(self.other_users):
                id_name, user_name, answer, input_ans, user_num, end_game = user
                labelframe_user2 = tk.LabelFrame(self.frame_2, text=f"{user_name}")
                labelframe_user2.grid(row=idx+1, column=0)
                answer_user_label2 = tk.Label(labelframe_user2, text='Answer:', font=("Arial",12))
                answer_user_label2.grid(row=0, column=0, sticky='w')
                int_var_user2 = tk.IntVar()
                int_var_user2.set(answer)
                answer_user_number2 = tk.Label(labelframe_user2, textvariable=int_var_user2, font=("Arial",12), bg="black")
                answer_user_number2.grid(row=0, column=0, sticky='w', padx=60)
                text_user2 = tk.Text(labelframe_user2, height=10, width=30, font=("Arial",12), state='disabled')
                text_user2.grid(row=1, column=0)
                self.collecting_obj_user.append((id_name, text_user2, answer_user_number2))

    def user_one_update(self, event): 
        input_answer = self.entry_user1.get()
        self.text_user1.config(state='normal')
        self.text_user1.insert("end", f"\n{input_answer}")
        self.text_user1.config(state='disabled')
        self.list_input+=f";{input_answer}"
        db = updateDatabase(table_name=global_room_name, param_field=global_id, param_update=str(self.list_input))
        db.UpdateInput()
        db.closeDataBase()

    def update_other(self):
        db = DataBase(global_room_name)
        num = db.fetchUserNum()
        first_idx,*x = num
        self.other_users = db.fetchAllExcept(global_id)
        self.all_user= db.fetchAllData()
        db.closeDataBase()
        if len(self.all_user) != first_idx:
            self.other_user()
        elif self.continute_count:
            self.other_user()
            self.continute_count-=1

        for id_name, obj, label in self.collecting_obj_user:
            for user in self.other_users:
                if id_name == user[0]:
                    joiner = '\n'
                    if user[3] != None:
                        x = user[3].split(';')
                        show_on_table = joiner.join(x)
                        obj.config(state='normal')
                        obj.delete("1.0", tk.END)
                        obj.insert("1.0", show_on_table)
                        obj.config(state='disabled')
                    if user[5]:
                        label.config(bg='green')

        self.master.after(1000, self.update_other)

if __name__ == '__main__': 
    Login_UI() 

    root = tk.Tk() 
    Panyaon(root) 
    root.mainloop()