import pandas as pd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as msg
from pandastable import Table
from tkintertable import TableCanvas
from input_one_remake import *

class excel_to_excel:
	def __init__(self, root):
		self.root = root
		self.file_name = ''
		self.f = Frame(self.root,
					height = 200,
					width = 300)
		# Place the frame on root window
		self.f.pack()
		# Creating label widgets
		self.message_label = Label(self.f,
								text = 'Apollo',
								font = ('Arial', 19,'underline'),
								fg = 'Green')
		self.message_label2 = Label(self.f,
									text = 'Converter of raw Excel to Sample Format file',
									font = ('Arial', 14,'underline'),
									fg = 'Red')

		# Buttons
		self.convert_button = Button(self.f,
									text = 'Convert',
									font = ('Arial', 14),
									bg = 'Orange',
									fg = 'Black',
									command = self.convert_excel_to_excel)
		self.display_button = Button(self.f,
									text = 'Display',
									font = ('Arial', 14),
									bg = 'Green',
									fg = 'Black',
									command = self.display_xlsx_file)
		self.exit_button = Button(self.f,
								text = 'Exit',
								font = ('Arial', 14),
								bg = 'Red',
								fg = 'Black',
								command = root.destroy)

		# Placing the widgets using grid manager
		self.message_label.grid(row = 1, column = 1)
		self.message_label2.grid(row = 2, column = 1)
		self.convert_button.grid(row = 3, column = 0,
								padx = 0, pady = 15)
		self.display_button.grid(row = 3, column = 1,
								padx = 10, pady = 15)
		self.exit_button.grid(row = 3, column = 2,
							padx = 10, pady = 15)

	def convert_excel_to_excel(self):
		try:
			self.file_name = filedialog.askopenfilename(initialdir = '/Desktop',
														title = 'Select a excel file',
														filetypes = (('excel file','*.xls'),
																	('excel file','*.xlsx')))			
			df = pd.read_excel(self.file_name)
			# Next - Pandas DF to Excel file on disk
			if(len(df) == 0):	
				msg.showinfo('No Rows Selected', 'CSV has no rows')
			else:
                   
				remake_out(self.file_name)#correct_road()#,df.to_excel(self.file_name.rsplit('.', 1)[0] + '_out.xlsx', index=False)
				msg.showinfo('Excel file created', 'Excel File created')	
    
			
		except FileNotFoundError as e:
				msg.showerror('Error in opening file', e)

	def display_xlsx_file(self):
		try:
			self.file_name = filedialog.askopenfilename(initialdir = '/Desktop',
														title = 'Select a excel file',
														filetypes = (('excel file','*.xlsx'),
																	('excel file','*.xlsx')))
			df = pd.read_excel(self.file_name)
			
			if (len(df)== 0):
				msg.showinfo('No records', 'No records')
			else:
				pass
				
			# Now display the DF in 'Table' object
			# under'pandastable' module
			self.f2 = Frame(self.root, height=200, width=300)
			self.f2.pack(fill=BOTH,expand=1)
			self.table = Table(self.f2, dataframe=df,read_only=True)
			self.table.show()
		
		except FileNotFoundError as e:
			print(e)
			msg.showerror('Error in opening file',e)

# Driver Code
root = Tk()
root.title('Convert Excel to Excel File')

obj = excel_to_excel(root)
root.geometry('800x600')
root.mainloop()

