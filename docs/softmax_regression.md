### Softmax regression

Softmax regression, also known as multinomial logistic regression, is a classification algorithm used for predicting the probability of a categorical dependent variable with more than two categories. It is an extension of logistic regression, which is used for binary classification problems. In softmax regression, the algorithm predicts the probability distribution of a categorical outcome across all possible categories. It computes the probabilities of each category and assigns the observation to the category with the highest probability. The probabilities computed by softmax regression sum up to one, making it suitable for multiclass classification tasks.

The softmax function is used to compute the probabilities of each class. It takes as input a vector of scores (often called logits) and normalizes them into a probability distribution. The formula for softmax function for a class \( j \) is:

$$
\begin{aligned}
\Large P(y = j | x) = \frac{e^{z_j}}{\sum_{k=1}^{K} e^{z_k}}
\end{aligned}
$$

Where:

- $P(y = j | x)$ is the probability that the input $x$ belongs to class $j$.
- $e$ is the base of the natural logarithm (Euler's number).
- $z_j$ is the score (logit) assigned to class $j$.
- $K$ is the total number of classes.

Softmax regression is often used in neural networks as the output layer for multiclass classification tasks. It can be trained using various optimization algorithms such as gradient descent or stochastic gradient descent to minimize the cross-entropy loss between the predicted probabilities and the actual class labels.