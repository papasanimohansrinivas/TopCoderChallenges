# Debitron ML 

# Folder Ordering

1.Debitron Challenge
		|
		|__ RESULT
		|		|
		|		|__DDB.xlsx
		|
		|
		|__ Scripts
		|		|
		|		|
		|		|__ .ipynb_checkpoints
		|		|
		|		|__Serialised Models
		|		|				|
		|		|				|__LogRmodel_1
		|		|				
		|		|__BankingIndustry.ipynb
		|		|
		|		|__production_model.ipynb
		|		|
		|		|__Untitled.ipynb
		|		|
		|		|__production_model.py
		| 		|
		|		|__model_training.py
		|
		|__ Testing Data
		|		|
		|		|__
		|
		|__ Training Data
		|		|
		|		|__CompiledDDBs_Challenge_v3_2.xlsx
		|       |
		|       |__DataDictionary_Challenge_v2.xlsx
		|		
		|__ Readme.md


## Requirements

1.Python 2.7

2.Pandas library

3.sklearn library

4.Jupyter NoteBook or Anaconda

5.Pickle Library

## Instructions to execute code

1.First Way
		1.Change folder paths accordingly in model_training.py and production_model.py 

		2.Then run production_model.py from cmd

		3.It will create a LogRmodel_1 named file in serialised_model folder

		4.then run model_training.py from cmd 

		5.It will generate DDB.xlsx file in the RESULT folder

2.Second Way
		1.start Jupyter NoteBook from Debitron Challenge folder 

		2.start BankingIndustry.ipynb and run cells upto model_2

		3.model_2 is actually incomplete

		4.It wwill also generate LogRmodel in serialised folder

		5. then start production_model.ipynb in notebook and execute all cells

		6.Same as above It will generate DDB.xlsx in Result folder



#Ideology 

1.I had trained my model on first 20000 data points in excel 

2. Then i validated them against 10000 remaining in dataset 

3. I had got 85.5 accuracy 

4.So i serialised model

5.Given a new dataset my model will classify each user forced debit will get accepted or rejected 

6.Then i moved would_be_rejected people into top rows and sorted both rejected / aprroved guys  each of them by their amount due .



