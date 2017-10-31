import os
import subprocess

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from subprocess import call

def visualize_tree(tree, feature_names):
    """Create tree png using graphviz.

    Args
    ----
    tree -- scikit-learn DecsisionTree.
    feature_names -- list of feature names.
    """
    with open("model.dot", 'w') as f:
        export_graphviz(tree, out_file=f,
                        feature_names=feature_names)

    command = ["dot", "-Tpng", "dt.dot", "-o", "dt.png"]
    try:
        subprocess.check_call(command)
    except:
        exit("Could not run dot, ie graphviz, to "
             "produce visualization")


def main():

	df = pd.read_csv('CampusCrimesMerged.csv')

	# print(df.head())

	model = DecisionTreeClassifier(min_samples_split=20, random_state=99)

	df = df[['Sector of Institution', 'Offense', 'Count']]

	features = ['Sector of Institution', 'Offense']

	# print(df.head())

	

	obj_df = df.select_dtypes(include=['object']).copy()

	obj_df['Sector of Institution'] = obj_df['Sector of Institution'].astype('category')
	obj_df['Offense'] = obj_df['Offense'].astype('category')

	# print(obj_df.dtypes)

	obj_df['Sector of Institution'] = obj_df['Sector of Institution'].cat.codes
	obj_df['Offense'] = obj_df['Offense'].cat.codes

	# print(obj_df.dtypes)

	# X = df.drop('Count', axis=1)

	X = obj_df

	y = df['Count']

	model.fit(X, y)

	with open("CampusCrimes.dot", 'w') as f:
		export_graphviz(model.tree_, out_file=f, feature_names=X.columns)

	call(['dot', '-T', 'png', 'CampusCrimes.dot', '-o', 'CampusCrimes.png'])

if __name__ == "__main__": main()