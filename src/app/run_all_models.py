import pandas as pd
import pickle


#LOAD YOUR Dataframe from where to extract metabolite names
samples = pd.read_csv('../data/predictions/samples.csv',index_col=0)
#LOAD YOUR PROTEOMICS DATA: COLUMNS SHOULD BE PROTEIN-ORFS (www.yeastgenome.org) AND INDEX EACH YEAST STRAIN
example = pd.read_csv('../data/predictions/example.csv',index_col=0)

for position in range(726,738):  #go through model and feature 'filter' for each target

#load the featured list for the specific target
#(DF with selected features are named according to the iloc in the 'all_data_13.csv' DataFrame)
    filename = f'../data/selected features/40/{position}.csv'
    features = pd.read_csv(filename,index_col=0).columns.get_values()
    features_example = example[features]
#load the model for the specific target (models are numbered according to the iloc in the 'all_data_13.csv' DataFrame)
    model_filename = f'../models/{position}.sav'
    model = pickle.load(open(model_filename, 'rb'))
    result = model.predict(features_example)
    result = result.clip(min=0)
#add the prediction for each metabolite and strain to the dataframe with column name = metabolite name
    metabolite_name = samples.columns.get_values()[position]
    example[metabolite_name] = pd.Series(list(result), index=example.index)
#save the new dataframe
example_predictions_2 = example.iloc[:,726:738]
filename_example_predictions = '../data/predictions/example_predictions.csv'
example_predictions.to_csv(filename_example_predictions, index=True)
print('Glycolysis and PPP!')

return example_predictions_2