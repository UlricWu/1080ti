

Additionally, during training, the log would show some information about the iteration, loglikehood and so on. I jsut wonder how to set the max number of ierations and the threshold at the begining of the calling the model.


# Performance comparison between Monthly Data and Daily Data

**Bug Report** Why Monthly Data with more trining time compared to Day Data?

**Feature Request**Additionally, during training, the log would show some information about the iteration, loglikehood and so on. I jsut wonder how to set the max number of ierations and the threshold at the begining of the calling the model.

`Prophet` [source code](https://github.com/facebook/prophet)
`example.csv` The dataset has three columns, including 'ds', 'y_x', 'y_y'. 'ds' means the date, while 'y_x' and 'y_y' are the value that we are intesested in. Due to the Confidentiality Agreement, those value features are converted already with the same performance and the same issue I mentioned.
`example.ipynb` is the example code to Performance comparison between Monthly Data and Daily Data.

**experiment **

## task 1.
I group by the month to get the month data, and used Prophet to do some forecasting, but I found the total training time on the monthly data is longer than the day -based data. Usually, the more data, the longer time. 3 years daily data sums up to 1095 records and groups by up to 36 records. 

## taks 2
 in order to avoid the incorrect parameters, I used grid search to monitor the total training time on different parameters. I found the same issue that on average,  the monthly data takes longer time to be trained than the day-based data.
 
 ## task 3
  for some parameters take extreme time to be trained, around 20 times of the majority parameters on the monthly data. Not sure what happened, but it's quite interesting.
 
  
