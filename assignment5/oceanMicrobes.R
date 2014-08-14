# Reading the data
data <- read.csv("seaflow_21min.csv")

# Q1. How many particles labeled "synecho" are in the file provided?
sum(data$pop=="synecho")

# Q2. What is the 3rd Quantile of the field fsc_small?
summary(data)

# Creating train and test subsets of the data.
trainIndices <- sample(1:length(data[,1]), size = length(data[,1])/2)
train <- data[trainIndices,]
test <- data[-trainIndices,]

# Q3. What is the mean of the variable "time" for your training set? 
mean(train$time)

# plotting the data
library(ggplot2)
ggplot(data, aes(x=pe, y=chl_small, col=pop)) + geom_point()

# Training a decision tree
library(rpart)
fol <- formula (pop ~ fsc_small + fsc_perp + chl_small + pe + chl_big + chl_small)
treeModel <- rpart(fol, method="class", data=train)

# Use print(model) to inspect your tree.
# Q5. Which populations, if any, is your tree incapable of recognizing?
# Q6. What is the value of the threshold on the pe field learned in your model?
# Q7. Which variables appear to be most important in predicting the class population?
print(treeModel)

# Q8. How accurate was your decision tree on the test data? Enter a number between 0 and 1.
treePrediction <- predict(treeModel, test, type="class")
sum(treePrediction == test[,12])/length(test[,12])

# Building and evaluating a random forest
library(randomForest)
forestModel <- randomForest(fol, data=train)

# Q9. What was the accuracy of your random forest model on the test data? Enter a number between 0 and 1.
forestPrediction <- predict(forestModel, test, type="class")
sum(forestPrediction == test[,12])/length(test[,12])

# Q10. Which variables appear to be most important in terms of the gini impurity measure?
importance(forestModel)

# Training a support vector machine model and comparing results.
library(e1071)
svmModel <- svm(fol, data=train)

# Q11. What was the accuracy of your support vector machine model on the test data? Enter a number between 0 and 1.
svmPrediction <- predict(svmModel, test, type="class")
sum(svmPrediction == test[,12])/length(test[,12])

# Q12. Construct a confusion matrix for each of the three methods using the table function. What appears to be the most common error the models make?
table(pred = treePrediction, true = test$pop)
table(pred = forestPrediction, true = test$pop)
table(pred = svmPrediction, true = test$pop)

# Q13. The variables in the dataset were assumed to be continuous, but one of them takes on only a few discrete values, suggesting a problem. Which variable exhibits this problem?
for(i in 6:11)
  print(length(unique(data[,i])))

# Finding miscalibrated file
ggplot(data, aes(x=time, y=chl_big, col=pop)) + geom_point()
ggplot(data, aes(x=time, y=chl_big, col=file_id)) + geom_point()

# Q14. After removing data associated with miscalibrated file, what was the effect on the accuracy of your svm model?
# Enter a positive or negative number representing the net change in accuracy, where a positive number represents an improvement in accuracy and a negative number represents a decrease in accuracy.
dataClean <- data[data[,"file_id"]!=208,]
trainCleanIndices <- sample(1:length(dataClean[,1]), size = length(dataClean[,1])/2)
trainClean <- dataClean[trainCleanIndices,]
testClean <- dataClean[-trainCleanIndices,]
svmModelClean <- svm(fol, data=trainClean)
svmPredictionClean <- predict(svmModelClean, testClean, type="class")
sum(svmPredictionClean == testClean[,12])/length(testClean[,12])
sum(svmPredictionClean == testClean[,12])/length(testClean[,12]) - sum(svmPrediction == test[,12])/length(test[,12])
