import tkinter as tk
from functools import partial
import tkinter.font as font
import os



def text_analysis_func(window):
	window = tk.Tk()
	window.title("Text Analysis")
	text_analysis_func1(window)
	window.mainloop()

def text_analysis_func1(window):
	
	window.geometry("1300x780")


	label_quesone_ = tk.StringVar()  
	label_questwo_ = tk.StringVar() 
	label_questhree_ = tk.StringVar() 
	label_quesfour_ = tk.StringVar() 
	label_quesfive_ = tk.StringVar() 

	labelResult = tk.Label(window,font=("Tkdefault",18),pady="20",padx="90")  
	
	labelResult.grid(column=0,row=10) 


	def redirect():
		window.destroy()
		window.quit()
		os.system("python E:\Hackathon\SIH2022-main\code\login.py")

	def call_result(result1, a, b, c, d, e):
		a = [(a.get()), (b.get()), (c.get()), (d.get()), (e.get())]
		global score
		score = 0
		average_score = 0.0
		for i in a:
			if i.lower() == "yes":
				score = score + 1
			elif i.lower() == "no":
				score = score + 0
			else:
				score = -1
				continue
			
		average_score = score/5
		
		if score == -1:
				open_new()
				#result = "Invalid Response. Please Enter Yes or No."
		elif average_score >= 0.8:
				score = average_score
				open_new()
				#result = "You have high levels of empathy and interpersonal skills.\nHere are some tips and suggestions\nPractice active listening\nEmbrace differences\nPractice emotional intelligence\nDevelop effective communication skills."
		elif average_score >= 0.5:
				score = average_score
				open_new()
				#result = "You have moderate levels of empathy and interpersonal skills."
		else:
				score = average_score
				open_new()
				#result = "You have low levels of empathy and interpersonal skills."   
		return 	

	l = tk.Label(window, text = "Answer Yes/No For The Questions:",font =("Tkdefault", 20))
	l.grid(row=0, column=0, ipadx="100",ipady="30", pady="20", padx="60")

	label_quesone = tk.Label(window, text="If you see someone falling, would you help?", font=("Tkdefault",18))
	label_quesone.grid(row=1, column=0, ipadx="100", pady="20")

	label_quesone_ent = tk.Entry(window, font=("Tkdefault",18),textvariable=label_quesone_)
	label_quesone_ent.grid(row=1, column=1)

	label_questwo = tk.Label(window, text="Do you forgive people easily?", font=("Tkdefault",18))
	label_questwo.grid(row=2, column=0, ipadx="100",pady="20")

	label_questwo_ent = tk.Entry(window, font=("Tkdefault",18),textvariable=label_questwo_)
	label_questwo_ent.grid(row=2, column=1)

	label_questhree = tk.Label(window, text="Do you feel other people emotions?", font=("Tkdefault",18))
	label_questhree.grid(row=3, column=0, ipadx="100",pady="20")

	label_questhree_ent = tk.Entry(window, font=("Tkdefault",18),textvariable=label_questhree_)
	label_questhree_ent.grid(row=3, column=1)

	label_quesfour = tk.Label(window, text="Do you accept being wrong?", font=("Tkdefault",18))
	label_quesfour.grid(row=4, column=0, ipadx="100",pady="20")

	label_quesfour_ent = tk.Entry(window, font=("Tkdefault",18),textvariable=label_quesfour_)
	label_quesfour_ent.grid(row=4, column=1)

	label_quesfive = tk.Label(window, text="Do you apologize?", font=("Tkdefault",18))
	label_quesfive.grid(row=5, column=0, ipadx="100",pady="20")

	label_quesfive_ent = tk.Entry(window, font=("Tkdefault",18),textvariable=label_quesfive_)
	label_quesfive_ent.grid(row=5, column=1)

	call_result = partial(call_result, labelResult, label_quesone_, label_questwo_, label_questhree_, label_quesfour_, label_quesfive_) 

	submit_button = tk.Button(window, text="Logout", activebackground = "pink", activeforeground = "blue", bg='#0052cc',fg='#ffffff',height=2, width=10, command=redirect)
	submit_button.grid(row=8, column=0, columnspan=1, pady="5", padx="5")
	# submit_button.grid(side=tk.RIGHT)
	submit_button['font'] = font.Font(size=14, weight='bold')

	submit_button = tk.Button(window, text="Submit", activebackground = "pink", activeforeground = "blue", bg='#0052cc',fg='#ffffff',height=2, width=10, command=call_result)
	submit_button.grid(row=8, column=1, columnspan=1, pady="5", padx="5")
	# submit_button.pack(side=tk.LEFT)
	submit_button['font'] = font.Font(size=14, weight='bold')

	
def open_new():
		new_window = tk.Toplevel()
		new_window.geometry("900x500")
		la = tk.Label(new_window, text = "RESULT",font =("Tkdefault", 20))
		la.pack(pady=15)
		if score == -1:
				tk.Label(master=new_window, text="\nInvalid Response. Please Enter Yes or No.",font =("Tkdefault", 20)).pack()
				text1 = "\n\nInvalid Response. Please Enter Yes or No."
				#result = "Invalid Response. Please Enter Yes or No."
		elif score >= 0.8:
				tk.Label(master=new_window, text="\nYou have high levels of empathy and interpersonal skills\n\nHere are some tips and suggestions:\n\nPractice active listening\nEmbrace differences\nPractice emotional intelligence\nDevelop effective communication skills",font =("Tkdefault", 20)).pack()
				text1 = "\n\nYou have high levels of empathy and interpersonal skills\n\nHere are some tips and suggestions:\n\nPractice active listening\nEmbrace differences\nPractice emotional intelligence\nDevelop effective communication skills"
		elif score >= 0.5:
				tk.Label(master=new_window, text="\nYou have moderate levels of empathy and interpersonal skills.\n\nHere are some tips and suggestions:\n\nFocus on self-improvement\nPractice active listening\nLearn to understand others' perspectives\nDevelop effective communication skills",font =("Tkdefault", 20)).pack()
				text1 = "\n\nYou have high levels of empathy and interpersonal skills\n\nHere are some tips and suggestions:\n\nFocus on self-improvement\nPractice active listening\nLearn to understand others' perspectives\nDevelop effective communication skills"
				#result = "You have moderate levels of empathy and interpersonal skills."
		else:
				tk.Label(master=new_window, text="\nYou have low levels of empathy and interpersonal skills.\n\nHere are some tips and suggestions:\n\nFocus on self-awareness\nPractice active listening\nLearn about empathy\nManage your emotions\nPractice, practice, practice.",font =("Tkdefault", 20)).pack()
				text1 = "\n\nYou have high levels of empathy and interpersonal skills\n\nHere are some tips and suggestions:\n\nFocus on self-awareness\nPractice active listening\nLearn about empathy\nManage your emotions\nPractice, practice, practice."
				#result = "You have low levels of empathy and interpersonal skills."
		with open('text_result.txt', 'w') as f:
			f.write(text1)
		f.close()