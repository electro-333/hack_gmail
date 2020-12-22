from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button





appl="""
MDFloatLayout:
	md_bg_color:[238/255,255/255,164/255,1]
	MDFloatLayout:
		MDToolbar:
			pos_hint:{'top':1}
			#MDIconButton:
				#icon:'format-list-bulleted'
		MDCard:
			size_hint:1,.926
			pos_hint:{'center_y':.462,'center_x':.5}
			Carousel:
				id:slider
				
				MDFloatLayout:
					
					MDLabel:
						id:label2
						text:''
						pos_hint:{'center_y':0.17,'center_x':.63}
						font_size:20
						markup:True
					MDLabel:
						text:'SingUp'
						pos_hint:{'center_y':0.8,'center_x':.85}
						font_size:70
					MDTextField:
						id:username4
						helper_text:'example_numbers'
						helper_text_mode:'on_focus'
						pos_hint:{'center_x':.5,'center_y':.7}
						icon_right:'account'
						size_hint:None,None
						size:530,20
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDTextField:
						helper_text:'example@gmail.com'
						helper_text_mode:'on_focus'
						id:email
						pos_hint:{'center_x':.5,'center_y':.55}
						icon_right:'email'
						size_hint:None,None
						size:530,20
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDTextField:
						helper_text:'enter at least four letters '
						helper_text_mode:'on_focus'
						id:password
						pos_hint:{'center_x':.5,'center_y':.4}
						icon_right:'eye-off'
						size_hint:None,None
						size:530,20
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDTextField:
						helper_text:'confirm password '
						helper_text_mode:'on_focus'
						id:confirme
						pos_hint:{'center_x':.5,'center_y':.25}
						icon_right:'eye-off'
						size_hint:None,None
						size:530,20
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDRaisedButton:
						text:'[color=ffffff] next [/color] '
						markup:True
						pos_hint:{'center_x':.5,'center_y':.1}
						size_hint:.3,.05
						on_press:app.add_label()
						md_bg_color:[0/255,0/255,0/255,1]
						font_size:20
						on_release:app.next()
						
						
						
						
				MDFloatLayout:
					MDLabel:
						text:'LOGIN'
						pos_hint:{'center_y':0.8,'center_x':.85}
						font_size:70	
					MDLabel:
						id:label
						text:' '
						pos_hint:{'center_y':0.43,'center_x':.76}
						font_size:20
						markup:True
					MDTextField:
						id:username
						pos_hint:{'center_x':.5,'center_y':.6}
						icon_right:'account'
						size_hint:None,None
						size:530,20
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDTextField:
						id:passw
						password:True
						size_hint:None,None
						size:530,20
						pos_hint:{'center_x':.5,'center_y':.5}
						icon_right:'eye-off'
						icon_right_color:[0/255,106/255,0/255,1]
						color_mode:'custom'
						line_color_focus:[0/255,0/255,0/255,1]
					MDRaisedButton:
						text:'[color=ffffff] enter [/color] '
						markup:True
						pos_hint:{'center_x':.5,'center_y':.35}
						size_hint:.3,.05
						on_press:app.add_label()
						md_bg_color:[0/255,0/255,0/255,1]
						font_size:20
						
						
						
				
						
				
			
				
				
					
				
					
					
					
"""
class MainApp(MDApp):
	def build(self):
		myApp=Builder.load_string(appl)
		return myApp
		
		
		
	#singup
	def add_label(self):
		password_get=self.root.ids.password.text
		user_name=self.root.ids.username4.text
		password=self.root.ids.passw.text
		user=self.root.ids.username.text
		
		if len(user)==0 and len(password)==0:
			self.root.ids.label.text=('[color=ff0000]please enter a existing information[/color]')
			self.root.ids.slider.load_previous()
			
		elif user==user_name and password ==password_get:
			self.root.ids.label.text=('[color=00ff00]              login successfuly[/color]')
			self.root.ids.slider.load_next(mode='next')
			
			
		elif password =='' or user=='':
			self.root.ids.label.text=('[color=ff0000]        there is an empty place[/color]')
			
			
		else:
			self.root.ids.label.text=('[color=ff0000]username or password is incorrect[/color] ')
			
			
	#login
	def next(self):
		password_get=self.root.ids.password.text
		user_name=self.root.ids.username4.text
		conf=self.root.ids.confirme.text
		
		
		
		if len(password_get)>=6 and len(user_name)>=4 and conf==password_get:
			self.root.ids.slider.load_next(mode='next')
			
			
		elif len(password_get)<=4:
			self.root.ids.label2.text=('[color=ff0000]  A strong password consists of at least 4 characters[/color] ')
			
			
			
		elif conf != password_get:
			self.root.ids.label2.text=('[color=ff0000]               there is a problem in confimation [/color] ')
			
			
		else:
			self.root.ids.label2.text=('[color=ff0000]                    unknow error[/color] ')		
		
MainApp().run()
