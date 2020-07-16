

messy_impute <- function(df, center = 'mean', margin = 2){
  if(!require(matrixStats)){
    install.packages("matrixStats")
    library(matrixStats)
  }

  
  if (center == 'mean'){
    center <- mean
  }else{
    center <- median
  }

  if (margin == 1){
    index <- which(rowSums(is.na(df))!=0)

    for(i in index){
      names <- colnames(df[i,])[colSums(is.na(df[i,])) > 0]
      for(col in names){
        if (col == "Homework_10"){

          temp <- as.numeric(as.vector(df[i,][,2:10]))
          df[i,][col] <- center(temp)
        }
        if (col == 'Exam_3'){
          temp <- as.numeric(as.vector(df[i,][12:13]))
          df[i,][col] <- center(temp)


        }

      }

    }
  }

  if (margin == 2){

    names <- colnames(df)[colSums(is.na(df)) > 0]

    for (name in names){
      val <- center(df[,name], na.rm = TRUE)
      index <- which(is.na(df[,name]) != 0)
      df[index,][,name] <- val

    }


  }
  return( df)
}


tidy_impute <- function(df, center = 'mean', margin = 1){
  if(!require(matrixStats)){
    install.packages("matrixStats")
    library(matrixStats)
  }
  
  
  if (center == 'mean'){
    center <- mean
  }else{
    center <- median
  }
  
  if (margin == 1){
    index <- which(rowSums(is.na(df))!=0)
    
    for(i in index){
      names <- colnames(df[i,])[colSums(is.na(df[i,])) > 0]
      for(col in names){
        if (col == "Homework_10"){
          
          temp <- as.numeric(as.vector(df[i,][,2:10]))
          df[i,][col] <- center(temp)
        }
        if (col == 'Exam_3'){
          temp <- as.numeric(as.vector(df[i,][12:13]))
          df[i,][col] <- center(temp)
          
          
        }
        
      }
      
    }
  }
  
  if (margin == 2){
    
    names <- colnames(df)[colSums(is.na(df)) > 0]
    
    for (name in names){
      val <- center(df[,name], na.rm = TRUE)
      index <- which(is.na(df[,name]) != 0)
      df[index,][,name] <- val
      
    }
    
    
  }
  tidy_format <- df %>% gather(Assignment_Type, Grade, Homework_1:Exam_3,  na.rm = FALSE)
  return(tidy_format)
}
