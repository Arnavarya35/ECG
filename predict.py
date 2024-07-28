import streamlit as st
import pickle
import numpy as np

def load_binmodel():
    with open('bin_model.pkl', 'rb') as file:
        data = pickle.load(file)
    return data



def load_multimodel():
    with open('multi_model.pkl','rb') as file:
        mdata = pickle.load(file)
    return mdata

bin_model = load_binmodel()
multi_model = load_multimodel()


def show_predictpage():
	st.title('ECG Signal Based Heart Disease Prediction')
	st.write(""" ### We need some information to predict the chances of you having a heart disease""")

        st.write(""" ### Do you want to know whether your heartbeat is normal or abnormal.
                        Or an in-depth Analysis of your heartbeat ?""")

        choice = st.selectbox('Select your Chocie? Binary(for normal/abnormal), Multi-class(for in-depth)',
                                ('Binary', 'Multi-class'))

        if choice == 'Binary':
            bin_model = load_binmodel()
            user_data = np.array(arduino_data)
            user_data = user_data.reshape(1, 187, 1)

            pred = bin_model.predict(user_data)
            prediction = np.round(pred).flatten()
            if prediction == 1.0:
                st.subheader('Your Heart Beat is Abnormal.Consult a Doctor!')
            else:
                st.subheader('You Heart Beat is Normal.)
        else:
                             multi_model = load_multimodel()
                             user_data = np.array(arduino_data)
                             user_data = user_data.reshape(1,187,1)
                             mpred =  multi_model.predict(user_data)
                             mprediction = np.round(new_ypred).flatten()
                             for i in range(mprediction):
                                 if mprediction[0] == 1:
                                     st.subheader('Your Heart Beat is Completely Normal.')
                                 elif mprediction[1] == 1:
                                     st.subheader('Your Heart Beat comes under Supraventricular Ectopic Beat.')
                                     st.write("""# Supraventricular tachycardias (SVT) is a kind of abnormally fast heart rhythm (heartbeat). It's a problem in the electrical system of the heart. The word supraventricular means above the ventricles. With SVT, the abnormal rhythm starts in the upper heart chambers (atria).""")
                                 elif mprediction[2] == 1:
                                     st.subheader('Your Heart Beat is Ventricular Ectopic Beat.')
                                     st.write("""# Premature ventricular contractions (PVCs) are extra heartbeats that begin in one of the heart's two lower pumping chambers (ventricles). These extra beats disrupt the regular heart rhythm, sometimes causing a sensation of a fluttering or a skipped beat in the chest.""")
                                 elif mprediction[3] == 1:
                                     st.subheader('Your Heart beat is a type of Fusion beat.')
                                     st.write("""# A fusion beat occurs when a supraventricular and a ventricular impulse coincide to produce a hybrid complex. It indicates that there are two foci of pacemaker cells firing simultaneously: a supraventricular pacemaker (e.g. the sinus node) and a competing ventricular pacemaker (source of ventricular ectopics)""")
                                 elif mprediction[4] == 1:
                                     st.subheader('Your Heart Beat is classified as unknown beat.')
                                     s.write("""#This bascially indicates abnormality for further information contact your Doctor.""")
                                     
                                     

