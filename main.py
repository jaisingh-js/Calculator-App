import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty , BooleanProperty
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.core.window import Window


class Calculater(Widget):
	def __init__(self, **kwargs):
		super(Calculater, self).__init__(**kwargs)
		
		label = ObjectProperty(None)
		self.value1 = ""
		self.value2 = ""
		self.operation = ""
		self.ans = ""
		self.operation_pressed = False
		self.equal_pressed = False
		
		
	def get_size(self):
		if Window.size[1] > 1920:
			return 85
			
		else:
			return 70
	
		
	def  numeric(self, num):
		if self.operation_pressed == False and self.equal_pressed == False:
			if len(self.value1) < 8:
					self.value1 = self.value1 + num
					self.update_text()
				
		elif self.operation_pressed == True:
			if len(self.value2) < 8 :
					self.value2 = self.value2 + num
					self.update_text()
			
			
	def operator(self, oper):
		if self.value1 == "":
			pass
		
		elif self.value1 != "" and self.value2 == "":
			self.operation = oper
			self.update_text()
			self.operation_pressed = True
		
		elif self.value2 != "":
			self.calculate()
			self.value1 = str(self.ans)
			self.ans = ""
			self.operation = oper
			self.value2 = ""
			self.operation_pressed = True
			self.update_text()
			
			
			
			
	def equal(self):
		if self.value1 != "" and self.value2!= "" :
			self.calculate()
			if self.ans == "error":
				self.label.text = "Error"
				self.value1 = ""
				self.value2 = ""
				self.ans = ""
				self.operation = ""
				self.operation_pressed = False
				self.equal_pressed = False
			
			else:
				self.label.text = str(self.ans)
				self.value1 = str(self.ans)
				self.ans = ""
				self.value2 = ""
				self.operation = ""
				self.operation_pressed = False
				self.equal_pressed = True
		
				
				
	def calculate(self):
		if self.value1 != "" and self.value2 != "":
			try :
				if (self.operation == "+") :
					self.ans = round(float(self.value1) + float(self.value2) , 4)
				
				elif (self.operation == "-") :
					self.ans = round(float(self.value1) - float(self.value2) , 4)
				
				elif (self.operation == "×") :
					self.ans = round(float(self.value1) * float(self.value2) , 4)
				
				elif (self.operation == "/") :
					self.ans = round(float(self.value1) / float(self.value2) , 4)
				
				
			except:
				self.ans = "error"				
				
			
			
			
	def clear(self):
			self.label.text = "0"
			self.value1 = ""
			self.value2 = ""
			self.ans = ""
			self.operation = ""
			self.operation_pressed = False
			self.equal_pressed = False
			
						
	def update_text(self):
			self.label.text = self.value1 + self.operation + self.value2
			


	def no_dot(self):
			if self.value1 == "":
				self.numeric(".")
				
			elif self.value1 != "" and self.operation_pressed == False and self.equal_pressed == False:
				if "." not in self.value1:
					return self.numeric(".")
				else:
					return
					
			elif self.value2 == "" and (self.operation_pressed == True or self.equal_pressed == True):
				return self.numeric(".")
				
			elif self.value2 != "" and (self.operation_pressed == True or self.equal_pressed == True):
				if "." not in self.value2:
					return self.numeric(".")
				else:
					return
				
			
			

	
	
class Cbtn(Button):
	def __init__(self, **kwargs):
		super(Cbtn, self).__init__(**kwargs)
			
	def get_size(self):
		if Window.size[1] > 1919 :
			return 75
			
		else:
			return 55
	
	
class CalcApp(App):
	def build(self):
		c = Calculater()
		return c
		
		
if __name__ == "__main__":
	CalcApp().run()