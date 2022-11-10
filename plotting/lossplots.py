import sys
sys.path.append('..')
from utils.TrainingUtils import *
import h5py
fin = "../../CASEUtils/jet_images/jet_testfiles/X3000_Y700.h5" #signal we're testing
bkg = "../../CASEUtils/jet_images/jet_testfiles/QCD-HT2000toInf.h5" #background we're testing
plot_dir = "plotting/plots/"
model_name = "../../CASEUtils/jet_images/AEmodels/AEs/jrand_autoencoder_m2500.h5" 
jet_type = 'j2_images' # or 'j1_images'


fsignal = h5py.File(fin, "r")[jet_type][()]
fbkg =h5py.File(bkg, "r")[jet_type][()]
model = tf.keras.models.load_model(model_name)
fsignal = np.expand_dims(fsignal, axis = -1)
fbkg = np.expand_dims(fbkg, axis = -1)
reco_signal = model.predict(fsignal, batch_size = 1)
reco_bkg = model.predict(fbkg, batch_size = 1)

sig_score =  np.mean(np.square(reco_signal - fsignal), axis=(1,2))
bkg_score = np.mean(np.square(reco_bkg - fbkg), axis=(1,2))

xhy = fin.split('/')[-1].split('.')[0]
qcd = bkg.split('/')[-1].split('.')[0]


#Plotting
colors = ["g", "b", "r", "gray", "purple", "pink", "orange", "m", "skyblue", "yellow", "lightcoral", "gold","olive"]
hist_labels = ["Background", "Signal"]
hist_colors = ["b", "r"]
hist_scores = [bkg_score, sig_score]
print(np.max(bkg_score))
print(np.max(bkg_score))
make_histogram(hist_scores, hist_labels, hist_colors, 'Labeler Score', qcd +"_background_and_"+ xhy +"_XtoHY_Signal_for_" + jet_type  , 100,
            normalize = True, fname = qcd +"_Background_and_"+ xhy +"_XtoHY_Signal_for_" + jet_type +".png")



