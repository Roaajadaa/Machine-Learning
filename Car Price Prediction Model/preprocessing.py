{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "1cc74ab2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import MinMaxScaler"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "91a2e3cf",
   "metadata": {},
   "outputs": [],
   "source": [
    "def Reciprocal_transformation(feature_to_transform):\n",
    "    feature_reciprocal_transformation = 1 / feature_to_transform\n",
    "    return feature_reciprocal_transformation\n",
    "\n",
    "def min_max_normalization(dataframe, features_to_normalize):\n",
    "    dataframe_copy = dataframe.copy()\n",
    "    scaler = MinMaxScaler()\n",
    "    dataframe_copy[features_to_normalize] = scaler.fit_transform(dataframe_copy[features_to_normalize])\n",
    "    return dataframe_copy\n",
    "\n",
    "def Label_Encoder(The_feature):\n",
    "    label_encoder = LabelEncoder()\n",
    "    The_feature_encoded = label_encoder.fit_transform(The_feature)\n",
    "    return The_feature_encoded\n",
    "\n",
    "def OneHot_Encoder(data, column):\n",
    "    onehot_encoded_columns = pd.get_dummies(data[column], prefix=f'{column}-')\n",
    "    data = pd.concat([data, onehot_encoded_columns], axis=1)\n",
    "    data.drop(column, axis=1, inplace=True)\n",
    "    return data\n",
    "\n",
    "reciprocal_cols = ['passengers']\n",
    "min_max_cols = ['model', 'motor_power', 'car_speedometer', 'ex_owners', 'Number_of_Additions', 'car_license', 'glass']\n",
    "label_encoder_cols = ['model', 'motor_power', 'car_speedometer', 'passengers', 'ex_owners', 'Number_of_Additions', 'car_license', 'glass']\n",
    "one_hot_cols = ['Name', 'color', 'fuel_type', 'origin_car', 'lime_type']\n",
    "\n",
    "def preprocess_data(input_data):\n",
    "    input_df = pd.DataFrame([input_data])\n",
    "\n",
    "    # Reciprocal transformation\n",
    "    input_df[reciprocal_cols] = Reciprocal_transformation(input_df[reciprocal_cols])\n",
    "\n",
    "    # Min-Max normalization\n",
    "    input_df = min_max_normalization(input_df, min_max_cols)\n",
    "\n",
    "    # Label Encoding\n",
    "    for col in label_encoder_cols:\n",
    "        input_df[col] = Label_Encoder(input_df[col])\n",
    "\n",
    "    # One-Hot Encoding\n",
    "    for col in one_hot_cols:\n",
    "        input_df = OneHot_Encoder(input_df, col)\n",
    "\n",
    "    return input_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f1d475c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
