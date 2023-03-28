import streamlit as st
import requests

def welcome():
	return 'welcome all'

# this is the main function in which we define our webpage
def main():
	# giving the webpage a title
	st.title("Iris Flower Prediction")
	
	# here we define some of the front end elements of the web page like
	# the font and background color, the padding and the text to be displayed
	html_temp = """
	<div style ="background-color:yellow;padding:13px">
	<h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1>
	</div>
	"""
	
	# this line allows us to display the front end aspects we have
	# defined in the above code
	st.markdown(html_temp, unsafe_allow_html = True)
	
	# the following lines create text boxes in which the user can enter
	# the data required to make the prediction
	sepal_length = st.text_input("Sepal Length", "Type Here")
	sepal_width = st.text_input("Sepal Width", "Type Here")
	petal_length = st.text_input("Petal Length", "Type Here")
	petal_width = st.text_input("Petal Width", "Type Here")
	
	# the below line ensures that when the button called 'Predict' is clicked,
	# the prediction function defined above is called to make the prediction
	# and store it in the variable result
	if st.button("Predict"):
		url1 = "http://172.17.0.1:80"
		url2 = "http://172.17.0.1:8000"

		data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width" : petal_width
    	}
		
		try :
			response = requests.post(f"{url1}/predict", json=data, timeout=8000)
		except:
			response = requests.post(f"{url2}/predict", json=data, timeout=8000)

		if response.status_code == 200:
			hasil = response.json()
			st.success('The output is {}'.format(hasil['iris_type']))
			st.balloons()
		else:
			st.error("Error:", response.status_code, response.json())

if __name__=='__main__':
	main()

