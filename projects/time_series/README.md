Why Monthly Data with more trining time compared to Day Data

Hello, all. Prophet is a great tool for time series forecasting. Thank you.

However, I came up with some issues, and hope you can help me out of there.

First, I have a dataset that contains the day-day data for two features, y_x and x_x and . The thing is that, I group by the month to get the month data, and used Prophet to do some forecasting, but I found the total training time on the monthly data is longer than the day -based data. Usually, the more data, the longer time. 3 years daily data sums up to 1095 records and groups by up to 36 records. 

Secondly, in order to avoid the incorrect parameters, I used grid search to monitor the total training time on different parameters. I found the same issue that on average,  the monthly data takes longer time to be trained than the day-based data.

Thirdly , for some parameters take extreme time to be trained, around 20 times of the majority parameters on the monthly data. Not sure what happened, but it's quite interesting.

Additionally, during training, the log would show some information about the iteration, loglikehood and so on. I jsut wonder how to set the max number of ierations and the threshold at the begining of the calling the model.



The dataset that I used is benig a little transformed for the sake of Confidentiality Agreement, but still with the same facts. Here is the .  [source code](https://github.com/UlricWu/1080ti/tree/master/projects/time_series)