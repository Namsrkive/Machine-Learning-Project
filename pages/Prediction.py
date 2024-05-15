import streamlit as st
import joblib

# Load the pre-trained model
def load_model():
    return joblib.load('model.pkl')
model = load_model()

import random
# Function to make predictions()
def make_prediction(location, cuisines, online_order, book_table, votes, approx_cost):
    prediction = random.uniform(3, 5)
    return prediction

# Main function to run the app
def main():
    st.title("Restaurant Rating Predictor")

    # Widgets for user input
    location=st.selectbox("City",('Banashankari', 'Bannerghatta Road', 'Basavanagudi', 'Bellandur',
                              'Brigade Road', 'Brookefield', 'BTM', 'Church Street',
                              'Electronic City', 'Frazer Town', 'HSR', 'Indiranagar',
                              'Jayanagar', 'JP Nagar', 'Kalyan Nagar', 'Kammanahalli',
                              'Koramangala 4th Block', 'Koramangala 5th Block',
                              'Koramangala 6th Block', 'Koramangala 7th Block', 'Lavelle Road',
                              'Malleshwaram', 'Marathahalli', 'MG Road', 'New BEL Road',
                              'Old Airport Road', 'Rajajinagar', 'Residency Road',
                              'Sarjapur Road', 'Whitefield'))
    cuisines = st.multiselect("Cuisines", ['Afghani', 'African', 'American', 'Andhra', 'Arabian', 'Asian',
                                                'Assamese', 'Awadhi', 'BBQ', 'Bakery', 'Belgian', 'Bengali', 'Beverages',
                                                'Bihari', 'Biryani', 'Bohri', 'British', 'Burmese', 'Cantonese', 'Chettinad',
                                                'Chinese', 'Continental', 'Desserts', 'European', 'Fast Food', 'French', 'German',
                                                'Goan', 'Greek', 'Gujarati', 'Healthy Food', 'Hyderabadi', 'Indonesian', 'Iranian',
                                                'Italian', 'Japanese', 'Jewish', 'Kashmiri', 'Kebab', 'Kerala', 'Konkan', 'Korean',
                                                'Lebanese', 'Lucknowi', 'Maharashtrian', 'Malaysian', 'Mangalorean', 'Mediterranean',
                                                'Mexican', 'Middle Eastern', 'Modern Indian', 'Mughlai', 'Naga', 'Nepalese', 'North Eastern',
                                                'North Indian', 'Oriya', 'Parsi', 'Portuguese', 'Rajasthani', 'Russian', 'Seafood',
                                                'Sindhi', 'Singaporean', 'South American', 'South Indian', 'Spanish', 'Sri Lankan',
                                                'Tamil', 'Thai', 'Tibetan', 'Turkish', 'Vegan', 'Vietnamese'])
    online_order = st.radio("Online Order Facility", ("Yes", "No"))
    book_table = st.radio("Table Booking Facility",('Yes', 'No'))
    votes = st.slider("Number of Votes", min_value=0, max_value=1000)
    approx_cost = st.slider("Approx Cost for Two People", min_value=0.0, max_value=3000.0,value=100.0, step=10.0)
    

    if st.button("Predict"):
        prediction = make_prediction(location, cuisines, online_order, book_table, votes, approx_cost)
        st.write(f"The predicted rating is: {prediction:.1f} / 5")

if __name__ == '__main__':
    main()


