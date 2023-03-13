import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

# Normal Text
st.write("Hello, let's learn Streamlit at Pacmann")

# Title
st.title("This is the title of my first project about Streamlit")

# Header Subheader
st.header("This is a header")
st.subheader("this is the subheader")

# This is Markdown
st.markdown("### this is the markdown")
st.markdown("## this is the markdown")
st.markdown("# this is the markdown")

# Camption
st.caption("this is the caption")

# Code
st.code("x=2021")

# Latex
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# Display Images
# import Image from pillow to open images
from PIL import Image
img = Image.open("img/loan.jpeg")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

	# display the text if the checkbox returns True value
	st.text("Showing the widget")

# success
st.success("Success")

# info
st.info("Information")

# warning
st.warning("Warning")

# error
st.error("Error")

# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Radio Button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))

# conditional statement to print
# show the result using the success function if Male
if (status == 'Male'):
	st.success("Male")
	st.balloons()
# show the result using the error function if Female
else:
	st.error("Female")

# Selection box
# first argument takes the titleof the selectionbox
# second argument takes options
hobby = st.selectbox("Hobbies: ",
					['Dancing', 'Reading', 'Sports'])

# print the selected hobby
st.write("Your hobby is: ", hobby)

# multi select box
# first argument takes the box title
# second argument takes the options to show
hobbies = st.multiselect('choose a planet:',['Jupiter', 'Mars', 'neptune'])

# write the selected options
st.write("You selected", len(hobbies), 'planet')



# Create a simple button that does nothing
st.button("Click me for no reason")

# Create a button, that when clicked, shows a text
if(st.button("About")):	
    with st.spinner('Wait for it...'):    
        time.sleep(5)
		
    st.text("Welcome To GeeksForGeeks!!!")
    st.balloons()


st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])

# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level = st.slider("Select the level", 1, 5)

# print the level
# format() is used to print value
# of a variable at a specific position
st.text('Selected: {}'.format(level))


st.number_input('Pick a number', 0,10)


# Text Input
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)

st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')

# Sidebar
st.sidebar.title("this is written inside the sidebar")
st.sidebar.button("click")

# Visualisasi
rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)

# give a title to our app
st.title('Welcome to BMI Calculator')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',
				('cms', 'meters', 'feet'))

# compare status value
if(status == 'cms'):
	# take height input in centimeters
	height = st.number_input('Centimeters')

	try:
		bmi = weight / ((height/100)**2)
	except:
		st.text("Enter some value of height")

elif(status == 'meters'):
	# take height input in meters
	height = st.number_input('Meters')

	try:
		bmi = weight / (height ** 2)
	except:
		st.text("Enter some value of height")

else:
	# take height input in feet
	height = st.number_input('Feet')

	# 1 meter = 3.28
	try:
		bmi = weight / (((height/3.28))**2)
	except:
		st.text("Enter some value of height")

# check if the button is pressed or not
if(st.button('Calculate BMI')):

	# print the BMI INDEX
	st.text("Your BMI Index is {}.".format(bmi))

	# give the interpretation of BMI index
	if(bmi < 16):
		st.error("You are Extremely Underweight")
	elif(bmi >= 16 and bmi < 18.5):
		st.warning("You are Underweight")
	elif(bmi >= 18.5 and bmi < 25):
		st.success("Healthy")
	elif(bmi >= 25 and bmi < 30):
		st.warning("Overweight")
	elif(bmi >= 30):
		st.error("Extremely Overweight")

